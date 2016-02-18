import json
import requests
import jwt
from datetime import datetime, timedelta
from flask import request, current_app, jsonify
from flask_restful import Resource

from backend import db
from backend.models import User, Cart


def create_token(user):
    payload = {
        'sub': user.id,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(days=14)
    }
    token = jwt.encode(payload, '123')
    return token.decode('unicode_escape')


def parse_token(req):
    token = req.headers.get('Authorization').split()[1]
    return jwt.decode(token, '123')


class Facebook(Resource):
    def post(self):
        access_token_url = 'https://graph.facebook.com/v2.3/oauth/access_token'
        graph_api_url = 'https://graph.facebook.com/v2.3/me'

        params = {
            'client_id': request.json['clientId'],
            'redirect_uri': request.json['redirectUri'],
            'client_secret': current_app.config['FACEBOOK_SECRET'],
            'code': request.json['code']
        }

        # Step 1. Exchange authorization code for access token.
        r = requests.get(access_token_url, params=params)
        access_token = json.loads(r.text)

        # Step 2. Retrieve information about the current user.
        r = requests.get(graph_api_url, params=access_token)
        profile = json.loads(r.text)

        # Step 3. (optional) Link accounts.
        if request.headers.get('Authorization'):
            user = User.query.filter_by(facebook=profile['id']).first()
            if user:
                response = jsonify(message='There is already a Facebook account that belongs to you')
                response.status_code = 409
                return response

            payload = parse_token(request)

            user = User.query.filter_by(id=payload['sub']).first()
            if not user:
                response = jsonify(message='User not found')
                response.status_code = 400
                return response

            u = User(facebook=profile['id'], display_name=profile['name'])
            db.session.add(u)
            db.session.commit()
            token = create_token(u)
            return jsonify(token=token)

        # Step 4. Create a new account or return an existing one.
        user = User.query.filter_by(facebook=profile['id']).first()
        if user:
            token = create_token(user)
            return jsonify(token=token)

        names = profile['name'].split(' ')
        u = User(facebook=profile['id'], first_name=names[0], last_name=names[1])
        u.cart = Cart()
        db.session.add(u)
        db.session.commit()
        token = create_token(u)
        return jsonify(token=token)
