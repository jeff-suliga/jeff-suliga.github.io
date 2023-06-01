---
layout: post
title: The Chaos Game
---

This post will be somewhat different from the rest in that, I'm not really going to explain much here. The point of this post is to showcase something that I first came across a long time ago, and decided to recreate in MS Paint for fun.

1. [The Motivation](#the-motivation)
2. [The Game](#the-game)
3. [The Results](#the-results)
4. [The Code](#the-code)

-----

### The Motivation

I first learned about this so-called "Chaos Game" (which is actually its standard name) from [this video](TODO) back in high school. I thought it was super cool, but I haven't really thought about it or seen it anywhere since then.

Fast-forward 5 years and I'm learning and playing around with `pyautogui`, a python library that lets me program mouse and keyboard inputs, just because I was curious to see how I could do that. I didn't want to test my programs by just letting it click all over my screen, so I opened up Microsoft Paint - probably the most basic and primitive window I can use to click and track where I'm sending my mouse to go via turtle-esque function calls.

As I'm getting bored with just `moveTo()` and `click()`, I remember this one video I saw a long time ago that describes a game using just those two functionalities to create amazing fractal designs out of randomness - the Chaos Game.

I code up a pretty basic version of this game to be played within my MS Paint window and suddenly become engrossed with toying around with the rules and seeing what I get.

-----

### The Game

The Chaos Game is very simple. The most well-known result uses the following rules:

<p>
<pre>
        1. Place 3 nonlinear vertices somewhere in the open space
        2. Place another point anywhere in the space
        3. Pick one of the 3 vertices at random
        4. Place another point that is halfway between the last point and the randomly chosen vertex
        5. Repeat steps 3 and 4 many times
</pre>
</p>

That's it! Starting with 3 points on a triangle and randomly adding more points around the figure based on this "halfway" rule is the entirety of the game. Before I reveal what the resulting figure would look like under these rules, think on it for yourself - if we started with vertices like these below and a starting point anywhere in the plane, what would happen after doing this process, say, 50000 times?

Would the whole inside of the triangle be filled with scattered points? Would some kind of pattern emerge? Are there any points that are impossible to reach under these rules?

<p style="text-align:center;">
    <img src="{{site.imgposturl}}/ChaosGame/3Vertices.png" alt="3 Starting Vertices">
</p>

Well, here's what actually happens:

<p style="text-align:center;">
    <img src="{{site.imgposturl}}/ChaosGame/SierpinskiTriangle50000.png" alt="Chaos Game Example">
</p>

Alright well we definitely know at this point that there's something going on here. If you haven't seen this before, the shape that we got from this very closely resembles the [Sierpinski Triangle](https://magazine.thingimajigs.com/amazing-sierpinski-triangle/), a self-similar object that can be created by just drawing triangles within triangles ad infinitum.

This is super cool to me - that this super simple procedure with a very random nature describes such a structured design. I won't go into why this emerges, there are some good resources elsewhere online for this, but I instead want to showcase some results that can arise from muddling with the rules a little bit.

However, something that I noticed while creating and playing with my python script is that, if the starting point is a point that is not exactly on the Sierpinski Triangle (including adding larger triangles outside the starting vertices to account for the case where the starting point lies outside of the triangle defined by the vertices), then the pattern will *never* truly reach the Sierpinski Triangle exactly! It will just keep getting closer and closer to the shape as more iterations are run.

Along with this, I think that once a point is marked it'll never be reached again. If this is true, then it follows that, if we know only the very last point chosen over the iterations, then we are able to trace backwards the exact series of points that were drawn to get all the way back to the start (given that our drawing is perfectly precise), which I think is pretty cool.

*Side Note*: I'm not a big fan of the name "Chaos Game" for this procedure. It makes sense intuitively, since the result of this game is order from seeming chaos (I mean, it is *random* for goodness sake, that's about as chaotic and unpredictable as it gets). However, when we use the term *chaotic* in math to describe a system, we generally mean that the system is incredbily sensitive to initial conditions, where the tiniest shift in the starting inputs to a system drastically change the system's behavior over time (see the [double pendulum](https://gereshes.com/2018/11/19/chaos-and-the-double-pendulum/)). But when we look at the chaos game, the results are just about the same regardless of the starting inputs (which is literally just the one starting point).

-----

### The Results

This is the fun part where you get to look at weird pictures of a ton of dots. All of the following pictures have been generated by my script (found in the [next section](#the-code)) and drawn in Microsoft Paint.

When I talk about "playing with the rules" of the chaos game, the first things that I tried were adding more vertices and changing how far to travel to the selcted vertex. In all of the following images, \\(d = 0.40\\) means that, instead of traveling halfway to the selected vertex at each step, you travel \\(40\%\\) of the way.

-----

### The Code

I've put this section last on purpose - I want you to have the best understanding of the process as you can before using the script I wrote. Please read the comment at the beginning of the script before running it, and follow the directions that the popups prompt you to do. It also is worth running `$ python chaos_drawing.py --help` the first time to see all of the input arguments that are available.

Keep in mind that this script was made to be ran with Microsoft Paint. Other image editors will likely work, but may take some tweaking to the global parameters or to `pyautogui`'s variables.

If you haven't done this before, you'll need to

`$ pip install pyautogui`

I also recommend running python in unbuffered mode for stdout by using `$ python -u chaos_drawing.py` for certain output to look cleaner.

There is a `getRandVertex()` function in the script that is used at each step to get the random vertex. This is where you can mess around and change how vertices are selected, such as "don't pick a vertex 2 vertices away from the previously chosen one." I've left some of the additional rules I used for my drawings commented out if you want to try running with those and seeing how it turns out yourself.

One last thing to note for the script, is that `VERTICES`, the list of vertices, keeps track of all of the figure's vertices *in the order they were entered*. This is important if you're trying to implement a new rule such as the one above.

<p style="text-align:center;text-decoration:underline;text-shadow: 2px 2px 5px red;">
    <a href="chaos_drawing.py">Download script here</a>
</p>

-----

[\[Top\]](#)
