#!/bin/bash
echo -n "enter your log:"
read str

git add .
git commit -m "$str"
git push origin master