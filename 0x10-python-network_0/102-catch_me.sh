#!/bin/bash
# Write a Bash script that displays the body of the response
curl -sL 0.0.0.0:5000/catch_me_2 -X PUT -d "user_id=98" -H "Origin: School"
