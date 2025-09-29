<<<<<<< HEAD
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

=======
# ECS 32A – Unit 1 Introduction

## Welcome to ECS 32A
- **Course goal**: Learn how to write programs from scratch, with no prior programming experience.
- Programming = a new language → requires practice & collaboration.
- Students come from diverse majors; programming is a general problem-solving tool.

> “Computer science is the new math.” – Christos Papadimitriou

---

## Why Learn to Program?
- Computers are used in almost every field.
- Programming goes beyond spreadsheets:
  - Handle data not in the right format.
  - Create tools not available off the shelf.
- Even if this is your last CS course, you’ll leave with:
  - A **powerful, flexible, free tool**.
  - An analytical skill to add to your resume.

---

## Why Python?
- **Portability**: Runs on most platforms; free & accessible.
- **Readability**: Shorter, simpler syntax.
  - *“Code is more often read than written.” – Guido van Rossum*
- **Developer productivity**:
  - Interpreted (no compiling step).
  - Large ecosystem of modules (graphics, data science, ML, web, etc.).
- **Popularity**: Used at Google, YouTube, NASA, Tesla, Pixar, etc.
- **Comparison**: Python programs are 3–10× shorter than Java or C++.

---

## Python & AI
- AI chatbots are good at Python → helps you code faster.
- Limitation:
  - Errors on complex tasks.
  - Stunts critical thinking if overused.
- In this course:
  - Learn Python **yourself**.
  - AI is **not allowed during exams**.

---

## Tools: IDLE & Jupyter
- **IDLE**: Integrated Development and Learning Environment
  - Shell: interactive line-by-line execution.
  - Script editor: write, save, and run full programs.
- **Jupyter Notebooks**:
  - Learned in discussion sections.
  - Popular in AI/ML and data science.

---

## Computer Model Recap
- **CPU**: asks “What next?” billions of times/sec.
- **Main memory**: fast, temporary (lost without power).
- **Secondary memory**: long-term storage.
- **Network**: remote storage/retrieval.
- **I/O devices**: keyboard, screen, etc.
- Programming = orchestrating all these resources with instructions.

---

## Interpreter vs Compiler
- **Interpreter**: Converts high-level → machine code *line by line* (Python).
- **Compiler**: Converts once → optimized machine code file (C, C++).
- Python = interpreted → fast to write & test.

---

## Course Overview
| Week | Topic                          | Chapters |
| ---- | ------------------------------ | -------- |
| 1    | Introduction                   | 1        |
| 1–2  | First programs, variables, I/O | 2        |
| 2–3  | Conditional execution          | 3        |
| 4    | Functions, iteration           | 4–5      |
| 5–6  | Strings, files                 | 6–7      |
| 7–8  | Lists, dictionaries, tuples    | 8–9      |
| 9–10 | OOP, big ideas in CS           | 14       |

---

## Course Structure
- **Homework (50%)**
  - Gradescope autograded – 45%
  - Coding style/manual grading – 5%
  - Work in groups of ≤3, but comments must be in your own words.
  - Unlimited resubmissions before deadline; late = 50% recovery.
- **Quizzes (50%)**
  - 6 quizzes in discussion sections.
  - Open-note; lowest 2 dropped.
  - Final = optional, counts as 2 quizzes.

---

## How to Learn Programming
- **Analysis**: Study existing code.
- **Synthesis**: Prototype & patch new programs.
- **Resources**:
  - IDLE, Python Tutor, Jupyter notebooks.
  - Lecture slides, textbook (*Python for Everybody*).
  - Core Python notebook (quick reference).

---

## Weekly Activities
- **Lecture**: 3 hrs – examples, demos, type-along.
- **Discussion**: 1 hr – Jupyter, quizzes, practice.
- **Support**:
  - Piazza (Q&A), Discord (tutors).
  - Office hours, Stay Late and Code (SLAC nights).
- **Engagement**:
  - Interactive textbook, code exercises.
  - Python Tutor links for step-by-step execution.
  - Practice sample exams on Gradescope.

---

## Assignments & First Program
- Install Python & IDLE.
- Write first script: `print("Welcome to ECS32A!")`
- **Welcome Assignment**: Submit simple programs to Gradescope until 100%.
>>>>>>> daec4984bb93132cbb8a768962a2f4c1ce9662e9
