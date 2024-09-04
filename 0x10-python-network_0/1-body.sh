#!/bin/bash
# Write a Bash script that displays the body of the response
curl -w "%{http_code}\n" -s -o /dev/null
