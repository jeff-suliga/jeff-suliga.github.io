#!/bin/bash

# Must be run from project's root folder

read -p 'Post name: ' POST_NAME

POST_PATH=$(sed "s/ //g" <<< $POST_NAME)

echo "Creating file Posts/$POST_PATH/$POST_PATH.md"
echo $'Make sure to change the file name, file fm, and in posts.yml if you want a different name.\n'
mkdir Posts/$POST_PATH
touch Posts/$POST_PATH/$POST_PATH.md

if [[ ! -e images/Posts/$POST_PATH ]]
then
    echo Post images folder not found. Creating images/Posts/$POST_PATH folder now... $'\n'
    mkdir images/Posts/$POST_PATH
fi