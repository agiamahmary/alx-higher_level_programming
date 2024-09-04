#!/bin/bash
# Write a Bash script that displays the body of the response
res=$(curl -sL -w " %{http_code}"  "$1")

if [ "${res: -3}" = "200" ];
then
    echo "${res:: -3}"
else
    exit
fi
