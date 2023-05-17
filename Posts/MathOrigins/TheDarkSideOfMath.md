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
2. [Fields!](#fields)
3. [-1/12](#-frac112)

-----

### Nonintegral Exponents

When we first think of exponentiation, we most likely think of repeated multiplication. \\(2^3=8\\) because you multiply \\(2\\) by itself \\(3\\) times. However, we know this doesn't cover all the ways that exponents are used in our math classes today. We've extended exponents to work out well not only with integral values, but with floating point values as well, even negative ones!

Or have we?

When we look at our current rules for exponentation, it makes a lot of sense from an algebraic standpoint. Letting \\(a\\) be in your favorite algebraic structure, \\(a^b \times a^c\\) will always be \\(a^{b+c}\\), which allows for intuition behind our rules for allowing decimal exponents. And similarly with a bit of algebraic finagling, this also would make sense for negative exponents as well (in abstract algebra, we allow for negative exponents to represent the multiplicative inverse of an element in any structure). In our field of real numbers under our standard operations, we take negative exponents to be divisions, and rational exponents to be roots (and define irrational exponents as the converging value of a converging sequence of rational numbers).

This might cause us to accept the rules that we have and keep moving, but before we do that, let's take a look at how this plays out from a graphical point of view.

This graph below shows the expression \\(y = x^r\\) for a varying \\(r \in \[0, 4\]\\). Look at how nicely the curve flows for positive \\(x\\). It seems that our extension of exponents works well, as there seems to be continuous motion at and in between each of the integral values of \\(r\\), which we already felt comfortable with given our primitive definition of exponentiation.

<p style="text-align:center;">
    <img src="{{site.imgposturl}}/MathOrigins/NonintegralExponents.gif" alt="Nonintegral Exponents">
</p>

But woah woah, wait, what the heck is going on with the negative \\(x\\) values??

It feels to me that this is evidence of our definition of exponents failing to work properly over all reasonable cases. In my mind, under a better exponential definition, the left half of this diagram (from a purely graphical view) should be able to flow freely up and down between the curves we know it should take for integral values such as \\(y = x^2\\) and \\(y = x^3\\). Say what you will about viewing this in the complex space (which is a very valid viewpoint for this question), but I still think that this viewpoint screams of math being manufactured.

A side question this brings up, could we have chosen a definition for exponents that works better for negative inputs than the definition we have, that still preesrves the consistency of using it on positive inputs? I understand this is a huge question with huge ramifications for doing this, but its fair food for thought nonetheless.

There may be something worth saying about the fact that I'm arguing something against an abstract space by using a less abstract space as an example. Maybe the "unabstraction" of what I was mentioning before about the abstract algebra stuff into the real number field that we know and love means we can't just ignore the way we define the relationship between exponents and roots and expect it to work out regardless. Part of me feels like I'm doing a "proof by example" of some sorts with this one.

However! If you also feel this way, then let's take a look at fields!

-----

### Fields!

If you know me, then you know pure math is my jam. My two semesters of abstract algebra may have been my favorite math classes I've taken, and, in thinking through the last part about the exponents, I remembered something that never quite sat well with me in these classes.

Definitions and axioms for algebraic structures can sometimes seem like they're out of left field (hehe) sometimes - for example, why do we require groups to be associative and not commutative? But I've learned to see that these decisions are based on observation of the way existing systems work, and allow us to make the best generalizations about structures that we can see and use in the world and in the realm of existing mathematics.

However, one of the requirements of a field is that every nonzero element has a multiplicative inverse - this is sometimes stated as "fields are closed under division." But why make the nonzero distinction?

We proved early on in my class by using cancellation that the additive identity of a ring (denoted by \\(0\\) from here on) multiplied with any element of the ring is always \\(0\\), and so it makes sense that it would never have a multiplicative inverse in a ring.

We know this makes sense in the field of real numbers under the usual operations (I'm going to call this the "natural field," I don't know if there's a standard term for this) as we tell our elementary schoolers "zero times anything is zero," and similarly "you can't divide by zero." But why is it that, when we're going more abstractly, that this is still always the case?

One could say my reasoning from before shows exactly why this is always the case, but a part of me is still unsettled by the extension from the natural field into the abstract, generic field.

-----

### \\(-\frac{1}{12}\\)

Alright here's where things are about to get *real* wonky.

What would happen if we summed up all of the natural numbers? What would we get if we did \\(1+2+3+4+ \dots \\) to infinity?

In other words, given

\\[S = \sum_{i = 1}^\infty i\\]

...what is \\(S\\)?

Well, the easy answer is \\(\infty\\), or that it doesn't exist due to partial sum divergence, but there are a good number of ways that I've come across that can be used to show that this sum, \\(S\\) actually holds the value \\(-\frac{1}{12}\\).

Soak this one in for a second - what I'm saying is that if we added up *infinitely many positive integers* it can be shown that we can get, not only a **negative** number, but a negative **fraction**! You cannot sit there and tell me this is a natural consequence of the universe.

I first came across this my sophomore year of high school from a video on youtube (I think it was Numberphile but I don't remember), and I still don't really know what to do with it. Say what you will about series divergence but, firstly you have to admit this is weird - that you can arrive at this \\(-\frac{1}{12}\\) in multiple different ways. \\(-\frac{1}{12}\\) doesn't seem like a value that deserves to pop up in this context as other common values might, so what makes it so special here?

I would encourage you to do a little digging on this one online, it was really fascinating to me when I was first exposed to it. My favorite ways to show this are by the analytic continuation of the Zeta function, and by Ramanujan summation. 

-----

Click [here](MathOrigins#extra-content) to return to the main post.

Click [here]({{ site.url }}) to return home.