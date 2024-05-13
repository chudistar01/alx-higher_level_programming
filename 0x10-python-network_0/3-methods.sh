#!/bin/bash
#script that displays all HTTP methods
curl -sI "$1" | grep -i "Allow" | awk '{print "$2"}' | tr -d '\r'
