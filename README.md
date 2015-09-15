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

`python manage.py run-api`

Now if you navigate to http://localhost:5000, you will be served the api etc :)
Also, http://localhost:5000/api/v1/

Now start hacking.

### Frontend

#### Install some apt dependencies

`sudo apt get install nodejs npm`

#### Install npm modules

Install grunt-cli:

`sudo npm install -g grunt-cli`

From the www directory of the repository, run:

`sudo npm install`

#### Install bower dependencies

From the www directory of the repository, run:

`bower install`

#### Start the grunt watch task

From the www directory, run:

`grunt watch`


#### Start dev HTTP server

From the www directory, run:

`grunt server`

Now navigate to http://localhost:8000 and you should see some stuff, done!

Now start hacking.
