# Terminal Alert Solution

-----

<img src="{{ site.imgurl }}/TerminalAlert/TerminalAlert.png" alt="Terminal Alert" style="width:100%;height:385px;object-fit:contain;">

-----

At the start of this puzzle, the player is presented with a muddled warning message saying that their files have been corrupted. The message is readable but littered with characters that don't seem to belong.

**Discovrey 1:** ASCII and /bin

The first thing the player might notice is the string "[A Star Crossed Information Interference]" that seems to not have been affected by the stated corruption. Taking the first, capitalized letters of this string gives "ASCII," the standardized system for encoding many characters into binary.

The message also references "the /bin on the right." /bin, short for binary, is the protected directory for many operating systems that is used to store binary files. This clues the player to look at the binary digits on the right portion of the border:

![Right Binary]({{site.imgurl}}/TerminalAlert/TerminalAlertSolution1.png)

Translating these strings of binary into characters by their ASCII codes yields the following string:

<p align=center>["-&:-?][^\s]*</p>

**Discovery 2:** Regular Expressions

At the end of the message is a reference to regular expressions, or regex, which is a standard way to search for specific patterns within strings of characters.

Using the string found above as a regular expression to search through the message, the following matches arise:

-----

=(and

$left

;side

>number

&and

?zero

"x3F)

<xor

:0x

$59

-----

These can also be seen [here](https://regex101.com/r/G2g0oN/1).

Removing the first characters that were used to idenitify the regex patterns and placing these together gives the following:

(not left side number and 0x3F) xor 0x59

**Discovery 3:** Bitwise operations

This string acts as directions for the next step of the puzzle. We see here that we now need to use the binary on the left portion or the border and perform some bitwise logical operations on each of them, where 0x represents the start of an eight bit value represented in hexadecimal as is standard.

![Left Binary]({{site.imgurl}}/TerminalAlert/TerminalAlertSolution2.png)

The first value is shown as an example below:

![Bitwise Calculations]({{site.imgurl}}/TerminalAlert/TerminalAlertSolution3.png)

Carrying on in this way of performing the logical operations on the left bytes and using the calculated binary as an ASCII reference yields *STEGANOGRAPHY_*. This, **STEGANOGRAPHY** is the art of hiding secret data within a file or message, and is the answer to this puzzle.

-----

Click [here]({{ site.url }}/#puzzles) to return to the main page.