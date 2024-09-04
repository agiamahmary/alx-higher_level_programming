#!/bin/bash
# Write a Bash script that displays the body of the response
curl -sL -w "%{http_code}"  "$1" | sed -n 's/200//p'
