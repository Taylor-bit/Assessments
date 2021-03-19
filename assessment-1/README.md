# Assessment 1

## Rubric
Click [here](https://docs.google.com/spreadsheets/d/1zU9ZkwPn5aWxIuC7NJrxr7fBNvUwjQYFm6hZje-_cZE/edit#gid=0) to see what we are grading you on

## Rules / Process
* Fork repo to your personal Github and clone as usual but don't open a pull request until the time is up. Others will be able to see your answers.
* This test is fully open notes and open Google
* Work independently - don't consult with other students!
* 4 hour time limit

# Part 1: Optimal Change
You are writing a computer program for an electronic vending machine to give you the optimal change for an item's cost.

Create your own class in Python that takes in two arguments - a total price and a user's amount paid. This class will have a method `optimal_change` which will output a string with the optimal change. Here it is in action:

```
change_maker = ChangeMaker(62.13, 100)
change_maker.optimal_change()
> "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

change_maker2 = ChangeMaker(31.51, 50)
change_maker2.optimal_change()
> "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
```

### Remember
- Don't forget to account for plural denominations (i.e., quarters, dimes, pennies, bills) and punctuation (i.e., commas and the period at the end of a sentence) to delineate between different denominations.
- This is **optimal** change. Obviously, you can give the change in pennies, but we're looking for the most optimal (least amount of) change possible.
- Fully understand the data types of your input and output
- TDD everything! Write at least 3-4 unit tests. Feel free to start with the two examples above

# Part 2: Extra Questions
Answer the following questions in `answers.txt`:
1. What is the difference between a local variable and an instance variable? What does `self.ATTRIBUTE` give you the ability to do that `ATTRIBUTE` does not?
2. List and describe all the `git` commands you commonly use to create a pull request
3. Can you describe what recursion is? What does every recursive method need?
