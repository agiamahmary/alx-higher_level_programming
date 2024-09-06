#!/bin/bash
# Write a Bash script that takes in a URL and displays the body of the response
curl -d @"$2" -H "Content-Type: application/json" "$1"
