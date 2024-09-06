#!/bin/bash
# Write a Bash script that displays the body of the response
curl -sL -w "%{http_code}" -o /dev/null "$1"
