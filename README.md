# Luhn Algorithm Credit Card Checker
A Python port of a classic algorithm.
## What is the point?
- Nowadays, online vendors have to pay everytime they run a credit card through 
their backend payment service such as PayPal.
- To prevent trolls and malicious users from sending random numbers into the sites
checkout and wasting the companies money, companies usually use an algorithm 
such as the Luhn Algorithm to check a credit card before they run it with their provider.
- The algorithm will never say a valid credit card is invalid, although there are ways to 
trick the algorithm  such as using a number like **12345674**.

## How does the algorithm work?

The algorithm works by weighting each number in the series of numbers with 2's and 1's.
Once that is done, you find the product of every pair.
If the sum of all products is equal to a number that ends in a 0 (Ex. 30), then the number is valid.
**Example with 12345674, the number that tricks the algorithm.**

| Number | Weight | Product |
| ------ | ------ | ------ |
| 1 | 2 | 2
| 2 | 1 | 2
| 3|  2 | 6
| 4 | 1 | 4
| 5 | 2 | 1
| 6|  1 | 6
| 7 | 2 | 5
| 4 | 1 | 4
|End | None | Sum: 3**0**



## License
[MIT](https://github.com/CadeCodes/Luhn/blob/main/LICENSE)
