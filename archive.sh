#!/bin/bash

# Must be run from project's root folder
# Exit Codes:
#     1 = Not enough Arguments
#     2 = Puzzle not found

OIFS=$IFS
IFS=$'\n'

if [ $# -lt 1 ]
then
    echo "Not Enough Arguments"
    exit 1
fi

if [[ ! -f "./Puzzles/$1.md" ]]
then
    echo "Puzzle $1 not found. Make sure you are running from project root directory"
    exit 2
fi

mkdir ./Puzzles/Archived/$1_A
mv ./Puzzles/$1* ./Puzzles/Archived/$1_A

echo $'\n-----\n' >> ./Puzzles/Archived/ArchivedPuzzles.md
echo "[$1]($1_A/$1)" >> ./Puzzles/Archived/ArchivedPuzzles.md

echo $'\n' >> ./Puzzles/Archived/$1_A/$1-*
echo 'Click [here]({{ site.url }}/Puzzles/Archived/ArchivedPuzzles) to return to the main page.' >> ./Puzzles/Archived/$1_A/$1-*

IFS=$OIFS