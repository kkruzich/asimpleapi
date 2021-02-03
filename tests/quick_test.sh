#!/bin/bash

echo "GET with HTML:"
curl -X GET http://127.0.0.1:5000/; echo

echo "GET with JSON:"
curl -X GET -H "Accept: application/json" http://127.0.0.1:5000/; echo 

echo "POST with HTML:"
curl -X POST http://127.0.0.1:5000/; echo 

echo "POST with JSON:"
curl -X POST -H "Accept: application/json" http://127.0.0.1:5000/; echo

