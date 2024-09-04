#!/bin/bash
# Write a Bash script that displays all HTTP methods the server will accept.
curl -si $1 | sed -n 's/^Allow//p'
