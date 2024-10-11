#!/bin/bash

#file existence check

echo "Enter file name: "
read filename

if [ -e "$filename" ]; then
  if [ -r "$filename" ]; then
    echo "File exists and is readable "
  else
    echo "File exists but is not readable"
  fi
else
    echo "File does not exist"
fi