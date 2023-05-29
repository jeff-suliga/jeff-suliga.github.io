---
layout: puzzleSol
title: Extra Credit Solution
flavortext: Mr. Suliga is offering extra credit to those able to solve this last problem on our homework.<br>He wants us to show our work since he says we won't need to guess, but also gave us the hint that <em>H is not 5.</em>
puzzle-folder: ExtraCredit
img-height: 700
---

<p align="center">
    {% if page.img-path %}
    <img src="{{ site.imgurl }}/{{ page.puzzle-folder }}/{{ page.img-path }}" alt="{{ page.puzzle-title }}" style="width:100%;height:{{page.img-height}}px;object-fit:contain;">
    {% else %}
    <img src="{{ site.imgurl }}/{{ page.puzzle-folder }}/{{ page.puzzle-folder }}.jpg" alt="{{ page.puzzle-title }}" style="width:100%;height:{{page.img-height}}px;object-fit:contain;">
    {% endif %}
</p>

[//]: <> (Background image by brgfx on Freepik)

-----

Starting this puzzle, the player is shown a simple-looking math problem on a chalkboard in a classroom setting.

**Discovery 1:** Cryptarithm

Reading the text on the chalkboard, the player is told that they are working with a specific type of puzzle, called a *cryptarithm* puzzle. Solving this cryptarithm should seem like the natural first step to this puzzle.

The flavortext tells the player two things - that they won't need to guess at any point solving the cryptarithm, and that the letter *H* in the puzzle does not hold the value *5*.

Upon solving the cryptarithm, the player should find the following relations:

| **Value**  | 0 | 1 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------------|---|---|---|---|---|---|---|---|---|
| **Letter** | F | W | R | S | A | H | E | G | N |

Here's a sample walkthrough of a way to solve the cryptarithm:

<iframe width="100%" height="550px"
    src="https://www.youtube.com/embed/[TODO]">
</iframe>

**Discovery 2:** Looking under the ANSWER

From the chalkboard, the player is told that they should look under the answer after they have found it.

Out of the nine letters used in the cryptarithm, six of them can be used to spell *ANSWER*.

| **Letter** | A | N | S | W | E | R |
|------------|---|---|---|---|---|---|
| **Value**  | 5 | 9 | 4 | 1 | 7 | 3 |

Looking below the placements of these numbers on a standard QWERTY-style keyboard (in the only way possible for all the numbers) in this order spells **TORQUE**, the answer to this puzzle.