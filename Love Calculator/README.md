# Love Calculator

Write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

`"Your score is *x*, you go together like coke and mentos."`
For Love Scores between 40 and 50, the message should be:

`"Your score is *y*, you are alright together."`
Otherwise, the message will just be their score. e.g.:
```
"Your score is *z*."
```
```
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."
```


### Example Input 1
```
Kanye West
Kim Kardashian
```
### Example Output 1
```
The Love Calculator is calculating your score...
Your score is 42, you are alright together.
```
### Example Input 2
```
Brad Pitt
Jennifer Aniston
```
### Example Output 2
```
The Love Calculator is calculating your score...
Your score is 73.
```
