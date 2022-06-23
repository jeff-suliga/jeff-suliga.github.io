# Caveman Solution

-----

It seems we've uncovered an old civilization's art wall - their language seems less developed, but at least it reads left to right.

<img src="{{ site.imgurl }}/Caveman/Caveman.jpg" alt="Caveman" style="width:100%;height:683px;object-fit:contain;">

-----

This puzzle is all about different styles of braille.

The first step in solving this puzzle is decoding the message on top. This portion is written in standard UEB style braille and spells out

"Six Key Braille"

**Discovery 1:** Six Key Braille

Six Key Braille refers to the way many modern keyboards can be used to type braille characters. Six keys on the keyboard are mapped to each of the six dots that can be filled in for a braille character in the following way:

'F' maps to dot 1

'D' maps to dot 2

'S' maps to dot 3

'J' maps to dot 4

'K' maps to dot 5

'L' maps to dot 6

Where dots 1-6 are labeled in the following manner:

![Braille Dot Numbering]({{site.imgurl}}/Caveman/braille_cells.png)

From here the player will notice that all of the letters in the rest of the puzzle are comprised of groups of these above letters, each representing a single braille character. For example, the sequence "FSJL" would refer to the letter 'X' in UEB, as dots 1, 3, 4, and 6 would be raised.

At this point, jumping ahead and decoding the last section of the puzzle using this method will yield a bunch of characters that don't exist or produce gibberish when using UEB. The player must first take a look at the middle section in red. Decoding this portion with the six key method yields the following message in UEB:

"Nemeth Braille"

**Discovery 2:**  Nemeth Braille

Nemeth braille is a style of braille that was created specifically for the purpose of extending UEB to include mathematical concepts. This includes operations, important functions, exponents, and using a different system for encoding numbers, among other capabilities.

The remaining 7 lines of braille are all written in nemeth braille, and one quickly notices that each line begins with this character:

<img src="{{ site.imgurl }}/Caveman/Nemeth_Number.png" style="width:100%;height:400px;object-fit:contain;">

In nemeth style braille, this character represents the beginning of a sequence that contains numbers. Once the player has decoded this character on the first line of the last section, they know to expect a numeric sequence from each of the rest of the lines as well. Decoding the lines gives the following expressions:

\\(5*4\\)

\\(8-7\\)

\\(3\\)

\\(8*3-4\\)

\\(18-9\\)

\\(10+2\\)

\\(5\\)

These expressions when evaluated yield "20 1 3 20 9 12 5"

Treating 1 as 'A', 2 as 'B' and so on, this expression says **TACTILE**, the answer to this puzzle.

-----

Click [here]({{ site.url }}/#puzzles) to return to the main page.