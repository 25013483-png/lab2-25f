# Lab 2 - Variables, Expression, and Statements

## Setup

1. Click the "**Use this template**" button near the top of this repository on GitHub
2. Set the following properties on the GitHub repository, then click "Create repository":
    - **Owner**: your GitHub username (NOT the course organization)
    - **Name**: csd110-26f-lab-2
    - **Visibility**: Private
3. In your new repository, go to Settings -> Collaborators, and add your instructor as a collaborator.
4. Create a branch named `lab-2` on which to do your lab work
5. Create a Codespace on that branch, and open it (give it a few minutes to initialize)
6. In your Codespace terminal, verify your setup using `gh lab setup-check`

### Required Reading 

It is assumed that you have attended all lectures and completed readings and practice exercises up to the end of Chapter 2 in the course textbook.  If you have not done so yet, you should!

### Reflections

As you are working on your lab, help yourself remember important things by taking notes in `reflections.md`. Record notes about anything you think important to remember, any problems you encountered and how you resolved them, and any remaining questions you may still have.

> **NOTE**: `reflections.md` is a 'markdown' file.  Markdown is a markup language that has simple syntax for adding formatting to plain text documents. See [this documentation on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to learn how to format text in a markdown file.

### AI Use

> **IMPORTANT**: ***Failure to include an accurate AI Use Statement as described below may result in a lab grade deduction of up to 100% depending on your instructor's evaluation of how well you understand the code you submit***

You MAY use AI as a LEARNING AID to help you understand topics you are needing extra help with.
You may NOT use AI to do your work for you or to avoid having to think and learn on your own.

#### AI Use Statement

**Whether or not you use AI**, you MUST include an AI Use Statement in your `reflections.md` document that indicates clearly:

- Which specific AI tools you used in the completion of this lab (or an explicit statement that you did not use any AI tools).
- Links to or copies of **ALL** AI chats you had related to this assignment. 

> **IMPORTANT:** if sharing a link, do NOT simply copy the URL from your browser; you MUST click the **Share** button and create a public link.

Examples:
- I used ChatGPT to help me better understand the lab requirements.  Below are links to my ChatGPT chats.
- I used Claude to give me examples of statements vs expressions in Python.  Below are links to my conversation.
- I did not use any AI tools to complete this lab.

### Running your code

You can run your code in one of two ways:

#### Running code from the terminal

1. Open the terminal (View -> Terminal)
2. Enter a command like the following `python path/to/script.py`.  For example, to run the `q1.py` script in the `src` folder, run `python src/q1.py`.

#### Running code using the debugger

1. Open the Python file you want to run
2. Open the 'Run and Debug' panel (right side, right-arrow icon with bug in lower left corner). 
3. Make sure the "Python Debugger: Current File" configuration is selected in the dropdown at the top of the panel.
4. Click the green arrow button to run the currently opened Python file

### Testing your code

A set of tests have been prepared for this lab that will help you determine if your code is correct or not.

#### Running tests 

| Task | Command | Example |
|------|---------|---------|
| Run all tests | `pytest` | `pytest` |
| Stop at the first failing test while working | `pytest -x` | `pytest -x` |
| Run one test file | `pytest <path_to_file>` | `pytest test/test_q1.py` |
| Run one test function | `pytest <path_to_file>::<function_name>` | `pytest test/test_q1.py::test_that_n_is_42` | 

While working, use `pytest -x` to focus on one failure at a time. Fix that issue and run the same command again to continue through the tests. Once the tests are passing this way, run `pytest` to check the entire lab.

#### Reading test output

The output of the tests will give you an indication of which tests passed or failed. For any failed tests, you will also see messages that should help you determine why the test failed.

Here are some tips for dealing with failing tests:

1. The name of the test itself usually gives a clue as to what the test is checking.
2. The sentence after the "AssertionError" message usually indicates what the expected value was and what the actual value was.
3. Compare the "Expected" and "Actual" values to see how they differ.  This will often give you a clue as to what is wrong with your code, which is generating the "Actual" value.
4. Often fixing one test fixes other failing tests as well—tackle one problem at a time.
5. When working on a failing test, run just that test (see above) so you can focus on its output without having to wade through the output of all the other tests.

#### Passing tests does not guarantee correctness

If all the tests passed, you can be reasonably sure that your code is correct, **BUT PASSING ALL TESTS DOES NOT NECESSARILY MEAN YOU WILL GET 100%** because some grades are assigned to non-coding tasks, and it is sometimes possible to create incorrect programs that do pass the tests.

## Instructions

### Overview 

In this lab you will use values, operators, variables, expressions, and statements to complete some simple programs. 

### Part 1 - Assignment statements and types

In the file `q1.py`...

1. Assign the value 42 (an integer) to a variable with the name `n`
1. Assign twice the value of the number π (the approximate value 3.14159 for π will do) to a variable named `tau` and the `*` operator
3. Assign the value 'Sault College' (a string) to a variable named `school`

Now, in the terminal, start a Python REPL session (just run the command `python`; to exit the REPL session, type `Ctrl+d`)

1. Do each of the above assignments again
2. Use the `type(..)` function to determine the type of each of the three variables
3. Experiment with re-assigning the variables to new values. Can you assign text to a variable that started as a number, or vice versa? What is the type of the variable after this reassignment?
4. Experiment with some of the operators you have learned. Use both variables and literals. Try the operators on both numbers and strings. Does Python know the order of operations? What happens if you try to `+` a number with a string?
5. Once you have completed the above steps, select the text in your REPL session and copy it (`Ctrl+c`)
6. Paste your session text into the `q1_repl_session.txt` file.


### Part 2 - Syntax errors

In `q2.py` four lines of Python code are given, but each one has a syntax error.  

1. Correct all four of these errors so that the program runs without error.
2. After each line, add a comment describing which syntax rule was being broken by that line
 
   > **NOTE**: You may fix the errors in any reasonable way you choose, but the code must ultimately assign the values that have already been specified to four different variables.  You may NOT simply remove/comment all the lines of code or change the values assigned. 

### Part 3 - Print statements and string operators

In `q3.py`...

1. Add a `print` statement that produces the following text: Feeling...HotHotHot! 

    > **IMPORTANT**: You are only allowed to use the string `Hot` in your code **ONE TIME**.  Simply writing `print("Feeling...HotHotHot!")` is NOT acceptable for this question. (HINT: Use the string operators we discuss in class.)

### Part 4 - Debugging

In `q4.py` you have been given a Python program that is supposed to calculate the volume of a square-based pyramid and print an appropriate message.  Unfortunately, the code is full of errors of all kinds: syntax, runtime and semantic! 
 
1. Try running the program, and use the error messages and debugging tools to help you identify the errors and fix the bugs.
2. For each change you make, add a comment describing the kind of error (syntax, run-time, semantic)
 
    > **NOTE:** The volume of a square-base pyramid is $\frac{1}{3}b^2 h$, where $b$ is the length of one side of the base and $h$ is the height.  A pyramid of base 3,000cm and height 1,000cm should have a volume of 3,000,000,000 cm^3 
3. Once you have fixed all the syntax errors and are able to run the script, set a debugging breakpoint on line 2. (Click in the gutter area to the left of the line numbers in the editor. A dot should appear, indicating that a breakpoint has been set.)
4. Run your program with the debugger (see the [Running your code](#running-code-using-the-debugger) section above) and observe that the program does not run to completion, but pauses at your breakpoint.
5. **OBSERVE**: You can hover over variables with your pointer to inspect variable values. The "Variables" section of the debug panel also shows you the values of all variables currently in scope.
6. Hover over the "Watch" section and click the + icon that appears.
7. Enter the expression `base*height` in the field that appears.
8. Use the debugger controls to "Step Over" one line at a time to line 4.
9. **OBSERVE**: Variable values are updated in the "Variables" section as you step through the code. Expressions entered in the "Watch" section are also evaluated and updated as you step through the code.
10. Take a screenshot that shows:
    1.  Your program with a breakpoint on line 2 and paused on line 4
    2.  The Variables panel
    3.  The Watch panel with your `base*height` expressions
11. Upload the screenshot to your codespace files.

## Reflections

Did you take notes in `reflections.md` as you worked? (See the [Reflections](#reflections) instructions above.) You should!

Did you document your AI usage adequately? (See the [AI Use](#ai-use) instructions above.) You must!
 
## Submission

1. **Test** your code to verify that it is working as expected (see the [Testing your code](#testing-your-code) section above).
1. **Commit** all changes in your lab files with meaningful commit messages.

    > **IMPORTANT**: Make sure that the screenshot file is included in your commits so your teacher will be able to see it on GitHub
2. **Push** your commits to GitHub
3. **Verify** that the code on GitHub is correct
4. Create a **Pull request** using your lab branch as the 'compare' branch and the main branch as the 'base'
5. Navigate to the "Files Changed" tab of your pull request, and **copy the URL** to this page into the lab folder on the LMS.

## Rubric

See the rubric attached to this lab in the LMS

### Automatic limits:

Your grade will be limited to a maximum of 79% for any of the following:
- Missing / inadequate [AI Use Statement](#ai-use)
- Missing / inadequate [Reflections](#reflections)
- Incorrect lab [Setup](#setup)
