#!/bin/bash
# Write a Bash script that takes in a URL and displays the body of the response
curl -d "@$1" -H "Content-Type: application/json" 0.0.0.0:5000/route_json
