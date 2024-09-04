#!/bin/bash
# Write a Bash script that displays the body of the response
curl -w "%{http_code}" -s -o /dev/null $1
