---
layout: post
title: Star Theorem
extenstion: Extension (not currently used)
publish-date: In Progress
description: Acute Triangles in the Sky
---

By the end of this post, I hope you'll agree with the following statement:

<p style="text-align:center;font-style:italic;">"There is a zero probability that three randomly placed stars in the sky create an acute triangle."</p>

This claim has been labeled by my friends as Jeff's **Star Theorem**. For those unfamiliar, an acute triangle is a triangle whose angles are all strictly less than \\(90^{\circ}\\).

Most people after hearing this statement feel comfortable disagreeing, if not with a mathematical argument then with the fact that, one can look up at the night sky and pick out many groups of three stars that create acute triangles.

In fact, that's exactly where this idea originated. I distinctly remember the summer following my Junior year of high school, taking a weekend trip with some friends to a lake near where we live. One night some of us decided to go down to the beach and watch the night sky and, amidst laughter and late-night conversation between my friends around me and music playing that I had mentally tuned out, I found myself creating these triangles between triplets of stars found in that night sky. Playing around in my mind with the consequence of moving these triangle's vertices around in the continuous plane of reference that I had, led me to that above realization - that to randomly choose three vertices of a triangle in the night sky means this triangle has a zero probability - a zero percent chance - of being an acute triangle.

That's a fun thought - that somewhere out there in the cosmos lie three individual stars that first sparked this interesting realization of mine.

-----

### Possible with Probability Zero

You may notice that I keep saying that this event has a *zero probability* of occurring, and there's a specific reason for this. I use these words because this event is not *impossible*, and there's a subtle difference in this case between the meaning of those words that comes inherent to the continuous nature of placing stars among the night sky. That's what we'll explore here.

This is the very first problem most people have with our claim, is that it's clearly possible to create an acute triangle with stars in the sky, and I'll never argue with that. There are lots of examples of this in the sky that you could point out this evening. In fact, there are *infinitely many* ways to make an acute triangle by placing stars in the sky, yet the probability of this happening by chance remains zero. Sit tight, there's more on comparable infinities in a bit.

I have a very simple way of describing how events that are possible can still have probability zero of occurrance. If I asked you to find the probability that a random number chosen from from integers 0 to 9 (inclusive) is 5, you would easily give me the answer 0.1 (10%). You found this answer by using a formula that we all know, whether we realize it or not:

\\(Probability\space of\space Success \space = \space \frac{Amount\space of\space Successful\space Outcomes}{Total\space Number\space of\space Outcomes}\\)

In this instance, our selection set was formed from a discrete set of values - the integers from 0 to 9 - which made this above calculation trivial. One outcome where the chosen number is 5 and 10 total outcomes implies that the probability of randomly selecting a 5 is 0.1.

Now let's change the rules a little bit. What if I instead asked you to find the probability that a random number chosen from *real numbers* 0 to 9 is 5? Clearly the number 5 is included in this set as a possible outcome, but so is 5.01, 5.00001, and 4.9999999... and each of the infinitely many numbers in between, meaning the \\(Total\\) \\(Number\\) \\(of\\) \\(Outcomes\\) in this instance is infinity. So this outcome is not impossible, yet absurdly unlikely. Probability zero unlikely.

In the same way, we can say that the probability of choosing any number *except* 5 randomly from this set has probability 1, but not certain.

There's a small but important difference between these two questions, and I hinted at it before. In the first example, we were choosing from what we call a *discrete set* of values, meaning there are distinct values in the set such that each value is "isolated" from the rest. In the second example we have what we call a *continuous set*, as each element is no longer isolated from the elements surrounding it\*. I like to think of a discrete set as a set that can be listed. In this first example you can write down the numbers in the set, starting with 0 and counting up to 9. In the second example, to list the numbers you would start out at 0, and then be left searching for the "next value" to write down out of our set of real numbers.

There's a lot that could be said about how we calculate probabilities of continuous sets, the difference between using sums and integrals for this calculation, or even the usefulness of the probability of a specific value in a continuous setting - but the conclusion remains that the one instance of 5 in an infinitely large set yields a probability of 0 for it being chosen at random. And the ones in distress by this comment can find solace in that, for this question of stars making triangles, we actually will not be pulling a discrete success set from a continuous set - we'll be comparing the sizes of two infinitely large continuous sets.

\*I believe this difference and many other aspects of this claim that I will argue have clear explanation using aspects of a field of maths called *Measure Theory*, which I see as the math of *density*. I don't have any formal education or much personal research in this area, so for the more advanced than I, I would love to hear any connections that can be made between this claim we are investigating and measure theory. It's a field that I've become more and more interested in learning about as I advance in my maths education.

-----

### Assumptions

