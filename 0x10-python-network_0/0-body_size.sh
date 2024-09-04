#!/bin/bash
# Write a Bash script that takes in a URL,
curl -s -w "%{size_download}\n" -o /dev/null $1
