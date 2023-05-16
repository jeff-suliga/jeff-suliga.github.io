---
layout: post
title: Math Origins
publish-date: In Progress
description: Is Math Invented or Discovered?
---

<blockquote>
    <p style="color: #9B008A; font-size: 1.2em;">
        "I feel like all the time, people want math to do more than it really can. Y'know like one of the biggest misconceptions is that math tells you, like, truths. But it doesn't - it tells you, given certain assumptions what are the necessary links to consequences ... you want math to be able to be this self-contained thing that can do everything, but it's no different from the other fields out there. As much as it wants to be on its own pedestal, it's got its own foibles that we all just have to deal with. Every other science certainly knows this well, why do the mathematicians think that they would get to play a different game entirely?"
    </p>
    <footer align="right">
        Grant Sanderson, 3blue1brown on <a href="https://www.youtube.com/watch?v=pJyKM-7IgAU?t=913">Bertrand's Paradox</a>
    </footer>
</blockquote>

It was my junior year of high school when I was first faced with this question, and at this point my formal math education extended through integral calculus. I was hanging out with my math teacher in the time before first period started one day, when Mr. Martin asked me something along the lines of this question:

<p style="text-align:center;font-size:150%;"><em>"You ever feel like we might discover something that breaks math?"</em></p>

I remember at the time quickly responding, defending the concreteness of math's origins. I said "it works way too well" and we therefore could not make any discoveries that contradict what we've already found out about the world. 17 year old me would have said without hesitation that math is entirely discovered as opposed to invented - for how could a science that is so descriptive of our natural world, so useful and present in just about all areas of life, and "works so well" be one that is foundationally manufactured by human thought?

As I have advanced in my formal math education and self study I have grown to see the naivety in this stance. I look back on recent years in school as my math study has become more abstract and fundamental and notice just how many areas of even basic middle/high school mathematics have been shaped by a fabricated structure designed to fit our discoveries into a defined set of rules to play by. If Mr. Martin were to ask me this question again now, I would say absolutely! Without a doubt there will absolutely be some new discovery or way of thought that challenges the current state of mathematical thinking. In fact, it has happened many times!

In this post I will introduce this commonly-asked question and speak to why I now lean more towards saying that math is invented, rather than discovered.

A basis for my response in grade school was due to the fact that I could look around and see math around me in the physical world. At the most fundamental level of counting how many watermelons Johnny bought from the store, math is present. In studying the algebraic relationship between instantaneous rates of change and continuous accumulation (differentiation vs. integration), math's seeming completeness is found. All around us, math can be used to identify, describe, and predict attributes of the physical world. **Because that's what it's designed to do.**

Math is designed to describe the physical world, and when it doesn't, we make more rules for it to do so. When we find a problem that is unsolvable using the current state of mathematical thinking, we extend the base from which all math is contained. This would be an example of math-breaking discovery. Examples of this throughout history could be: negative numbers, non-integral exponents, infinity, complex numbers, analytic continuation, the gamma function and fractional calculus, quaternion math, the hyperreal system.

-----

### Mathematical Structure

To really see what I mean by "extending the base from which math is contained" we should talk about how modern mathematics is structured. We define a set of beliefs called **axioms** that we take to be fundamentally true. Something like, for any number \\(x\\), \\(x = x\\). This seems harmless but statements like these form the entire structure of mathematics, from simple equations to real analysis. We don't however want to just be working with axioms. This would mean trying to solve a simple quadratic expression would take on the order of days, if not longer. This is where **theorems** come into play. If we think of a new idea that could be used to solve a problem, we call this a **conjecture** and, once proven to be true, it becomes a **theorem**.

*Side Note*: If you're uncomfortable with what an axiom is, take your favorite math homework problem you've done. Find any step that you took in this problem, and ask yourself why you were able to perform this step. Keep asking yourself this until you reach a point where you get to something that you find fundamentally true. This could be an axiom (but, more often than not, you can go deeper).

A conjecture could be something along the lines of "multiplying two odd numbers yields an odd number," which we can easily prove using our agreed upon definition of an odd number. For the curious, we say an integer \\(x\\) is odd provided there exists an integer \\(k\\) such that \\(x=2k+1\\). Or:

