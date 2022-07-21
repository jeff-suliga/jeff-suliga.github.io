#!/bin/bash

# Must be run from project's root folder

read -p 'Puzzle Title (no spaces): ' PUZZLE_NAME
read -p 'Puzzle Answer: ' PUZZLE_ANS

touch Puzzles/$PUZZLE_NAME.md
touch Puzzles/$PUZZLE_NAME-$PUZZLE_ANS.md

cat Puzzles/Puzzle_Template.txt >> Puzzles/$PUZZLE_NAME.md
cat Puzzles/Solution_Template.txt >> Puzzles/$PUZZLE_NAME-$PUZZLE_ANS.md

if [[ ! -e images/$PUZZLE_NAME ]]
then
    echo 'Puzzle images folder not found. Creating folder now...'
    mkdir images/$PUZZLE_NAME
fi