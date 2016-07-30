# Getting Started

## Install dependencies

Ensure that you have a reasonably new version of node (v5) and npm (v3) installed.

### Install webpack goodies globally:

    sudo npm install -g webpack

    sudo npm install -g webpack-dev-server

### Install project npm dependencies

From inside the new_www directory, run

    npm install

### Build semantic

From inside the new_www/semantic directory, run

    gulp build

## Start webpack dev server

From inside the new_www directory, run

    webpack-dev-server --inline --hot

## Start deving

Now navigate to http://localhost:8000/ (Or wherever it might be serving from)
