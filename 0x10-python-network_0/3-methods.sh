#!/bin/bash
#script that displays all HTTP methods
curl -sI "$1" | grep "Allow" | awk '{print "$2"}' | tr -d '\r'
