---
layout: puzzleSol
title: Pool Tables Solution
flavortext: At the most elite level, competitors rely more on feeling than on sight in this simple sport of shooting spheres.
puzzle-folder: PoolTables
img-path: PoolTables.jpg
img-height: 600
---

<p align="center">
    <img src="{{ site.imgurl }}/{{ page.puzzle-folder }}/{{ page.img-path }}" alt="{{ page.puzzle-title }}" style="width:100%;height:{{page.img-height}}px;object-fit:contain;">
</p>

-----

For this puzzle, the player is first placed in front of 7 pool tables with colored balls strewed within them.

**Discovery 1:** Braille

The flavortext hints at using "feeling rather than sight" to play this game. This is intended to lead the player into realizing that this picture is an encoding of a message in braille. Treating each pool table as a braille character, one can produce the following message:

![Rainbow]({{ site.imgurl }}/PoolTables/PoolTablesSolution1.png)

**Discovery 2:** Finding the Rainbow

Once the player has decoded the message *Rainbow*, they'll notice that every ball on the tables is one of the colors of the rainbow, or black. This means they now need to focus on the colors of the balls individually, which yields the following pattern:

![Rainbow Colored]({{ site.imgurl }}/PoolTables/PoolTablesSolution2.png)

We can decode this same message again, but this time in rainbow color order of the balls. Doing this gives the following:

![Banzai]({{ site.imgurl }}/PoolTables/PoolTablesSolution3.png)

This message then translates in braille to **BANZAI**, the answer to this puzzle.
