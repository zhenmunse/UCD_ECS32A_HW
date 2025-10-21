# Unit 4 Repeated Execution

------

> “The power of the computer lies in its ability to perform repetitive tasks accurately and tirelessly.” – Donald E. Knuth

- ## 1. Why Repetition Matters

  Computers are fast not because they “think,” but because they **repeat** — performing simple operations thousands or millions of times without error.
   Repeated execution gives programs the ability to model processes, analyze data, simulate growth, and perform calculations that would be impractical by hand.

  We use **loops** to express repeated execution.

  ### The Three Forms of Control Flow

  | Type        | Description                    | Example              |
  | ----------- | ------------------------------ | -------------------- |
  | Sequential  | Statements run top to bottom   | Assignment, print    |
  | Conditional | Execute statements selectively | `if`, `elif`, `else` |
  | Repeated    | Execute statements repeatedly  | `while`, `for`       |

  ------

  ## 2. Basic Structure of a While Loop

  A **loop** repeats a block of code while a condition is true.

  ```python
  while condition:
      statement(s)
  ```

  **Example: Countdown**

  ```python
  n = 3
  while n > 0:
      print(n)
      n = n - 1
  print("Contact!")
  ```

  - **Iteration variable** (`n`) controls when the loop stops.
  - Loop terminates when condition evaluates to `False`.

  Flowchart:

  ```pgsql
       +---------------+
       |   condition   |
       +-------+-------+
               |
            True ↓
          statements
               |
               +----> back to test
            False ↓
             exit loop
  ```

  ------

  ## 3. Increment and Decrement

  Updating variables is a key part of loop control.

  ```python
  x = 0
  x = x + 1   # increment
  x = x - 1   # decrement
  x += 1      # shorthand increment
  x -= 1      # shorthand decrement
  ```

  Without proper updates, your loop may **never stop**.

  ------

  ## 4. Types of Loops

  ### Definite Loops

  - Number of iterations **known in advance**.
  - Example: printing a multiplication table.

  ```python
  num = int(input("Enter a number: "))
  i = 1
  while i <= 9:
      print(i, "x", num, "=", i*num)
      i += 1
  ```

  ### Indefinite Loops

  - Number of iterations **depends on a condition**.
  - Often used for interactive programs.

  ```python
  while True:
      line = input(">")
      if line == "done":
          break
      print(line)
  print("Done!")
  ```

  ------

  ## 5. Infinite Loops and the Break Statement

  ### Infinite Loop (Bad Example)

  ```python
  n = 3
  while n > 0:
      print(n)
      n = n + 1  # wrong direction
  print("Contact!")
  ```

  The loop never ends because `n` grows forever.

  You can terminate it in IDLE with **Ctrl + C**.

  ### The Break Statement

  `break` exits the loop immediately.

  ```python
  n = 3
  while True:
      print(n)
      n = n - 1
      if n == 0:
          break
  print("Contact!")
  ```

  ------

  ## 6. Continue Statement

  `continue` skips the rest of the loop block and goes back to the top.

  ```python
  while True:
      line = input(">")
      if line == "skip":
          continue
      if line == "done":
          break
      print(line)
  print("Done!")
  ```

  Useful for **filtering input** or **skipping invalid data** without stopping the loop.

  ------

  ## 7. Commenting Loops

  - Add comments describing:
    - **Purpose** of the loop;
    - **Condition** or **termination rule**.

  ```python
  # Print 'spam.' four times
  count = 1
  while count <= 4:
      print("spam.")
      count += 1
  # Print 'spam.' until user enters 'y'
  done = False
  while not done:
      print("spam.")
      ans = input("Stop the spam? ")
      if ans == "y":
          done = True
  ```

  ------

  ## 8. Loop Patterns in Programs

  ### Looping for Valid Input

  A classic pattern: keep asking until valid data is entered.

  ```python
  while True:
      ans = input("Enter your choice (a, b, or c): ")
      if ans in ['a', 'b', 'c']:
          break
      print("Invalid input.")
  print("You entered", ans)
  ```

  Alternative using condition:

  ```python
  ans = input("Enter your choice: ")
  while ans not in ['a', 'b', 'c']:
      print("You must choose a, b or c")
      ans = input("Enter your choice: ")
  ```

  ------

  ### Counting and Summation Loops

  ```python
  count = 0
  total = 0
  while True:
      value = input("Enter a number (or 'done' to finish): ")
      if value == "done":
          break
      total += float(value)
      count += 1
  print("Count:", count, "Sum:", total, "Average:", total/count)
  ```

  ------

  ### Finding Min and Max with None

  When you don’t have a starting value, use `None` as a placeholder.

  ```python
  max_val = None
  min_val = None
  
  while True:
      inp = input("Enter a number (or 'done'): ")
      if inp == "done":
          break
      num = float(inp)
      if max_val is None or num > max_val:
          max_val = num
      if min_val is None or num < min_val:
          min_val = num
  
  print("Max:", max_val, "Min:", min_val)
  ```

  - Uses **short-circuit evaluation** to avoid comparing `None` with numbers.
  - Illustrates the **guardian pattern**: check the safe condition first.

  ------

  ## 9. Nested Loops

  Loops inside loops can handle multi-dimensional tasks.

  ### 9×9 Multiplication Table

  ```python
  i = 1
  while i <= 9:
      j = 1
      while j <= 9:
          print("{:4.0f}".format(i * j), end="")
          j += 1
      print()
      i += 1
  ```

  Output is formatted into columns using width specifiers (`{:4.0f}`).

  ------

  ## 10. Formatting and Advanced Output

  ### The `.format()` Method

  ```python
  amount = 123.43
  pct = 18
  tip = amount * (pct / 100)
  print("A {:.0f}% tip would be ${:.2f}".format(pct, tip))
  ```

  Result:

  ```
  A 18% tip would be $22.22
  ```

  ### F-Strings (Python 3.6+)

  Simpler and faster:

  ```python
  print(f"A {pct:.0f}% tip would be ${tip:.2f}")
  ```

  ### Custom Separators and End Characters

  ```python
  print("Magic", 8, "Ball", sep="+", end="!")
  # Output: Magic+8+Ball!
  ```

  ### Tab-Separated Values

  ```python
  print("Year", "Balance", sep="\t")
  print(1, "$5000.00", sep="\t")
  ```

  → Useful for pasting into spreadsheets.

  ------

  ## 11. Practical Loop Examples

  ### Example 1: Compound Interest

  **Annual Compounding**

  ```python
  balance = 100
  rate = 7.0
  year = 1
  while year <= 50:
      interest = balance * (rate / 100)
      balance += interest
      year += 1
  print(f"In 50 years you'll have ${balance:.2f}")
  ```

  **Monthly Compounding**

  ```python
  balance = 100
  rate = 7.0 / 12
  month = 1
  while month <= 50 * 12:
      interest = balance * (rate / 100)
      balance += interest
      month += 1
  print(f"In 50 years you'll have ${balance:.2f}")
  ```

  ------

  ### Example 2: Guessing Game

  ```python
  import random
  games = 0
  score = 0
  
  while True:
      target = random.randint(1, 3)
      guess = input("Enter a number 1–3 or 'q' to quit: ")
      if guess == "q":
          break
      games += 1
      if int(guess) == target:
          print("You’re right!")
          score += 1
      else:
          print(f"Too {'low' if int(guess) < target else 'high'}! I was thinking of {target}.")
  print(f"You scored {score} out of {games}")
  ```

  This is an **indefinite loop** with exit condition (`'q'`), counters, and formatted feedback.

  ------

  ### Example 3: Saving to a Million

  ```python
  balance = 1400.0
  monthly_savings = 100
  rate = 7.0 / 12
  month = 0
  
  while balance < 1_000_000:
      interest = balance * (rate / 100)
      balance += monthly_savings + interest
      month += 1
  
  print("It took", month // 12, "years and", month % 12, "months.")
  ```

  ------

  ## 12. Patterns and Good Practice

  - **Initialize before the loop**
     (counters, accumulators, flags)
  - **Update inside the loop**
     (avoid infinite loops)
  - **Use break and continue carefully**
     to simplify logic, not complicate it.
  - **Comment loops** with purpose and condition.
  - **Avoid deep nesting** — flatten with combined conditions or flags.
  - **Use f-strings and format specifiers** for readable results.
  - **Apply loops to real problems**: accumulation, simulation, searching, input validation.

  ------

  ## 13. Key Takeaways

  - Loops make programs dynamic and powerful.
  - `while` loops support both **definite** (known count) and **indefinite** (condition-driven) iteration.
  - `break` exits loops, `continue` skips to the next iteration.
  - Combine repetition with formatted output for **data tables and models**.
  - Practical patterns: input validation, counting, statistics, simulation, and financial computation.

  > *"Repetition does not transform a lie into a truth, but it can transform a simple process into a masterpiece of precision — when executed by a computer."*
