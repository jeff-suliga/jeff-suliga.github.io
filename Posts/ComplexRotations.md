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

A complex number, we will first define as any number \\(z\\) which can be written as \\(z=a+bi\\) with \\(a\\) and \\(b\\) as real numbers. We're all familiar with the real numbers, these are any number that you might see in everyday math: integers, fractions, decimals, irrationals such as \\(\sqrt{2}\\) and the famous values \\(pi\\) or \\(phi\\).

In mathy notation, this can be written as the following:

\\[z \in \mathbb{C} \iff (\exists a,b\in\mathbb{R}) z=a+bi\\]

This may look confusing, but in plain English this reads:

"\\(z\\) is a complex number provided (if and only if) there exists real numbers \\(a\\) and \\(b\\) such that \\(z=a+bi\\)"

Here you might wonder what this \\(i\\) figure is, and why it's important enough to separate the \\(a\\) and \\(b\\) into separate values. As it happens, just about every number you could think of is a real number, until you realize that math has rules that you have to play around. One of these rules you may have been told is:

<p style="text-align:center;"><i>"You cannot sqaure root a negative number!</i></p>

This is true, but *only when playing within the rules of real numbers*. As it turns out, in the late 1500s a mathematician was trying to create a formula for finding roots of a cubic polynomial - they were trying to find a "[quadratic equation]("https://en.wikipedia.org/wiki/Quadratic_equation")" but for polynomials of the form \\(ax^{3}+bx^{2}+cx+d=0\\). In their final formula, which was mathematically accurate for finding these roots, they noticed that it was possible for some input values to end up with a square root of a negative number in their final solution.

For a long while this discovery was ignored, because *surely* this cannot be meaningful, it's just a side effect of certian inputs to the formula. This is where \\(i\\) comes in. When we started taking this square root of a negative seriously, we defined it to be \\(i=\sqrt{-1}\\), of which all square roots of negatives are multiples of, and a whole bunch of interesting things started happening. To this day, the field of *Complex Analysis* remains an actively taught and researched math field, centered around this idea of \\(i\\).

-----

Graphing 