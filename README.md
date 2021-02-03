
# asimpleapi

## A Simple API (with Flask)

#### Summary

This repository contains code demonstrating a simple API using the [Flask web application framework](https://flask.palletsprojects.com). `HTTP`
methods `GET` and `POST` are used, each returning JSON and HTML responses based on the client request header `Accept: application/json`

Two methods of installing and running the application are shown below, Local or with Docker. Choose which is best given your available compute resources and environment.

Also included here is a simple unit test using the [pytest](https://pytest.org) testing framework.

#### Requirements

The following are required for a local installation:

* Python 3.6+
* Python modules: Flask, [flask_accept](https://pypi.org/project/flask_accept), [pytest](https://pytest.org)


    pip install flask
    pip install flask_accept
    pip install pytest

The following are required for a Docker installation:

* [Docker](https://docker.com) CE/EE 17+


#### Repository Structure

    .
    |-- Dockerfile
    |-- README.md
    |
    |-- app
    |   |-- main.py
    |-- tests
    |   |-- test_main.py
    |   |-- quick_test.sh


#### Installation

Prior to running the application either locally or with Docker, determine if debug logging is desired and whether the API should available only for local
access (127.0.0.1), the default, or from other networks (0.0.0.0). Edit the following parameters based on preferences.

 `mydebug = False` - The default. Only INFO logging messages are printed to console (logging.StreamHandler)
 `mydebug = True` - Prints DEBUG messages to console in the form of: request ip address - request url - request method

 `app.run()` - The default and recommended setting.
 `app.run(host='0.0.0.0')` - Allows access from any network. May be scoped to specific network segments (refer to Flask documentation).

#### Installation - Local

Clone this repository and run the application directly:

    git clone https://github.com/kkruzich/asimpleapi.git
    python3 asimpleapi/app/main.py


#### Installation - Docker (optional)

Docker may be used to run the application. The following clones the repository, creates a docker image and container, and displays the logs of the running container. Use `docker logs myflaskid` repeatedly to view recent request entries.

    git clone https://github.com/kkruzich/asimpleapi.git
    cd asimpleapi

    docker build -t myflask .
    docker run -d --name myflaskid -p 5000:5000 myflask
    docker ps
    docker logs myflaskid


#### Testing - Quick Tests

A 'quick test' shell script `tests/quick_test.sh` included to verify connection to and responses from the application.

#### Testing - Unit Tests

It isn't necessary to run the application to perform the unit test. Running the tests is very simple:

    cd tests
    py.test

Upon success, output similar to the following will be printed:

    5 passed in 0.60s
