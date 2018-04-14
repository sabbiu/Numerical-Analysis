KAHAN ALGORITHM
--
https://en.wikipedia.org/wiki/Kahan_summation_algorithm

Relies on the fact that,
(((a + b) - a) - b) != 0

We must store compensation value and
add it back at every summation

Explanation: When we add much larger number with smaller number
then, we loose the precision of lower digits in smaller number.
Thus, on every new sum, we add previous lost compensation.

### Obtained Output from this program
\#1

    Kahan Sum: 384615380769230.75000
    Naive Sum: 384615380769261.62500
    ________________________^^^^^^__
    more is added in naive summation
 
\#2

    Kahan Sum: 384615380769230.75000
    Naive Sum: 384615380769130.75000
    _______________________^________
    less is added in naive summation
 
\#3

    Kahan Sum: 384615380769230.75000   
    Naive Sum: 384615380769108.00000
    _______________________^^^^^^___
    less is added in naive summation

We can notice that **Kahan Sum** gives same result every time but, **Naive Sum** gives different result every time.
It is because permuting the position of values every time will force Naive Sum to loose different digit's precision every time. But, As Kahan Algorithm compensate, it doesn't need to care about when, what number appears.
 