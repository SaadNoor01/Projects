# Treasure Map

A program that will mark a spot on a map with an X.

```

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
```

<img width="391" alt="image" src="https://github.com/SaadNoor01/Projects/assets/174381924/385c0780-7e2b-4739-829b-c15656196c05">

Write a program that allows you to mark a square on the map using a letter-number system.

<img width="376" alt="image" src="https://github.com/SaadNoor01/Projects/assets/174381924/142ea7dc-ed32-4474-9bb1-482de3d9d2e2">

So an input of A3 should place an X at the position shown below:

First, the program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "X". Remember that your nested list map actually looks like this:

```
[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
```
## Example Input 1
```
B3
```
## Example Output 1
```
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
```

## Example Input 2
```
B1
```
## Example Output 2
```
Hiding your treasure! X marks the spot.
['⬜️', 'X', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️️', '⬜️️']
```

