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

data = {
    'local': "module.exports = 'http://localhost:5000/api/'",
    'staging': "module.exports = 'https://festeasy-staging.herokuapp.com/api/'",
    'production': "module.exports = 'https://festeasy-production.herokuapp.com/api/'",
}

data = {
    'website-service/src/apiEndpoint.js': data[args.environment],
}

for path, line in data.items():
    with open(path, 'w') as f:
        f.write(line)
        print("Wrote '{line}' into {path}".format(line=line, path=path))
