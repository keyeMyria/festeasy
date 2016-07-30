# FestEasy

Tests: [![Circle CI](https://circleci.com/gh/jasrusable/festeasy.svg?style=svg&circle-token=c7a32d51438bd6f2fee752e729560c36b76a4a37)](https://circleci.com/gh/jasrusable/festeasy)

## Quickstart Guide
First, install git and clone the repository:

`git clone git@github.com:jasrusable/festeasy.git`

### Backend

The backend is coded in python3!

#### Install some apt dependencies

`sudo apt-get install python3-dev gcc python-virtualenv libpq-dev`

#### virtualenv

From the root of the repository, create a new virtualenv with:

`virtualenv -p python3 venv`

Now, activate that virtualenv:

`. ./venv/bin/activate`

Install pip dependencies:

`pip install -r requirements.txt`

#### Run dev server

First, activate the virtualenv. From the root of the repository run:

`. ./venv/bin/activate`

Now to run the server:

`python manage.py run-server`

Now if you navigate to [localhost:5000/api/v1/](http://localhost:5000/api/v1/), you will be served the api etc :)

Start hacking!
