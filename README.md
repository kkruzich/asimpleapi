
# asimpleapi

## A Simple API (with Flask)

### Summary

This repository contains code demonstrating a simple API using the [Flask web application framework](https://flask.palletsprojects.com). `HTTP`
methods `GET` and `POST` are used, each returning JSON and HTML responses based on the client request header `Accept: application/json`

Two methods of installing and running the application are shown below, Local or with Docker. Choose which is best given your available compute resources and environment.

Also included here is a simple unit test using the [pytest](https://pytest.org) testing framework.

### Requirements

The following are required for a local installation:

* Python 3.6+
* Python modules: Flask, [flask_accept](https://pypi.org/project/flask_accept), [pytest](https://pytest.org)

    ```
    pip install flask   
    pip install flask_accept   
    pip install pytest   
    ```

The following are required for a Docker installation:

* [Docker](https://docker.com) CE/EE 17+


### Repository Structure

    .
    |-- Dockerfile
    |-- README.md
    |
    |-- app
    |   |-- main.py
    |-- tests
    |   |-- test_main.py
    |   |-- quick_test.sh


### Installation - Overview

Prior to running the application either locally or with Docker, determine if debug logging is desired and whether the API should available only for local
access (127.0.0.1), the default, or from other networks (0.0.0.0). Edit the following parameters based on preferences.

 `app/main.py`:

 `mydebug = False` - The default. Only INFO logging messages are printed to console (`logging.StreamHandler`)   
 `mydebug = True` - Prints DEBUG messages to console in the form of: request ip address - request url - request method

 **_Note:_** If Docker is chosen as the preffered means of running the application, access from any network will be the default. See `/Dockerfile`

 `app.run()` - The default and recommended setting for local installation.   
 `app.run(host='0.0.0.0')` - Default for Docker. Allows access from any network. May be scoped to specific network segments (refer to Flask documentation).  

### Installation and Run - Local

Clone this repository and run the application:

    git clone https://github.com/kkruzich/asimpleapi.git
    cd asimpleapi/app
    export FLASK_APP=main
    flask run

Output similar to the following will indicate the application is running properly:

    2021-02-03 16:20:58,987 - INFO -  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Point a web browser to `http://127.0.0.1:5000` or use curl `curl http://127.0.0.1:5000`. Either of these will return the text, 'Hello, World'. See **Quick Tests** below for full verification of the running application. 

### Installation and Run - Docker (optional)

Docker may be used to run the application. The following clones the repository, creates a docker image and container, and displays the logs of the running container. Use `docker logs myflaskid` repeatedly to view recent request entries.

   **_Note:_** If Docker is chosen as the preffered means of running the application, access from any network will be the default. See `/Dockerfile` and **Installation - Overview** above.

    git clone https://github.com/kkruzich/asimpleapi.git
    cd asimpleapi

    docker build -t myflask .
    docker run -d --name myflaskid -p 5000:5000 myflask
    docker ps
    docker logs myflaskid

To remove the docker container and image:

    docker container stop myflaskid
    docker container rm myflaskid
    docker image rm myflask


### Testing - Quick Tests

A 'quick test' shell script `tests/quick_test.sh` included to verify connection to and responses from the application. Edit the 
variable `TARGET` if testing a remote instance. The script is a series of `curl` commands which will produce output similar to the 
following:

    GET with HTML:
    <p>Hello, World</p>

    GET with JSON:
    {"message":"Hello, World"}

    POST with HTML:
    <p>Hello, World</p>

    POST with JSON:
    {"message":"Hello, World"}


### Testing - Unit Tests

Before running Unit Tests, verify the application _is not_ running. Be certain to copy the most recent version of `/app/main.py` to 
the `/tests` directory.

    cd tests
    cp ../app/main.py . 
    py.test

Upon success, output similar to the following will be printed:

    4 passed in 0.60s

