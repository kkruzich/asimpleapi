#!/bin/bash

# target ipaddr or hostname
# TARGET="127.0.0.1"
TARGET="localhost"

echo "GET with HTML:"
curl -X GET http://${TARGET}:5000/; echo

echo "GET with JSON:"
curl -X GET -H "Accept: application/json" http://${TARGET}:5000/; echo 

echo "POST with HTML:"
curl -X POST http://${TARGET}:5000/; echo 

echo "POST with JSON:"
curl -X POST -H "Accept: application/json" http://${TARGET}:5000/; echo

