# Unit 2 First Programs

> “Programs do things with stuff.” – Mark Lutz, *Learning Python*

---

## 1. Printing to the Screen
- Use **IDLE shell** for interactive execution.
- **Statement** = a unit of code that has an effect.
- **`print()`** is a built-in function.
  
  - Input inside parentheses is processed and output.
  - Strings = text inside quotes `" "` or `' '`.
  - Use matching quotes to handle apostrophes:
    ```python
    print("You can't play here")  # works
    print('You can\'t play here') # also works
    print('You can't play here')  # SyntaxError: invalid syntax
    ```

### Special Characters
- `\n` → new line  
- `\t` → tab  
- These are **whitespace characters**.

### Multiple Arguments in `print()`
```python
print("Welcome", "to", "ECS32A!") 
# Output: Welcome to ECS32A!
```

- Arguments separated by commas → printed with spaces.
- By default, output ends with `\n`.

## 2. Expressions, Operators & Precedence

- **Expression** = reduces to a value.
   Example: `4 + 5` → `9`.
- **Operators**: `+ - * / **`
- **Precedence (PEMDAS)**:
  1. Parentheses `()`
  2. Exponentiation `**`
  3. Multiplication / Division `* /`
  4. Addition / Subtraction `+ -`
- Always use parentheses when unsure.

## 3. Values and Types

- **Value** = basic data unit (number, text).
- **Type** = category of a value (determines representation & operations).
- Python types:
  - `int` → integers (`42`)
  - `float` → floating-point numbers (`42.0`)
  - `str` → strings (`"42"`)

### Type Checking

```python
type(42)     # <class 'int'>
type(42.0)   # <class 'float'>
type("42")   # <class 'str'>
```

### Floating Point Issues

- Division always → float in Python 3.
- Floating point ≠ exact (due to binary representation).

## 4. Variables & Assignment

- **Assignment**: `x = 2`
   → “Assign 2 to x”.
- Variables = boxes labeled with names.
- Values inside can be updated.

### Increment Pattern

```python
count = count + 1  # increases count by 1
```

### Swapping Values

```python
# Incorrect (overwrites)
x = y
y = x

# Correct (using a temporary variable)
z = x
x = y
y = z
```

### Naming Rules

- Use **meaningful names** (mnemonics).
- Rules:
  - Can use letters, digits, `_`.
  - Cannot start with digit.
  - Case sensitive.
  - Avoid Python keywords & built-in names.
- Styles:
  - `camelCase`
  - `snake_case` (preferred in Python).

## 5. Writing Programs

- **Statement**: executable instruction (`print(x)`).
- **Expression**: reduces to a value (`x + 1`).
- Program = sequence of statements.

### Scripts in IDLE

1. File → New File
2. Write statements
3. Run → Run Module
4. Output appears in shell

------

## 6. Comments & Headers

- Start with `#` → ignored by interpreter.

- Purpose: explain *why*, not just *what*.

- Good variable names reduce need for comments.

- Headers at top of script:

  ```python
  # fahr2cel.py
  # Author: Name
  # Homework 1: Convert Fahrenheit to Celsius
  ```

------

## 7. Building Blocks of Programs

1. **Input** – get data from outside (e.g., `input()`).
2. **Output** – show results (`print()`).
3. **Sequential execution** – run statements in order.
4. **Conditional execution** – make decisions.
5. **Repeated execution** – loops.
6. **Code reuse** – functions, modules.

------

## 8. Advanced Operators

- **Floor Division `//`**

  ```python
  42.0 // 10  # 4.0
  -42 // 10   # -5
  ```

- **Modulus `%`**

  ```python
  105 % 60   # 45
  ```

  - Common use: check divisibility, parity.

- **String Operators**

  - `+` → concatenation (`"ECS" + "32A"` → `"ECS32A"`)
  - `*` → repetition (`"Hi"*3` → `"HiHiHi"`)

------

## 9. User Input

- `input("Prompt")` → always returns a **string**.

- Must convert types if doing math:

  ```python
  fahrenheit = float(input("Enter Fahrenheit: "))
  celsius = (fahrenheit - 32) * 5/9
  print("Celsius:", celsius)
  ```

------

## 10. Built-in Functions

- **Seen so far**:
  - `print()`
  - `type()`
  - `input()`
  - `int()`, `float()`, `str()`
- Functions:
  - Called with parentheses.
  - Take arguments (inputs).
  - May return values.

## 11. Example Programs

### Parrot

```python
text = input("Enter some text: ")
print("You entered '" + text + "'")
```

### Check Splitter

```python
total = float(input("Total bill: "))
people = int(input("Number of diners: "))
share = total / people
print("Each person owes $" + str(share))
```

### Postage Stamp Machine

```python
STAMP_PRICE = 55
dollars = int(input("Enter number of dollars: "))
pennies = 100 * dollars
stamps = pennies // STAMP_PRICE
change = pennies % STAMP_PRICE
print("First class stamps:", stamps)
print("Change:", change, "cents")
```