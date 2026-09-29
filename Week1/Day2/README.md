**1. What you will build**
Write a Python program that asks the user to enter a mark (a number between 0 and 100) and then
prints the matching letter grade. The program runs in the terminal — there is no website or app
interface. You will set up a clean Python environment, write your code in a .py file, run it, and
confirm it produces the correct output. Use pure Python only — no frameworks or external
packages.

Grading scale to implement
Your program must convert a mark into a grade using exactly this scale:
Mark range Grade
90 – 100      A
80 – 89       B
70 – 79       C
60 – 69       D
Below 60      E
.

**Invalid Input Handling**

_Validating the input type and accepting only integers between 0 and 100
By using the try.. catch the exception and prompt the user to enter valid input 
Use strip() to trim spaces from the input if the user is giving a string value._



while True:

    mark_input = input("\nEnter your mark (between 0 and 100, or q to quit): ").strip()     #strip() removes any leading or trailing whitespace from the input

    if mark_input.lower() == "q":
        break

    try:
        mark = int(mark_input)
        if mark < 0 or mark > 100:
            raise ValueError("\nMark must be between 0 and 100")
    except ValueError as e:
        print(e)
        continue

**Result**

Enter your mark (between 0 and 100, or q to quit): 98

Mark : 98 -> Your grade is A

Enter your mark (between 0 and 100, or q to quit): 87

Mark : 87 -> Your grade is B

Enter your mark (between 0 and 100, or q to quit): 72

Mark : 72 -> Your grade is C

Enter your mark (between 0 and 100, or q to quit): 69

Mark : 69 -> Your grade is D

Enter your mark (between 0 and 100, or q to quit): 43

Mark : 43 -> Your grade is E

Enter your mark (between 0 and 100, or q to quit): SE 
invalid literal for int() with base 10: 'SE'

Enter your mark (between 0 and 100, or q to quit): 108

Mark must be between 0 and 100

Enter your mark (between 0 and 100, or q to quit): -1

Mark must be between 0 and 100

Enter your mark (between 0 and 100, or q to quit): 
