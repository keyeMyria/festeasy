import argparse


parser = argparse.ArgumentParser(
    description='Set API endpoints for www and admin_www.'
)

choices = ['staging', 'production', 'local']
parser.add_argument(
    '-e',
    '--environment',
    required=True,
    type=str,
    action='store',
)
args = parser.parse_args()

if args.environment not in choices:
    print('Unkown environment supplied, assuming local.')
    args.environment = 'local'

api_endpoint = {
    'local': "module.exports = 'http://localhost:5000/api/'",
    'staging': "module.exports = 'https://festeasy-staging.herokuapp.com/api/'",
    'production': "module.exports = 'https://festeasy-production.herokuapp.com/api/'",
}
mixpanel_token = {
    'local': "module.exports = '9590d744e2d59d3b1a1c30c7b3eac9cc'",
    'staging': "module.exports = '9590d744e2d59d3b1a1c30c7b3eac9cc'",
    'production': "module.exports = '44c20f043e78cc4696c8b0143d130cb4'",
}

data = {
    'website-service/src/apiEndpoint.js': api_endpoint[args.environment],
    'website-service/src/mixpanelToken.js': mixpanel_token[args.environment],
}

for path, line in data.items():
    with open(path, 'w') as f:
        f.write(line)
        print("Wrote '{line}' into {path}".format(line=line, path=path))
