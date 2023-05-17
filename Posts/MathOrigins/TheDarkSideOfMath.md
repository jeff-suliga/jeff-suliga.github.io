---
layout: post
title: The Dark Side of Mathematics...
publish-date: In Progress
---

Welcome to the ***Dark Side of Math >:)***

This page will showcase some weird results that I've come across in math that just don't seem to "work out" as clean as the general view of mathematics would claim they should. These are in no particular order, and isn't really designed to be read through top to bottom. I'll likely be adding to (and possibly removing from) this page somewhat regularly as I come across new ideas or learn to look at these ones in a new way.

For most of these, the reason why they point me to believe that math was invented is that there seems to be an element involved that I like to call "discovering backwards." If you take a dive into some more abstract math, it would seem like math started from very profound observation of the world and how entities interact with one another, and it would seem like we did in fact build math from the ground up starting from basic axioms - but that's not actually what happened at all.

Math started a long time ago as simply counting objects, and it wasn't for a long while after then that we started going a bit deeper and more abstract with our ideas. At this point, we already had plenty of symbols and relationships that were defined that we couldn't just get rid of, and instead had to make sure our abstract thoughts and reasonings worked with the ideas already in place. This is how I think of "discovering backwards."

Enjoy the mess!

1. [Nonintegral Exponents](#nonintegral-exponents)
2. [Fields!](#fields!)

-----

### Nonintegral Exponents

When we first think of exponentiation, we most likely think of repeated multiplication. \\(2^3=8\\) because you multiply \\(2\\) by itself \\(3\\) times. However, we know this doesn't cover all the ways that exponents are used in our math classes today. We've extended exponents to work out well not only with integral values, but with floating point values as well, even negative ones!

Or have we?

When we look at our current rules for exponentation, it makes a lot of sense from an algebraic standpoint. Letting \\(a\\) be in your favorite algebraic structure, \\(a^b * a^c\\) will always be \\(a^{b+c}\\), which allows for intuition behind our rules for allowing decimal exponents. And similarly with a bit of algebraic finagling, this also would make sense for negative exponents as well (in abstract algebra, we allow for negative exponents to represent the multiplicative inverse of an element in any structure). In our field of real numbers under our standard operations, we take negative exponents to be divisions, and rational exponents to be roots (and define irrational exponents as the converging value of a converging sequence of rational numbers).

This might cause us to accept the rules that we have and keep moving, but before we do that, let's take a look at how this plays out from a graphical point of view.

This graph below shows the expression \\(y = x^r\\) for a varying \\(r \in \[-10, 10\]\\). Look at how nicely the curve flows for positive \\(x\\). It seems that our extension of exponents works well, as there seems to be continuous motion at and in between each of the intergral values of \\(r\\), which we already felt comfortable with given our primitive definition of exponentiation.

But woah woah, wait, what the heck is going on with the negative \\(x\\) values??

There may be something worth saying about the fact that I'm arguing something against an abstract space by using a less abstract space as an example. Maybe the "unabstraction" of what I was mentioning before about the algebraic structure stuff into the real number field that we know and love means we can't just ignore the way we define the relationship between exponents and roots and expect it to work out regardless. Part of me feels like I'm doing a "proof by example" of some sorts with this one.

However! If this is true, then let's take a look at fields!

-----

### Fields!

Why is division by zero undefined in a generic field

-----

Linear Algebra "dot product" thing being defined to align with pythagorean theorem (inner product I think is what I was thinking of)

-----

Click [here](MathOrigins#extra-content) to return to the main post.

Click [here]({{ site.url }}) to return home.