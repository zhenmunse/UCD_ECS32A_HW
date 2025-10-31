# Unit 9 Object-Oriented Programming (OOP)

> Organize larger programs around **objects** so code is easier to read, reuse, test, and extend.

---

*This module might be taught again at the beginning of ECS32B*

------

## 1. Core vocabulary and concepts

- **Class**: a *blueprint* (new data type) that bundles data + behavior.
- **Object / Instance**: a concrete value created from a class.
- **Attributes**: variables stored inside an object (its state).
- **Methods**: functions defined inside a class that operate on the object.
- **Instantiation**: creating an object from a class, e.g. `car = Car()`.
- **Dot syntax**: access members with `object.attribute` / `object.method(...)`.

Python mapping you already know:

- *Value* ↔ **Object**, *Data type* ↔ **Class** (e.g., `"A"` ↔ `str`, `[1,2,3]` ↔ `list`).

------

## 2. Defining and using classes

A class is defined using the `class` keyword. It usually contains a constructor method `__init__`, and other methods that define behavior.

```python
class Car:
    def __init__(self, body_type="Car", color="White"):
        self.mileage = 0
        self.body_type = body_type
        self.color = color

    def drive(self, miles):
        self.mileage = self.mileage + miles
        print("So far", self.mileage, "miles")
```

Usage:

```python
my_car = Car("Sedan", "Teal")
my_car.drive(30)         # So far 30 miles
print(type(my_car))      # <class '__main__.Car'>
print(my_car.mileage)    # 30
```

### The `__init__` constructor

- Runs automatically when a new object is created.
- Initializes attributes.
- May include default parameters (`Car()` makes a white car).

### The `self` parameter

- Always the first parameter of an instance method.
- Refers to the object the method is called on.
- Attributes are always accessed using `self.attribute` inside class methods.

## 3. Attributes and methods

Objects combine **state (attributes)** with **behavior (methods)**.

```python
class OdometerCar:
    def __init__(self):
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print("So far", self.mileage, "miles")
```

### Accessing attributes directly

```python
c = OdometerCar()
c.drive(20)
print(c.mileage)   # 20
c.mileage = 100    # dangerous if uncontrolled
```

### Getter and setter methods

Safer way to access/modify attributes.

```python
class SafeCar:
    def __init__(self):
        self.mileage = 0

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, new_value):
        if new_value >= self.mileage:
            self.mileage = new_value
        else:
            print("Can't roll back mileage")
```

Usage:

```python
car = SafeCar()
car.set_mileage(120)
print(car.get_mileage())  # 120
```

- Getters return the value of an attribute.
- Setters modify the attribute safely, enforcing rules.
- This is part of **encapsulation**.

------

## 4. Examples of simple classes

### Tally Counter

Models a device that counts clicks.

```python
class Counter:
    def __init__(self):
        self.value = 0

    def click(self):
        print("Click.")
        self.value += 1

    def get_value(self):
        return self.value

    def reset(self):
        self.value = 0
```

### Magic 8 Ball

Simulates the toy that gives random answers.

```python
import random

class Magic8Ball:
    def __init__(self, path="magic_answers.txt"):
        self.answers = []
        with open(path) as infile:
            for line in infile:
                line = line.strip()
                if line:
                    self.answers.append(line)

    def play(self):
        print(random.choice(self.answers))

    def add_answer(self, ans):
        self.answers.append(ans)

    def get_num_answers(self):
        return len(self.answers)
```

------

## 5. Four principles of OOP

### Abstraction

- Hide complexity, expose a simple interface.
- Users of an object don’t need to know internal implementation.
- Example: you call `drive(miles)` without knowing how mileage is updated.

### Encapsulation

- Keep data safe by controlling access.
- Prevent programmers from directly changing attributes.
- Enforce rules with setter/getter methods.

### Polymorphism

- Same operations can apply to different object types.
- Example: `print()` works on many types because of `__str__` / `__repr__`.
- Example: sorting objects if `__lt__` is defined.

### Inheritance

- Child classes can reuse and extend parent class code.
- Supports hierarchical design.
- Example: `BatteryBossMachine` inherits from `BossMachine`.

------

## 6. Case study: Boss vending machines

### Base BossMachine class

```python
class BossMachine:
    def __init__(self, cans=2, capacity=550):
        self.capacity = capacity
        self.price = 2.25
        self.cash = 0.0
        self.numberOfCans = cans

    def buyBoss(self):
        if self.numberOfCans > 0:
            self.numberOfCans -= 1
            self.cash += self.price
            print("Have a Boss")
        else:
            print("Sold Out")

    def refillCans(self, cans=100):
        if self.numberOfCans + cans <= self.capacity:
            self.numberOfCans += cans

    def checkCans(self):
        return self.numberOfCans

    def getCash(self):
        return self.cash

    def setPrice(self, price):
        self.price = price
```

### Encapsulation in action

- Instead of `machine.numberOfCans = 12465`, you should call `refillCans()`.
- Instead of `machine.cash = -9999`, you should use `getCash()` safely.

### Polymorphism hooks

Add custom behavior for `print()` and `<`.

```python
def __repr__(self):
    return f"Cans: {self.numberOfCans}, Cash: ${self.cash:.2f}"

def __lt__(self, other):
    return self.cash < other.cash
```

### Inheritance

```python
class BatteryBossMachine(BossMachine):
    def __init__(self, cans=2, capacity=550):
        super().__init__(cans, capacity)
        self.charge = 1000
        print("Fully charged!")

    def buyBoss(self):
        super().buyBoss()
        self.charge -= 1
        print("Charge remaining", self.charge)
```

------

## 7. Special methods (“dunder” methods)

- **`__init__`**: constructor, runs when creating object.
- **`__repr__`**: how object is represented as a string (used by `print()`).
- **`__lt__`**: less-than comparison (`<`) for sorting.
- **`__str__`**: human-readable string (fallback for `print()`).
- **`__eq__`**: equality comparison (`==`).

These allow Python objects to behave like built-ins.

------

## 8. Method definition patterns

- Always include `self` as first parameter.
- Use `return` to produce output.
- Default parameters allowed, filled left to right.

Example:

```python
class Car:
    def __init__(self, body_type="Car", color="White"):
        self.body_type = body_type
        self.color = color
```

Usage:

- `Car()` → White Car
- `Car("Truck")` → White Truck

------

## 9. Common pitfalls

- Forgetting `self` in method definitions or calls.
- Mutating attributes directly instead of using methods.
- Using mutable default arguments (`list`, `dict`) in parameters.
- Variable names colliding with built-ins (`list`, `dict`, `max`).
- Assuming true privacy: Python only uses naming conventions (`_internal`).