\\[(\forall x \in \mathbb{Z}) \big[ D(x) \iff ( \exists k \in \mathbb{Z} ) x = 2k + 1 \big]\\]

Since we can prove this statement about multiplying odd numbers, we can call this a **theorem** and use it to prove other things instead of working through this argument again. This is how mathematics is built, from the ground of axioms upwards with a huge interconnected web of theorems. We start with axioms and when we think of a new problem, we use our already built up theorems to try to reach up and grab this conjecture, and if proven true, this conjecture becomes a theorem itself which can in turn be used to tether in new conjectures, otherwise if it is shown to be false we know not to use it to try to confirm other conjectures. This is the essence of what Mr. Sanderson is saying with "\[Math\] tells you, given certain assumptions what are the necessary links to consequences..."

This structure is all well and good, but what happens when we come across an idea that just doesn't fit within the same bounds that are defined by the current axiomatic state of mathematics? This math-breaking idea can neither be proven true nor proven false, and possibly cannot even be properly expressed using the current state of mathematical representation. What then?

Well, historically we've elected to ignore this idea. Probably the biggest examples of this are the concepts of infinity and imaginary numbers, both of which I've already mentioned. The idea of infinity was well established and pondered before this point, but when the idea of certain infinities being larger than others (countable vs. uncountable) was first brought to light, it was disregarded and the one who first thought about it was ridiculed and their ideas disregarded with them. Similarly with imaginary numbers, when we came across the possibility of \\(\sqrt{-1}\\) from a very meaningful source, we again disregarded it. It wasn't until later for each of these cases when we expanded our bounds to include these ideas, further expanding this large web of possibilities in mathematics.

It's important to see what we just did here. These concepts fell outside the boundaries of the state of thought at the time, so we made a bigger system to contain them, and since then many very applicable discoveries have stemmed from the inclusion of this new extension. I believe this result is one of the big reasons why people might say math is discovered - they could point to complex roots of unity solving real world problems dealing with generalizing certain periodicities, but this wouldn't have been possible without the inclusion of complex numbers into our realm of thinking, and more importantly arise as a *direct consequence* of how we've decided to include this idea into our mathematical structure. Complex numbers would be just as useful but would act "backwards" if we had said \\(\sqrt{-1} = -i\\) instead of \\(\sqrt{-1} = i\\).

-----

### Mathematical Completeness

Ok so here we stand. We know that, if we ever do reach a result that doesn't sit well with the current state of mathematics, we can add some axioms or add some rules so that it ends up sitting nicely into our calculations. But, the key question here is, do we know this will ever happen? In other words, will we ever reach a point where math is *complete*? When we've found all of the outlier problems, like imaginary numbers, where no more extensions of our axioms is ever needed?

This may seem like a question we have no answer to, where we can go back-and-forth in discussion about, but we do actually have an answer to this question:

<p style="text-align:center;font-size:150%;"><strong>No.</strong></p>

