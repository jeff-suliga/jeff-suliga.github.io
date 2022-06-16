---
layout: post
title: Complex Rotations
extenstion: ComplexRotations
publish-date: June 16, 2022
description: Multiplying complex numbers visually
---

My goal for this post is to provide a more intuitive and staisfying way to understand solve problems with complex numbers. If solving for z in expressions such as

\\(z=i^{n}, \space n \in \mathbb{Z};\quad\quad\\) or \\(z=re^{i\theta};\quad\quad\\) or even \\(z=(\sqrt{2} + i\sqrt{2})^{4};\quad\quad\\) or even better \\(z=\sqrt{4(\frac{1}{2}+i\frac{\sqrt{3}}{2})}\\)

leave you wondering where to even start trying to evaluate - good! By the end of this I hope that you will have the tools you need to evaluate these, and be able to explain them to others.

-----

### What Are Complex Numbers?

Skip this section if you are familiar with what complex numbers are.

-----

Let's start with the basics. *What is a complex number?*

A complex number, we will first define as any number \\(z\\) which can be written as \\(z=a+bi\\) with \\(a\\) and \\(b\\) as real numbers. We're all familiar with the real numbers, these are any number that you might see in everyday math: integers, fractions, decimals, irrationals such as \\(\sqrt{2}\\) and the famous values \\(\pi\\) or \\(\phi\\).

In mathy notation, this can be written as the following:

\\[z \in \mathbb{C} \iff (\exists a,b\in\mathbb{R}) \space z=a+bi\\]

This may look confusing, but in plain English this reads:

"\\(z\\) is a complex number provided (if and only if) there exists real numbers \\(a\\) and \\(b\\) such that \\(z=a+bi\\)"

Here you might wonder what this \\(i\\) figure is, and why it's important enough to separate the \\(a\\) and \\(b\\) into separate values. As it happens, just about every number you could think of is a real number, until you realize that math has rules that you have to play around. One of these rules you may have been told is:

<p style="text-align:center;font-style:italic;">"You cannot square root a negative number!"</p>

This is true, but *only when playing within the rules of real numbers*. As it turns out, in the late 1500s a mathematician was trying to create a formula for finding roots of a cubic polynomial - they were trying to find a "[quadratic equation](https://en.wikipedia.org/wiki/Quadratic_equation)" but for polynomials of the form \\(ax^{3}+bx^{2}+cx+d=0\\). In their final formula, which was mathematically accurate for finding these roots, they noticed that it was possible for some input values to end up with a square root of a negative number in their final solution.

For a long while this discovery was ignored, because *surely* this cannot be meaningful, it's just a side effect of certain inputs to the formula. This value cannot be found anywhere on our real number line, so what would we even do with it? Where would we put it?

This is where \\(i\\) comes in, the *imaginary unit*. When we started taking this square root of a negative seriously, we defined it to be \\(i=\sqrt{-1}\\), of which all square roots of negatives are multiples of, and a whole bunch of interesting things started happening, including discoveries with very real applications all around us today. To this day, the field of *Complex Analysis* remains an actively taught and researched math field, centered around this idea of \\(i\\).

**Note:** All square roots of negative numbers are multiples of \\(i\\): \\[\sqrt{-5}=\sqrt{-1 \times 5}=\sqrt{-1}\times\sqrt{5}=i\sqrt{5}\\] with \\(\sqrt{5}\\) being a real number.

