---
layout: post
title: Complex Rotations
extenstion: ComplexRotations
publish-date: June 16, 2022
description: Multiplying complex numbers visually
---

My goal for this post is to provide a more intuitive and staisfying way to understand solve problems with complex numbers. If solving for z in expressions such as

\\(z=i^{n}, n \in \mathbb{Z};\quad\quad\\) or \\(z=re^{i\theta};\quad\quad\\) or even \\(z=(\sqrt{2} + i\sqrt{2})^{4};\quad\quad\\) or even better \\(z=\sqrt{4(\frac{1}{2}+i\frac{\sqrt{3}}{2})}\\)

leave you wondering where to even start trying to evaluate - good! By the end of this I hope that you will have the tools you need to evaluate these, and be able to explain them to others.

-----

### What Are Complex Numbers?

Skip this section if you are familiar with what complex numbers are.

Let's start with the basics. *What is a complex number?*

A complex number, we will first define as any number \\(z\\) which can be written as \\(z=a+bi\\) with \\(a\\) and \\(b\\) as real numbers. We're all familiar with the real numbers, these are any number that you might see in everyday math: integers, fractions, decimals, irrationals such as \\(\sqrt{2}\\) and the famous values \\(\pi\\) or \\(\phi\\).

In mathy notation, this can be written as the following:

\\[z \in \mathbb{C} \iff (\exists a,b\in\mathbb{R}) \space z=a+bi\\]

This may look confusing, but in plain English this reads:

"\\(z\\) is a complex number provided (if and only if) there exists real numbers \\(a\\) and \\(b\\) such that \\(z=a+bi\\)"

Here you might wonder what this \\(i\\) figure is, and why it's important enough to separate the \\(a\\) and \\(b\\) into separate values. As it happens, just about every number you could think of is a real number, until you realize that math has rules that you have to play around. One of these rules you may have been told is:

<p style="text-align:center;font-style:italic;">"You cannot sqaure root a negative number!"</p>

This is true, but *only when playing within the rules of real numbers*. As it turns out, in the late 1500s a mathematician was trying to create a formula for finding roots of a cubic polynomial - they were trying to find a "[quadratic equation](https://en.wikipedia.org/wiki/Quadratic_equation)" but for polynomials of the form \\(ax^{3}+bx^{2}+cx+d=0\\). In their final formula, which was mathematically accurate for finding these roots, they noticed that it was possible for some input values to end up with a square root of a negative number in their final solution.

For a long while this discovery was ignored, because *surely* this cannot be meaningful, it's just a side effect of certian inputs to the formula. This value cannot be found anywhere on our real number line, so what would we even do with it? Where would we put it? This is where \\(i\\) comes in, the *imaginary unit*. When we started taking this square root of a negative seriously, we defined it to be \\(i=\sqrt{-1}\\), of which all square roots of negatives are multiples of, and a whole bunch of interesting things started happening. To this day, the field of *Complex Analysis* remains an actively taught and researched math field, centered around this idea of \\(i\\).

**Note:** All square roots of negative numbers are multiples of \\(i\\): \\[\sqrt{-5}=\sqrt{-1 \times 5}=\sqrt{-1}\times\sqrt{5}=i\sqrt{5}\\] with \\(\sqrt{5}\\) being a real number.

*Side Note*: I despise the use of the term "imaginary" used to describe these values. I would much prefer something like "transcendental" to describe how this value does not fit into our usual real numbers. Unfortunately, [transcendental numbers](https://en.wikipedia.org/wiki/Transcendental_number) already mean something else.

-----

### Graphing Complex Numbers

As mentioned above, we can see that the imaginary unit cannot be found anywhere on this real number line.

![Real Number Line]({{ site.imgurl }}/RealNumberLine.png)

However, we notice that a value can contain both a purely real component and a imaginary component, dividing this new form of number into 2 dimensions. This 2-dimensional number is what we call a *Complex Number* as seen above.

**Important Note:** Any number that is either purely real or purely a multiple of the imaginary unit (ex: \\(7.5\\), \\(0\\), \\(4i\\)) is still a complex number as either the \\(a\\) or \\(b\\) (or both) in (\\a+bi\\) can be the real number 0.

To represent real valued numbers we can plot them on a 1-dimensional line like the one seen above. For complex numbers we can do a similar thing, using a 2-dimensional plane to show both real and imaginary components.

![Complex Plane]({{ site.imgurl }}/ComplexPlane.svg)

**Note:** In this representation, you can think of a complex number \\(z=x+yi\\) as having "\\(x\\) and \\(y\\) coordinates" on a standard cartesian xy-plot.
Using this was actually the key way of thinking for solving a homework problem in one of my math classes this past year. For the more advanced, the problem was, \\(Prove \quad \mathbb{C}\cong \mathbb{R}^{2}\\)

-----

### Multiplying by \\(i\\)

Using the definition of \\(i\\), we can use some algebra to deduce a few things:

\\[i^{1} = i\\]
\\[i^{2} = (\sqrt{-1})^{2} = -1\\]
\\[i^{3} = i \times i^{2} = i \times -1 = -i\\]
\\[i^{4} = i \times i^{3} = i \times -i = -(i^{2}) = -(-1) = 1\\]
\\[i^{5} = i \times i^{4} = i \times 1 = i\\]

From here you'd notice that the values of \\(i^{n}\\) with \\(n\\) being an integer cycle between \\(\{1, i, -1, -i\}\\). This is in fact the first problem that was posed at the beginning of this article.

\\[(]z=i^{n}, n \in \mathbb{Z}\\]

As an evaluation of this expression, a "solution" to this expression could be to state that \\(z\\) cycles between the values above, depending on the value of \\(n\\). Whenever \\(n\\) is a multiple of 4, \\(z\\) will be \\(1\\). If \\(n\\) is one more than a multiple of 4, \\(z\\) is \\(i\\), and so on.

This is a fun pattern to notice, but if you plot these values on the complex plane and see them changing over time, I hope you'd notice there's something deeper at play here. In this and following plots, the real axis is denoted as 'Re' and imaginary axis denoted by 'Im':

[gif of cycle]

Each time we multiply by \\(i\\), it seems we're rotating whatever the previous value was by 90 degrees, or \\(\frac{\pi}{2}\\) radians (we will use radians from now on). More importantly, it almost seems like we are tracing out the outline of a circle by rotating around.