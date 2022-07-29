---
layout: post
title: Suliga Formulae
publish-date: In Progress
---

This post will showcase two different formulas that I came up with in my latter years of high school.

\\[\int\_{-\infty}^{\infty}e^{ax^{2}+bx+c} \space dx = \\]

\\[\lim\_{n \to \infty} e^{c - \frac{b^{2}}{4a}}\sqrt{\frac{\pi}{a}(e^{an} - 1)}\\]

[The first](#suliga-formula-1), coined by my friends as *The Suliga Theorem* (which doesn't even make sense), is a generalization of a discovery first popularized by and named after one of history's smartest minds, Carl Friedrich Gauss.

\\[\int\_{a}^{b} f(x) \space dx = \\]

\\[b \times f(b) - a \times f(a) + \int\_{f(b)}^{f(a)} f^{-1}(x) \space dx\\]

[The second](#suliga-formula-2) came from an unawareness of previously-derived (and much simpler) ways to integrate inverse trig functions. I didn't know these existed so I came up with my own way to integrate a function in terms of its inverse.

-----

### Suliga Formula 1

\\[\int\_{-\infty}^{\infty}e^{ax^{2}+bx+c} \space dx = \\]

\\[\lim\_{n \to \infty} e^{c - \frac{b^{2}}{4a}}\sqrt{\frac{\pi}{a}(e^{an} - 1)}\\]

Sometimes when people see this daunting mess of symbols, I get asked

<p style="text-align:center;"><em>"So how does it work?"</em> or <em>"What does it do?"</em></p>

These are valid questions given the very uninviting manner of the formula - there's literally not any numbers anywhere. This can be be hard for many people to wrap their minds around what this means, but it's actually very simple (given an exposure to integral calculus).

All this shows is that, if you're going about your life and suddenly need to find \\(\int\_{-\infty}^{\infty}e^{-3x^{2}+7x-1} \space dx \\), you're in luck! By plugging \\(-3, 7,\\) and \\(-1\\) in for \\(a, b,\\) and \\(c\\) respectively, you'd know that the answer is exactly \\(e^{\frac{61}{12}}\sqrt{\frac{\pi}{3}}\\)! This is about \\(165.07\\).

This example paints a pretty accurate picture of how "useful" this formula is - basically zero. I've never had to use this for anything and I don't expect to, however building up from a pretty useful example of this expression might shed some light on how it's been used in the past heavily in forming modern statistics.

At this point, you probably think this is a meaningless idea to explore. However, one might notice that, when we plug in \\(a = -1\\), \\(b = 0\\), and \\(c = 0\\) to this formula, we can see that

\\[\int\_{-\infty}^{\infty}e^{-x^{2}} \space dx = \sqrt{\pi}\\]

Whether you care at all about the initial formula or not, there's no denying that this is pretty dang cool. We're taking this weird infinite integral (whose integrand has no elementary antiderivative!) and getting \\(\sqrt{\pi}\\) out of it! We know that anywhere \\(\pi\\) shows it's face, there's a hidden circle to be found. In this instance, the circle is *very* hidden, but with a bit of thinking outside of the disc we can find it.

In fact, this example is where this discovery all began with Gauss in 1809. While understanding of ideas from [This Video](TODO) is not necessary just yet and will be explained in the extension below, it explains this particular example very well and will provide the best base for the information to come. This example has been titled as the *Gaussian Integral*.

*Side Note:* This video has a beautiful way of showing why we add "\\(\space rdrd\theta \space \\)" when converting from a cartesian integral to an integral in polar form. Even if you're familiar with the Gaussian integral or multivariable calculus, I *highly* recommend watching at least that part of the video. It builds a much stronger visual intuition for this than I ever got in my classes when dealing with change-of-variable integration.

\\[\int\_{-\infty}^{\infty}e^{ax^{2}+bx+c} \space dx\\]

Ok, so let's start from the top and break this nasty integral down one piece at a time. We first notice that this integrand has *no elementary antiderivative*. What this means is that, using our normal operations \\( + - \times \div \\), exponentiation, trigonometric/hyperbolic function expression, and their inverses, we **cannot** construct the antiderivative.

For example, to evaluate \\(\int\_{a}^{b} 4x^{2} \space dx \\), our first step is to find an antiderivative of \\(4x^{2}\\) - a function whose derivative is \\(4x^{2}\\). Using what many learn as the *power rule*, we know that this function is \\(\frac{4}{3}x^{3}\\), which I encourage you to check. The key point here is that, since we were able to come up with an explicity-defined antiderivative of \\(4x^{2}\\) using our normal notations, we can see that this function has an *elementary derivative*.

So going back to our problem, we're stuck wondering where to go. We know that this integrand's antiderivative is nonelementary because of this "\\(x^{2}\\)" term in the nasty exponent without any \\(x\\) term in the integrand. However, we were able to pull a trick (explained in the video) to convert this into a polar form and evaluate from there, but that only worked because we were integrating \\(e\\) raised to something squared.

This means that our first main step for evaluating this integral is to try to turn it into this form. We want to do some manipulations so that we have

\\[\int\_{-\infty}^{\infty} e^{f(x)^{2}} \space dx\\]

Well, the first conflict to this idea is that we have this "\\(+c\\)" in our exponent. However, with some tricky algebra we can quickly remove this from the integral:

\\[\int\_{-\infty}^{\infty} e^{ax^{2}+bx+c} \space dx = \\]
\\[\int\_{-\infty}^{\infty} e^{ax^{2}+bx} \space e^{c} \space dx = \\]
\\[e^{c} \int\_{-\infty}^{\infty} e^{ax^{2}+bx} \space dx\\]

Here we just used the fact that \\(e^{c}\\) is simply a constant, independent of \\(x\\), and so we can pull it ouside of the main integral.

At this point we can now use one of my favorite pieces of math to get this new integrand into the form that we want, [Completing the Square]("{{site.posturl}}/FactoringVisually/FactoringVisually").

\\[e^{c} \int\_{-\infty}^{\infty} e^{ax^{2}+bx} \space dx =\\]
\\[e^{c} \int\_{-\infty}^{\infty} e^{a(x^{2}+\frac{b}{a}x)} \space dx =\\]
\\[e^{c} \int\_{-\infty}^{\infty} e^{a(x^{2}+\frac{b}{a}x+\frac{b^{2}}{4a^{2}}-\frac{b^{2}}{4a^{2}})} \space dx =\\]
\\[e^{c} \int\_{-\infty}^{\infty} e^{a((x+\frac{b}{2a})^{2}-\frac{b^{2}}{4a^{2}})} \space dx =\\]
\\[e^{c} \int\_{-\infty}^{\infty} e^{a(x+\frac{b}{2a})^{2}-\frac{b^{2}}{4a}} \space dx =\\]
\\[e^{c} \int\_{-\infty}^{\infty} e^{a(x+\frac{b}{2a})^{2}} \space e^{-\frac{b^{2}}{4a}} \space dx =\\]
\\[e^{c} \space e^{-\frac{b^{2}}{4a}} \int\_{-\infty}^{\infty} e^{a(x+\frac{b}{2a})^{2}} \space dx =\\]
\\[e^{c-\frac{b^{2}}{4a}} \int\_{-\infty}^{\infty} e^{a(x+\frac{b}{2a})^{2}} \space dx =\\]

And look at that! We've reached a spot where we have the integral of \\(e\\) raised to something squared just like we wanted!

Now that was a lot that just happened, so lets first break down the steps we just took before we move on.

-----

### Suliga Formula 2

-----

[\[Top\]](SuligaFormulae)