*Side Note*: I despise the use of the term "imaginary" used to describe these values. I would much prefer something like "transcendental" to describe how this value does not fit into our usual real numbers. Unfortunately, [transcendental numbers](https://en.wikipedia.org/wiki/Transcendental_number) already mean something else.

-----

### Graphing Complex Numbers

-----

As mentioned above, we can see that the imaginary unit cannot be found anywhere on this real number line.

![Real Number Line]({{ site.imgurl }}/RealNumberLine.png)

However, we notice that a value can contain both a purely real component and a imaginary component, dividing this new form of number into 2 dimensions. This 2-dimensional number is what we call a *Complex Number* as seen above.

**Important Note:** Any number that is either purely real or purely a multiple of the imaginary unit (ex: \\(7.5\\), \\(0\\), \\(4i\\)) is still a complex number as either the \\(a\\) or \\(b\\) (or both) in \\(a+bi\\) can be the real number 0.

To represent real valued numbers we can plot them on a 1-dimensional line like the one seen above. For complex numbers we can do a similar thing, using a 2-dimensional plane to show both real and imaginary components.

![Complex Plane]({{ site.imgurl }}/ComplexPlane.svg)

**Note:** In this representation, you can think of a complex number \\(z=x+yi\\) as having "\\(x\\) and \\(y\\) coordinates" on a standard cartesian xy-plot.
Using this was actually the key way of thinking for solving a homework problem in one of my math classes this past year. For the more advanced, the problem was, \\[Prove \quad \mathbb{C}\cong \mathbb{R}^{2}\\] (Group Theory)

-----

### Multiplying by \\(i\\)

Using the definition of \\(i\\), we can use some algebra to deduce a few things:

\\[i^{1} = i\\]
\\[i^{2} = (\sqrt{-1})^{2} = -1\\]
\\[i^{3} = i \times i^{2} = i \times -1 = -i\\]
\\[i^{4} = i \times i^{3} = i \times -i = -(i^{2}) = -(-1) = 1\\]
\\[i^{5} = i \times i^{4} = i \times 1 = i\\]

From here you'd notice that the values of \\(i^{n}\\) with \\(n\\) being an integer cycle between \\(\\{1, i, -1, -i\\}\\). This is in fact the first problem that was posed at the beginning of this article.

\\[z=i^{n}, \space n \in \mathbb{Z}\\]

\\(n \in \mathbb{Z}\\) means "\\(n\\) is an element of the set of integers."

As an evaluation of this expression, a "solution" could be to state that \\(z\\) cycles between the values above, depending on the value of \\(n\\). Whenever \\(n\\) is a multiple of 4, \\(z\\) will be \\(1\\). If \\(n\\) is one more than a multiple of 4, \\(z\\) is \\(i\\), and so on.

This is a fun pattern to notice, but if you plot these values on the complex plane and see them changing over time, I hope you'd notice there's something deeper at play here. In this and following plots, the real axis is denoted as 'Re' and imaginary axis denoted by 'Im':

[gif of cycle]

Each time we multiply by \\(i\\), it seems we're rotating whatever the previous value was by \\(90^{\circ}\\), or \\(\frac{\pi}{2}\\) radians (we will use radians from now on). More importantly, it almost seems like we are tracing out the outline of a circle by rotating around. In fact, that's exactly what we're doing. Analogous to how we can use [polar coordinates](https://en.wikipedia.org/wiki/Polar_coordinate_system) \\((r, \theta)\\) to represent \\((x, \space y)\\) coordinates, we can use the distance a complex number is away from \\(0 \space (r)\\) and the angle it makes with the positive real axis \\((\theta)\\) to describe complex numbers instead of \\(a+bi\\).

The reason we would want to do this is to be able to more closely study this cyclic property that is inherent to the way we define the imaginary unit. The way this actually looks in practice, is through one of the most fundamental and beautiful formulas in all of mathematics. Discovered by [Leonhard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) and hence named after him, Euler's formula states that for any complex number with radius \\(1\\) and angle \\(\theta\\):

\\[e^{i\theta}=cos(\theta)+i \space sin(\theta)\\]

If you don't see the hidden circle in this formula yet, remember that \\(cos(\theta)\\) gives the x-coordinate on the unit circle at angle \\(theta\\), and \\(sin(\theta)\\) does the same for the y-coordinate. So here we have an expression that encodes this wild \\(e^{i\theta}\\) into \\(x+yi\\) like we saw before!

[![Euler's Formula]({{ site.imgurl }}/EulerFormula.png)](https://www.cuemath.com/eulers-formula/)

I really encourage the reader to sit on this for a bit and perhaps do a bit of research on this if they are interested. I mean it when I say that this is one of the most fundamental discoveries to all of modern mathematics, with countless applications since its inception. As a side effect of this formula, plugging in \\(\pi\\) gives us \\(e^{i\pi}=-1\\) and thus \\(e^{i\pi}+1=0\\) which has come to be known as Euler's Identity or, more commonly, *The Most Beautiful Equation in Mathematics*.

**Note:** I mentioned that the radius must be 1. This can easily be scaled by showing \\(re^{i\theta}=r(cos(\theta)+i \space sin(\theta))\\) as both real and imaginary axes are scaled proportionally. On many modern graphing calculators, if you go into the settings two of the available modes show "\\(a=bi\\)" and "\\(re^{i\theta}\\)" as ways to represent values!

And that's the second question I posed at the start of this post! Really well done if you've made it this far. Now it's time for the really good stuff. At this point we've built all the intuition we need to start solving some numeric problems in a very special way.