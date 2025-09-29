## Unit 1 Introduction

#### Course Overview & Getting Started

| Week | Topic                          | Chapters |
| ---- | ------------------------------ | -------- |
| 1    | Intro                          | 1        |
| 1~2  | Variable, type, statement, I/O | 2        |
| 2~3  | Conditional execution          | 3        |
| 4    | Functions, Iteration           | 4,5      |
| 5~6  | Strings, Files                 | 6,7      |
| 7~8  | Lists, Dictionaries, Tuples    | 8,9      |
| 9~10 | OOP, other big ideas           | 14       |

#### Course Structure

- Homework - 50%:
  - Gradescope - 45%;
  - Coding style and best practices - 5%;
- Quiz - 50%: 8 quizzes with 2 drops allowed ;

How to learn to program?

- Analysis of Existing Programs
- Synthesis of New Programs aka prototype and patch

> [!NOTE]
>
> Resources: IDLE, Python Tutor, Lecture Slides, Textbook, Jupyter notebooks, Core Python Notebook

#### Python Interpreter & IDLE

Interpreter interprets programs from high level language to binary language line-by-line.

Download Python, then open IDLE.

IDLE Shell -> File -> New File to the text editor

Syntax High Lighting:

``````python
hello
``````

but

``````python
print
``````

because `print` is a valid function while `hello` is not.

If not follow the rule, a `syntax error` would occur. The following is an example when you type in shell:

```python
print(Welcome to ECS32A)
```

the shell would respond as following:
```shell
  File "<stdin>", line 1
    print(Welcome to ECS32A)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

