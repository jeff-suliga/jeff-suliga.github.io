---
layout: post
title: Complex Rotations
extenstion: ComplexRotations
publish-date: June 16, 2022
description: Multiplying complex numbers visually
---

My goal for this post is to provide a more intuitive and staisfying way to understand solve problems with complex numbers. If solving for z in expressions such as

\\(z=i^{n}, n \in \mathbb{Z};\quad\quad\\) or \\(z=re^{i\theta};\quad\quad\\) or even better \\(z=\sqrt{4(\frac{\sqrt{2}}{2}+i\frac{\sqrt{2}}{2})}\\)

leave you wondering where to even start trying to evaluate - good! By the end of this I hope that you will have the tools you need to evaluate these, and be able to explain them to others.

-----

Skip this section if you are familiar with what complex numbers are.

Let's start with the basics. *What is a complex number?*

A complex number, we will first define as any number \\(z\\) which can be written as \\(z=a+bi\\) with \\(a\\) and \\(b\\) as real numbers. We're all familiar with the real numbers, these are any number that you might see in everyday math: integers, fractions, decimals, irrationals such as \\(\sqrt{2}\\) and the famous values \\(\pi\\) or \\(\phi\\).

In mathy notation, this can be written as the following:

\\[z \in \mathbb{C} \iff (\exists a,b\in\mathbb{R}) z=a+bi\\]

This may look confusing, but in plain English this reads:

"\\(z\\) is a complex number provided (if and only if) there exists real numbers \\(a\\) and \\(b\\) such that \\(z=a+bi\\)"

Here you might wonder what this \\(i\\) figure is, and why it's important enough to separate the \\(a\\) and \\(b\\) into separate values. As it happens, just about every number you could think of is a real number, until you realize that math has rules that you have to play around. One of these rules you may have been told is:

<p style="text-align:center;font-style:italic;">"You cannot sqaure root a negative number!</p>

This is true, but *only when playing within the rules of real numbers*. As it turns out, in the late 1500s a mathematician was trying to create a formula for finding roots of a cubic polynomial - they were trying to find a "[quadratic equation]("https://en.wikipedia.org/wiki/Quadratic_equation")" but for polynomials of the form \\(ax^{3}+bx^{2}+cx+d=0\\). In their final formula, which was mathematically accurate for finding these roots, they noticed that it was possible for some input values to end up with a square root of a negative number in their final solution.

For a long while this discovery was ignored, because *surely* this cannot be meaningful, it's just a side effect of certian inputs to the formula. This value cannot be found anywhere on our real number line, so what would we even do with it? Where would we put it? This is where \\(i\\) comes in, the *imaginary unit*. When we started taking this square root of a negative seriously, we defined it to be \\(i=\sqrt{-1}\\), of which all square roots of negatives are multiples of, and a whole bunch of interesting things started happening. To this day, the field of *Complex Analysis* remains an actively taught and researched math field, centered around this idea of \\(i\\).

**Note:** All square roots of negative numbers are multiples of \\(i\\): \\[\sqrt{-5}=\sqrt{-1 \times 5}=\sqrt{-1}\times\sqrt{5}=t\sqrt{5}\\] with \\(\sqrt{5}\\) being a real number.

*Side Note*: I despise the use of the term "imaginary" used to describe these values. I would much prefer something like "transcendental" to describe how this value does not fit into our usual real numbers. Unfortunately, [transcendental numbers](https://en.wikipedia.org/wiki/Transcendental_number) already mean something else.

-----

As mentioned above, we can see that the imaginary unit cannot be found anywhere on this real number line.

![Real Numbers]("{{ site.imgurl }}/RealNumberLine.png")

However, we notice that a value can contain both a purely real component and a imaginary component, dividing this new form of number into 2 dimensions. This 2-dimensional number is what we call a *Complex Number* as seen above.

**Important Note:** Any number that is either purely real or purely a multiple of the imaginary unit (ex: \\(7.5\\), \\(0\\), \\(4i\\)) is still a complex number as either the \\(a\\) or \\(b\\) (or both) in (\\a+bi\\) can be the real number 0.

To represent real valued numbers we can plot them on a 1-dimensional line like the one seen above. For complex numbers we can do a similar thing, using a 2-dimensional plane to show both real and imaginary components.

![Complex Plane]("{{ site.imgurl }}/ComplexPlane.svg")