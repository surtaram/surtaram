#!/bin/bash

#reverse a string

echo "Enter a string:"
read str
reverse=$(echo "$str" | rev)
echo "Reversed string: $reverse"