---
layout: post
title: 1111x1111=1234321
extenstion: Extension (not currently used)
publish-date: July 1, 2022
description: Palindromic Multiplication
---

1. [Multiplying by 11](#multiplying-by-11)
2. [Palindromes](#palindromes-from-111-1111)
3. [Number Systems](#number-systems)
4. [More Number Systems](#more-number-systems)

-----

### Multiplying by 11

I believe I was first taught my multiplication tables in the third grade. In my class we would sometimes play a highly competitive, one on one showdown multiplication game to test our knowledge in a fun way. Two kids would stand up, and the teacher would flip a flashcard with two numbers, both always between 1 and 12, and the first of the two to correctly shout the product of these numbers would move on to face the next kid. The highest of victories belonged to one who would be able to make their way through the entire room without being beaten, a dream achieved by only one person in the whole class - Mike Gerhart. I would usually beat a handful of kids in a row, but my mental math has never been remarkably strong and I would always end up taking a seat.

Once when we were playing this game I was having a particularly good day, and the conditions were perfect for me. The notorious mental math ace and now good friend of mine, Mike Gerhart, sat to my left after an stunning upset. I was now pitted against the one who slayed this beast. After defeating them I found myself moving around the classroom at marvelous pace, vanquishing each of my enemies one by one.

After I had conquered all but one of my adversaries, my victims now looked to me to become the second ever to make the rounds and claim my position in history as one to circle the whole room. My final battle of my campaign meant I had to face the only other to complete the task. Shaking in nervousness I stood up by Mr. Gerhart and awaited my two numbers that would either propel me into celebrity status or leave me in defeat.

I blinked my eyes at the most unopportune moment, and had a fraction less time than Mike to notice the numbers had been flipped:

\\[11 \times 7\\]

Before I had a chance to process this, the champ yelled out the answer to one of the easiest possible number pairs one could ask for, and my peers roared in anguish as I was forced to join them in defeat, never to achieve this massive goal of mine.

Everybody in that room knew their 11's multiples, at least up until \\(11 \times 11\\), because all it does is "double" whatever number it's multiplied with. \\(11 \times 11\\) is where it gets interesting. \\(11 \times 11\\) was easy to remember, because it was just "one two one." Simple, right?

Here we're going to explore the interesting pattern that arises when you dig a little deeper into this idea.

-----

### Palindromes from 111, 1111

Later in that same year, in that same classroom, I found myself doing what I'm sure all of us have done at some point - playing with my calculator. This wasn't some fancy calculator with lines and graphs and, ugh, *statistics*, this was a four function calculator with the small "solar panel" strip that you could cover with your thumb to make the digits disappear.

I was haphazardly inputting different operations when I came upon this pattern:

\\[111 \times 111 = 12321\\]
\\[1111 \times 1111 = 1234321\\]

I didn't know what a palindrome was at the time, but I did notice that these products seemed to be counting from 1, up to a number and then back down to 1 on the other side.

I kept going with this until I realized this pattern broke once I inputted a string of 10 1's in a row. The calculator I was using probably showed this in scientific notation (which I didn't know what it meant for a long time, my brother and I legitimately used to say "\\(1e-2\\)" as "one, Eistein's Theories, negative two"), but I was still able to notice the pattern didn't follow the "12345..." and back down idea.

Let's take a closer look at what we're doing when we multiply these string of ones together. For now we'll be working in our usual base 10 decimal system, but we'll expand this later.

Let's start out with just \\(111 \times 111\\). I venture to say that none of us can just straight multiply these in our heads, but we can break these numbers down in the following way:

\\[111 \times 111 = (100 + 10 + 1) \times 111\\]

\\[= 11100 + 1110 + 111 = 12321\\]

This last step can be shown vertically like this:

![111x111]({{site.imgposturl}}/PalindromicMultiplication/111x111.png)

Notice how, when we multiplied a string of three 1's by itself we got an addition of three values, each with three ones, offset by 0, 1, and 2 zeroes.

Let's move a step up now:

\\[1111 \times 1111 = (1000 + 100 + 10 + 1) \times 1111\\]

\\[= 1111000 + 111100 + 11110 + 1111 = 1234321\\]

Which can be seen as:

![1111x1111]({{site.imgposturl}}/PalindromicMultiplication/1111x1111.png)

Here we have a string of *four* 1's multiplied by itself to get an addition of *four* values, each with *four* ones, offset by 0, 1, 2, and 3 zeroes.

-----

### Number Systems

Now we have a better idea of what's going on here when we perform these calculations, so let's try and generalize this fact that we found above.

We can say based on this pattern, that if we have a string of \\(n\\) 1's in a row multiplied by itself, we will get an addition of \\(n\\) values, each with \\(n\\) ones, offset by 0, 1, 2, ..., \\(n-1\\) zeroes. This will result in a value that looks like the following:

\\[1 \space 2 \space 3 \space ... \space  n-1 \quad n \quad n-1  \space ... \space 1\\]

But consider the case that originally stumped me:

\\[1111111111 \times 1111111111\\]

![Ten ones]({{site.imgposturl}}/PalindromicMultiplication/10ones.png)

This doesn't follow our formula, because from the left we see "...5679..." and it seems to skip over the 8. So where does our formula fall apart?

*It doesn't!*

Our formula actually works perfectly fine, but we need to impose one more condition: that we need to be operating on numbers in a number system with base *greater than* \\(n\\).

If you're not familiar with how number systems work, check out this good article [here](https://betterexplained.com/articles/numbers-and-bases/)

Take another look at the image above. If we instead counted the amount of ones in each column of our answer we would get something like this, where "\|" here is being used to denote the different place values of our answer:

1111111111 x 1111111111 =

\|1\|2\|3\|4\|5\|6\|7\|8\|9\|10\|9\|8\|7\|6\|5\|4\|3\|2\|1\|

This follows our generalized formula as we expect, and here we start to see why this formula fails to work for this value when viewed in a base 10 number system, because when we sum up 10 ones as we did in that middle column, we are all taught to "carry the 1" to the next place value. If we do this with the boxes we've created above we'd see we get the same "...5679..." number that we arrived at before.

To avoid this carrying over, we just need to view this number in a different number system\*. Using a number system with base greater than \\(n\\) ensures that when we reach the \\(n\\) in the very middle of our pattern, we have a symbol to represent it and therefore do not have to "carry the 1" to the next place value.

\*Yes, I know this changes the actual value of the number in question. The point of doing this is for the purpose of extending our pattern we found and explaining why we might assume it fails to works once you reach a certain point. If you're asked to evaluate 1111111111x1111111111 in base 10 in your daily  life, you're out of luck in using this technique.

-----

### More Number Systems!

What this means is that this fun pattern will arise in any number system! We also can predict exactly when this pattern will "break down" in that number system. We know that, since we need to use a number system with base greater than \\(n\\) for this pattern to hold, it will break down once we try to multiply a number with \\(n\\) ones by itself in that number system.

So in base 4, this will break down when we try 1111x1111. From here we will use subscripts of numbers (in decimal of course) to denote which number system we are using:

\\[11\_{4} \times 11\_{4} = 121\_{4}\\]

\\[111\_{4} \times 111\_{4} = 12321\_{4}\\]

\\[1111\_{4} \times 1111\_{4} = \|1\|2\|3\|4\|3\|2\|1\|\_{4} = 1300321\_{4}\\]

These expressions are equivalent to the following in decimal (the base 10 number system we all just love so much for some reason):

\\[5\_{10} \times 5\_{10} = 25\_{10}\\]

\\[21\_{10} \times 21\_{10} = 441\_{10}\\]

\\[85\_{10} \times 85\_{10} = 7225\_{10}\\]

This fact that we can predict how the pattern will behave in a certain number system is fun, but I think the coolest takeaway from this idea that this pattern holds in any number system that is greater than \\(n\\)! For example, \\(1111\_{8} \times 1111\_{8} = 1234321\_{8}\\) in the same way that \\(1111\_{9} \times 1111\_{9} = 1234321\_{9}\\), \\(1111\_{10} \times 1111\_{10} = 1234321\_{10}\\), and \\(1111\_{j} \times 1111\_{j} = 1234321\_{j} \space ; \quad \forall j \gt n\\)!

Here's that example:

\\[1111\_{8} \times 1111\_{8} = 1234321\_{8}\\]

\\[1111\_{9} \times 1111\_{9} = 1234321\_{9}\\]

\\[1111\_{10} \times 1111\_{10} = 1234321\_{10}\\]

Which correspond to:

\\[585\_{10} \times 585\_{10} = 342225\_{10}\\]

\\[820\_{10} \times 820\_{10} = 672400\_{10}\\]

\\[1111\_{10} \times 1111\_{10} = 1234321\_{10}\\]

These are three completely different expressions, yet can be shown by the same pattern in their different number systems. Isn't that cool?

I'm sure there's more to be explored with this, but this is all that my mind takes me to with this. Let me know what more there is the be discovered!

-----

[\[Top\]](PalindromicMultiplication)