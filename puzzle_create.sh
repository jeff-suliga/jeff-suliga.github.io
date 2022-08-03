#!/bin/bash

# Must be run from project's root folder
# BEFORE RUNNING: Make sure puzzles.yml has a blank line at the end

read -p 'Puzzle Title: ' PUZZLE_NAME
read -p 'Puzzle Answer: ' PUZZLE_ANS

PUZZLE_PATH=$(sed "s/ //g" <<< $PUZZLE_NAME)

touch Puzzles/$PUZZLE_PATH.md
touch Puzzles/$PUZZLE_PATH-$PUZZLE_ANS.md

cat Puzzles/Puzzle_Template.txt >> Puzzles/$PUZZLE_PATH.md
cat Puzzles/Solution_Template.txt >> Puzzles/$PUZZLE_PATH-$PUZZLE_ANS.md

if [[ ! -e images/$PUZZLE_PATH ]]
then
    echo 'Puzzle images folder not found. Creating folder now...'
    mkdir images/$PUZZLE_PATH
fi

echo "- name: $PUZZLE_NAME" >> _data/puzzles.yml
echo "  ext: $PUZZLE_PATH" >> _data/puzzles.yml
echo "  link: /Puzzles/$PUZZLE_PATH" >> _data/puzzles.yml
echo '  thumb-ext: [omit if jpg]' >> _data/puzzles.yml

echo $'\nTODO:'
echo $'\tEdit front matter of puzzle md'
echo $'\tEdit front matter of puzzle solution md'
echo $'\tEdit _data/puzzles.yml values so it shows up correctly in index'
echo $'\tAdd puzzle solution explanation'