This is likely surprising. In fact, I venture to say that if I were to ask many undergraduate math students such as myself, many would conjecture "yes" (and they would be in accordance with a handful of math's greatest thinkers from the time the question was coming to light).

Before we go into why, let's iron out a very key detail in the way our logical reasoning works. Statements in a logical system, if solvable, must either be true or false. We don't allow for any gray area for statements to be *kinda* true, *almost* true, *partially* true. This also means that if we have a statement \\(k\\) in our current mathematical structure and show it is true by taking one "route" from our axioms to \\(k\\) by using theorems, there is no "route" from a different subset of axioms thorugh different theorems that can disprove \\(k\\). This is why we discover things like "the contrapositive of a statement has the same truth value as the original statement," or the use of "proof by contradiction." We couldn't use these things without the precondition that a statement and it's negation must always have binary and opposite truth values. This is called **consistency**. We can say our mathematical structure is **consistent** because a statement is either true or false based on its axioms, and therefore lacks axiomatic contradiction.

You'll notice I snuck in the phrase *if solvable*. This is to account for the case where we find a problem that, not because it is too hard or too complex, but by very nature of the problem and the logical system it is defined in, simply *cannot* be solved. In this case we, in the state of the logical system in which we are working in, would have no way of assigning a value of true or false to expressions containing statements such as these. Again, think of complex numbers when they were first encountered - this is just another way of saying that we've come across a thought that challenges the basis of our logical system.

Ok now we can revisit that question above. Acclaimed as one of the most important intellectual advances in modern mathemematics and logic, there is a theorem called *Gödel's Incompleteness Theroem*, proved by Kurt Gödel in 1931 (when he was 25!) that states, in accordance with the best of my understanding:

<p style="text-align:center;font-size:150%;">Any consistent formal system <em>F</em> within which a certain amount of elementary arithmetic can be carried out is incomplete.</p>

This is a massive claim - let's first break down some of the terminology. First, we see this *consistency* thing come back, and we already know what that means - no axiomatic contradictions exist in the system. Also, when it says "formal system," that means the same as saying "axiomatic system." So here we're working with a system based on a set of axioms from which theorems can be logically extended such that no condradictions exist in the axioms.

Now for this **incomplete** term, this is the big one. A system *F* is defined as **incomplete** iff the system contains statements that can be written in the language of the *F* that are unsolvable.

This theorem can be applied to our current state of mathematics to say that, no matter how many times we add axioms and change our formulas to account for problems such as complex numbers, there will **always** be problems that can be expressed using that new mathematical basis, that quite literally *cannot* be solved using that same math.

-----

### Consequences of Incompleteness

Ok so we just took a deep dive into a ton of really fundamental math ideas, which should bring up the question: what's the point, Jeff?

Personally, when I look at our key question of whether math was discovered or invented through the lens of our math being perpetually incomplete, it's enough for me to feel comfortable thinking we've invented math.

Don't get me wrong, there's a ton of beauty in the way we've constructed mathematics (I mean, I do study the thing like towards a degree) and I do believe there's an element of discovery that is found after we define things the way that we have (for example, discovering the quadratic, cubic, and quartic equations, and discovering that no generic quintic equation exists). However, the fact that this discovery is entirely contained within our choices for axioms, and that it is guaranteed to always lead to more things that will demand more axioms in order to be solvable, leads me to comfortably say without hesitation that math was invented rather than discovered.

Now, I also don't think this stance has to feel like I'm slandering math or anything like that, my high school self would probably feel deflated to hear me say that math is not discovered, but in reality I believe that this idea has brought an opening of my eyes of sorts - where I'm now free of misconceptions about math as this "self-contained, truth-bearing" entity as Grant pushes back against, and am now free to explore the realm of math from a more objective view. Things in my classes are the way they are because people much smarter than me have defined it to be that way, and these decisions now open doors for me to explore problems I otherwise wouldn't see, like [This One]({{site.posturl}}/PalindromicMultiplication/PalindromicMultiplication), and also give me freedom to come up with my own rules and find problems within those!

Another unfortunate result that arises from Gödel's theorems is that, sometimes we don't quite know if we're working on one of those problems that just can't be solved. There are well-known, long-standing problems out there (\\(P = NP\\), Collatz conjecture, Riemann hypothesis) that many great mathematicians have put great effort into and produced great results, but still haven't solved the problem at hand. My first time doing math research was with my first modern algebra professor working on a number theory/real analysis question related to Mahler measure. In truth I still can't fully explain my work with that project. But one of the first things he told me when I was in his office with him was that he had been working on that project for the majority of his upper-maths career, and was showing me related results of other mathematicians working on the problem for hundreds of years, and that we could have been working towards an unsolvable problem and just not know it.

I guess that's also a subtle beauty. Even given an unsolvable problem, I've seen firsthand just how often wild and seemingly unrelated ideas and results can come from attempting to solve a different problem. You never truly know what you're going to stumble upon in math research.

-----

### Extra Content

Maybe this wasn't the type of discussion you expected to have when approaching this question, and so I wanted to also provide some intereseting results I've noticed from the "dark side" of math - practical things, not fundamental math philosophy, that might also make people think math is invented.

[The Dark Side of Mathematics...](TheDarkSideOfMath)

-----

[\[Top\]](#)
