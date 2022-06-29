# Runaway Worm Solution

-----

<img src="{{ site.imgurl }}/RunawayWorm/RunawayWorm.jpg" alt="Runaway Worm" style="width:100%;height:900px;object-fit:contain;">

-----

Starting this puzzle, the player is faced with a cluttered diagram showing a worm's movements tracked over 7 days, each colored "in order." This order is in rainbow order: Red, Orange, Yellow, Green, Blue, Purple, Black.

**Discovery 1:** Dit N' Dah

The player is also told that the worm's movements throughout a given day are shown by the numbers beside its placement. Tracking these throughout each day by connecting them in numbered order will produce a letter for each day. The "red day" yields 'D' as shown:

<img src="{{ site.imgurl }}/RunawayWorm/RunawayWormSolution1.jpg" style="width:100%;height:550px;object-fit:contain;">

Connecting each set of colors in this way in the order mentioned above gives the phrase "Dit n Dah"

<img src="{{ site.imgurl }}/RunawayWorm/RunawayWormSolution2.jpg" style="width:100%;height:550px;object-fit:contain;">

This, paired with some hints in the clue's description lead the player to realize they should be looking for some kind of morse encoding in the image.

**Discovery 2:** Worm Morse

At this point the player realizes that, each instance of the worm's movement shows it either balled up or stretched out. These are meant to be interpreted as "dits" and "dahs." Again looking at each day individually as a morse character and stringing them together in order, the following message arises:

![Morse Message]({{site.imgurl}}/RunawayWorm/morse_message.png)

Decoding this message gives "5262421"

**Discovery 3:** Soil Horizons

The last bit of information that was given from the puzzle hint that hasn't been used yet, has to do with soil horizons.

The main soil horizons, or layers, that can be found are classified in the following way, starting from the outside of the planet's surface and moving inwards:

<p align=center>

    <span style="font-weight:bold">O, A, E, B, C, R</span>

</p>

At this point the player can see our decoded message "5262421," which only contains numbers 1-6, as referencing different soil horizons. For example, 5 refers to soil horizon 'C'. Continuing in this way gives **CARABAO**, this puzzle's answer.

-----

Click [here]({{ site.url }}/#puzzles) to return to the main page.