Before we begin, we have to first construct some boundaries for our problem. To start, we will assume we are working with an infinitely large region of space to place stars in. The physicist among you would likely argue with this, as we believe the size of the universe is, at any given moment, of finite size. However we also believe the size of our universe is expanding without bound faster than the speed of light, so for this reason we will be taking this trend towards infinite space as an instantaneous reality.

For now to make visualization easier, we will be working with a 2-dimensional view of space rather than our usual 3 dimensions. Think of taking all of 3D space and projecting it onto your frame of view when looking at the sky, as I first did. Don't worry, we will later extend our argument into 3 dimensions.

-----

### Spatial Probabilities

If you're confused on where we'll even begin to calculate any probabilities of these kinds of geometric events, it takes a fun trick that is probably familiar. We will be comparing the sizes of areas where these outcomes can occur.

First think of a dartboard that lies perfectly within a square frame. In geometry we would say that this dartboard is a circle *inscribed* in a square.

![Circle inscribed in a square]({{site.imgposturl}}/StarTheorem/circle-in-square.jpg)

Notice that the radius of this circle is the same as one half of the square's side lengths. Let's call this \\(r\\).

Provided that all dart throws hit within the square frame, and each point within this frame is equally likely to be hit, what is the probability that a dart throw lands on the left half of the frame. It's 50% right? We divided the frame into two sections, and compared the size of our area of success to the size of the total area, not unlike how we picked 5 randomly from our discrete set before.

Under these same assumptions, what would the probability of throwing a dart and hitting the dart board? (Choosing a random point and having it be inside the circle)

It makes intuitive sense that, because each point on this square is equally likely to be hit by the dart, we can say that the overall probability of this occurring is the area of the circle divided by the area of the square.

Area of circle = \\(\pi r^{2}\\)
Area of square = \\(base \times height = 2r \times 2r = 4r^{2}\\)

So the probability of hitting the dartboard = \\(\frac{\pi r^{2}}{4r^2} = \frac{\pi}{4}\\)

Using this way of thinking we can start constructing some triangles.

-----

### Placing Stars

To make a triangle out of stars in the sky, we can say with confidence that we need three stars. Due to the infinite nature of the 2D space we are currently working with, let's assume that these two dots below represent the placement of our first two stars.

![First Two Stars]({{site.imgposturl}}/StarTheorem/two-stars.png)

This assumption might have some of you scratching your heads. What if these stars aren't placed there? What if the one on the right is moved up a little bit?

We have to remember that we're working with an infinite plane here, and that we can turn this plane and "zoom in and out" as much as we want. If the stars are placed closer together than in this image, we can "zoom in" our view so that we see the same thing as above. Similarly if the right star was moved up a little bit, we can rotate our view clockwise such that we see the same as the image.

*-gif of aligning dots*

However, we *cannot* shear the plane in order to achieve this orientation (I don't think) - ponder briefly why we can't do that.

So at this point we've placed two of the three stars randomly on the plane, and you might realize that the placement of the third will completely determine whether or not the triangle made by connecting the stars will be an acute triangle. It's important to remember that we are dealing with an infinitely large plane here, so the boundaries of the image actually continue extending without bound.

I encourage you to try to think ahead through the next few steps ahead of time. Try picking any point on this plane and thinking of the type of triangle you create. Now drag this point around and notice how this triangle changes - specifically in what regions does the third star need to be in to create an acute triangle?

![Third Star Movement 1]({{site.imgposturl}}/StarTheorem/third-star-movement1.gif)

Look at this again, but with the following "critical boundaries" defined in black.

![Third Star Movement 2]({{site.imgposturl}}/StarTheorem/third-star-movement2.gif)

You'll notice these colored regions actually show these areas where the triangle is acute and obtuse. Any area in red marks where the triangle is obtuse (has an angle that is strictly greater than \\(90^{\circ}\\)) and any area in blue marks where the triangle is acute. The two upright black lines mark where the triangle is a right triangle (one angle is exactly \\(90^{\circ}\\)).

The right region in red marks where the "Star 1" angle is obtuse and the left region in red marks where the "Star 2" angle is obtuse. My favorite part about this diagram, however, is this circle in the middle. The red region inside this circle marks where the "Star 3" angle is obtuse, but I think a cooler realization comes from when the third star lies on this circle itself.

As a consequence of a [simple geometric theorem](https://www.varsitytutors.com/hotmath/hotmath_help/topics/inscribed-angles) we can see that, when the third star is located anywhere on this circle, using the stars as vertices yields a right triangle here as well. This portion is not relevant to answering our question, but it's still a fun geometric side effect.

![Third Star Circling]({{site.imgposturl}}/StarTheorem/third-star-circle.gif)

-----

[\[Top\]](StarTheorem)