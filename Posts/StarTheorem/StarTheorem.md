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

\\[Probability of Success \space = \space \frac{Amount of Successful Outcomes}{Total Number of Outcomes}\\]

In this instance, our selection set was formed from a discrete set of values - the integers from 0 to 9 - which made this above calculation trivial. One outcome where the chosen number is 5 and 10 total outcomes implies that the probability of randomly selecting a 5 is 0.1.

Now let's change the rules a little bit. What if I instead asked you to find the probability that a random number chosen from *real numbers* 0 to 9 is 5? Clearly the number 5 is included in this set as a possible outcome, but so is 5.01, 5.00001, and 4.9999999... and each of the infinitely many numbers in between, meaning the \\(Total Number of Outcomes\\) in this instance is infinity. So this outcome is not impossible, yet absurdly unlikely. Probability zero unlikely.

In the same way, we can say that the probability of choosing any random number *except* 5 from this set has probability 1, but not certain.

There's a small but important difference between these two questions, and I hinted at it before. In the first example, we were choosing from what we call a *discrete set* of values, meaning there are distinct values in the set such that each value is "isolated" from the rest. In the second example we have what we call a *continuous set*, as each element is no longer isolated from the elements surrounding it\*. I like to think of a discrete set as a set that can be listed. In this first example you can write down the numbers in the set, starting with 0 and counting up to 9. In the second example, to list the numbers you would start out at 0, and then be left searching for the "next value" to write down out of our set of real numbers.

There's a lot that could be said about how we calculate probabilities of continuous sets, the difference between using sums and integrals for this calculation, or the usefulness of the probability of a specific value in a continuous setting - but the conclusion remains that the one instance of 5 in an infinitely large set yields a probability of 0 for it being chosen at random. And the ones in distress by this comment can find solace in that, for this question of stars making triangles, we actually will not be pulling a discrete success set from a continuous set - we'll be comparing the sizes of two infinitely large continuous sets.

*\*Side Note:*  I believe this difference and many other aspects of this claim that I will argue have clear explanation using aspects of a field of maths called *Measure Theory*, which I see as the math of *density*. I don't have any formal education or much personal research in this area, so for the more advanced than I, I would love to hear any connections that can be made between this claim we are investigating and measure theory. It's a field that I've become more and more interested in learning about as I advance in my maths education.

-----

[\[Top\]](StarTheorem)