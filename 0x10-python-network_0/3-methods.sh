#!/bin/bash
# Write a Bash script that displays all HTTP methods the server will accept.
curl -s -X OPTIONS $1
