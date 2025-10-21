# Unit 3 Conditional Execution

------

> “The chains of habit are too weak to be felt until they are too strong to be broken.” – Samuel Johnson

## 1. From Sequential to Conditional Execution

- **Sequential execution**: every statement runs in order.
- **Conditional execution**: check a condition → decide which block runs.
- Enables a program to *adapt to different inputs* or *situations*.

Example:

```python
if condition:
    # do one or more indented statements
```

The condition is a **Boolean expression** — an expression that evaluates to `True` or `False`.

------

### Boolean values and expressions

- Boolean values: `True`, `False` (type `bool`)
- A **Boolean expression** is any expression that evaluates to `True` or `False`.

Examples:

```python
'Black' == 'White'     # False
'Black' != 'White'     # True
```

`==` → *is equal to*
`!=` → *is not equal to*

------

### Checking for no input

```python
name = input("Hello. What's your name?")

if name == "":
    print("I beg your pardon?")
else:
    print("Nice to meet you", name + ".")
```

- `""` is the **empty string**, meaning length `0`.
- `==` checks equality; `=` assigns a value.
- Indented statements form a **block** — executed together when condition is true.

------

## 2. Alternative and Chained Execution

### if–else structure

When there are two possible outcomes:

```python
if condition:
    # executed if condition is True
else:
    # executed if condition is False
```

Example:

```python
num = int(input("Enter an even integer:"))
if num % 2 == 1:
    print("That's odd.")
else:
    print("Thanks!", num, "is a good number.")
```

------

### if–elif–else (chained conditionals)

Used for multiple mutually exclusive cases:

```python
if condition1:
    # executed if condition1 True
elif condition2:
    # executed if condition2 True
else:
    # executed if all above are False
```

Rules:

- Only **one** block runs.
- Conditions are checked **top to bottom**.
- You can have many `elif`s but only one `else`.

Example:

```python
age = int(input("Enter your age:"))
if age >= 18:
    print("You can vote.")
elif age >= 16:
    print("You can drive but can’t vote.")
else:
    print("You can trick or treat.")
```

------

### Nested conditionals

Conditionals inside conditionals:

```python
if raining == "y":
    if windy == "y":
        print("Take a raincoat.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your walk.")
```

- Use sparingly; complex nesting is hard to read.
- **Flat is better than nested** — combine conditions using logical operators when possible:

```python
if x > 0 and x < 10:
    print("Single-digit positive number.")
```

------

## 3. Boolean Logic and Logical Operators

### Comparison operators

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | equal to                 |
| `!=`     | not equal to             |
| `>`      | greater than             |
| `>=`     | greater than or equal to |
| `<`      | less than                |
| `<=`     | less than or equal to    |

Example:

```python
score = 67
if score >= 60:
    print("You passed!")
```

String comparison is case- and space-sensitive:

```python
"apple" == "Apple"  # False
" " == ""           # False
```

------

### Logical operators

- `and`: both conditions must be `True`
- `or`: at least one condition must be `True`
- `not`: reverses a Boolean value

Example:

```python
temp = int(input("Enter degrees Celsius:"))

if temp > 0 and temp < 100:
    print("Water is liquid.")

if temp <= 0 or temp >= 100:
    print("Water is not liquid.")
```

------

### Truth tables

| A     | B     | A and B | A or B |
| ----- | ----- | ------- | ------ |
| True  | True  | True    | True   |
| True  | False | False   | True   |
| False | True  | False   | True   |
| False | False | False   | False  |

`not True` → `False`
`not False` → `True`

------

### Example: Simple chatbot

```python
color = input("What's your favorite color?")
if color == 'Red' or color == 'red':
    print('I like red too!')

temp = int(input("What’s your temperature?"))
if temp > 97 and temp < 100:
    print('Sounds normal!')
```

------

### Operator precedence

1. Arithmetic operators (PEMDAS)
2. Comparison operators (`<`, `>=`, etc.)
3. `not`
4. `and`
5. `or`

Parentheses can always be used to clarify order.

------

### Common logic error

```python
if color == 'Red' or 'red':    # this would be always True
    print("I like red too!")
```

Why?

- `'red'` as a non-empty string is always `True`.
- Correct version:

```python
if color == 'Red' or color == 'red':
    print("I like red too!")
```

------

### Truthiness in Python

Python treats values as `True` or `False` based on content.

```python
bool(1)       # True
bool(0.0)     # False
bool("False") # True
bool("")      # False
```

Non-zero numbers and non-empty strings are considered **True**.

------

## 4. Complex Conditionals and Applications

### Temperature categories

Example using chained conditionals:

```python
temp = int(input("Enter degrees Celsius:"))

if temp <= 0:
    print("Water is a solid.")
elif temp >= 100:
    print("Water is a gas.")
else:
    print("Water is a liquid.")
```

### Assigning letter grades

```python
percent = 78
if percent >= 90:
    grade = "A"
elif percent >= 80:
    grade = "B"
elif percent >= 70:
    grade = "C"
elif percent >= 60:
    grade = "D"
else:
    grade = "F"
```

------

### Income tax schedule (nested example)

```python
if marital_status == "s":
    if income <= 32000:
        tax = 0.10 * income
    else:
        tax = 3200 + 0.25 * (income - 32000)
else:
    if income <= 64000:
        tax = 0.10 * income
    else:
        tax = 6400 + 0.25 * (income - 64000)
```

- Use nested `if` to separate conditions that depend on each other.
- Always test incrementally (“prototype and patch”).

------

## 5. Boolean Variables, Guardian Pattern, and De Morgan’s Law

### Boolean variables

Variables that store Boolean values (`True` or `False`) for readability.

```python
raining = (input("Is it raining?") == "y")
windy = (input("Is it windy?") == "y")

if raining and not windy:
    print("Take an umbrella.")
```

### The Guardian Pattern

Prevents runtime errors by checking dangerous conditions first.

```python
if total != 0 and correct/total >= 0.6:
    print("Doing good!")
if total == 0 or correct/total < 0.6:
    print("Try harder.")
```

- `and` and `or` use **short-circuit evaluation**:
  - For `and`: if left side is `False`, right side is skipped.
  - For `or`: if left side is `True`, right side is skipped.

------

### De Morgan’s Law

Simplifies negated compound expressions.

| Original        | Equivalent        |
| --------------- | ----------------- |
| `not (A and B)` | `not A or not B`  |
| `not (A or B)`  | `not A and not B` |

Example:

```python
if not (state == "AK" or state == "HI"):
    print("Ground shipping applies")

# Equivalent to:
if state != "AK" and state != "HI":
    print("Ground shipping applies")
```

Another example:

```python
if not (temp > 0 and temp < 100):
    print("Water is not liquid.")
# Same as:
if temp <= 0 or temp >= 100:
    print("Water is not liquid.")
```

------

## 6. Key Takeaways

- **if statements** control program flow based on Boolean conditions.
- **elif and else** allow for multiple alternatives.
- **and, or, not** combine or negate conditions.
- **Nested ifs** should be avoided when possible — flatten logic with compound expressions.
- **Boolean variables** improve readability.
- **Guardian pattern** and **De Morgan’s Law** prevent errors and simplify expressions.
- Always test incrementally and reason carefully about condition order.
