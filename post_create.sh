#!/bin/bash

# Must be run from project's root folder
# BEFORE RUNNING: Make sure posts.yml has a blank line at the end

read -p 'Post name: ' POST_NAME

POST_PATH=$(sed "s/ //g" <<< $POST_NAME)

# Create new post file
echo $'\n' "Creating file Posts/$POST_PATH/$POST_PATH.md"
echo $'Make sure to change the file name, file fm, and in posts.yml if you want a different name.\n'
mkdir Posts/$POST_PATH
touch Posts/$POST_PATH/$POST_PATH.md

# Create post images folder if it doesn't already exist
if [[ ! -e images/Posts/$POST_PATH ]]
then
    echo Post images folder not found. Creating images/Posts/$POST_PATH folder now... $'\n'
    mkdir images/Posts/$POST_PATH
fi

# Add post template to new file
echo "---
layout: post
title: $POST_NAME
---

content

-----

[\[Top\]](#)" >> Posts/$POST_PATH/$POST_PATH.md

# Add post data to data file. Remove this to prevent deploying to index
echo "- home-title: $POST_NAME
  page-title: [Remove if same as home-title]
  home-description: [Short Description]
  page-description: [Remove if same as home-description]
  publish-date: In Progress
  path: $POST_PATH
  thumb: [Thumbnail file name]" >> _data/posts.yml