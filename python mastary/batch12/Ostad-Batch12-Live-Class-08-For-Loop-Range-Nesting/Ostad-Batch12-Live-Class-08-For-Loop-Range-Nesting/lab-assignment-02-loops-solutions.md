# Lab Assignment - 2 (Loops) - Python Version (Solutions)

> এটি `Ostad-Batch11-Live-Class-07-While-Loop-Counters/lab-assignment-02-loops-questions.md` - এর সমাধান। প্রশ্নগুলো Live Class 07 (While Loop)-এ দেওয়া হয়েছিল, `while` লুপ দিয়েই আগে নিজে চেষ্টা করার জন্য। এখানে সব সমাধান দেওয়া হলো - Live Class 08-এ `for` loop শেখার পর চাইলে এই একই প্রশ্নগুলো `for` + `range()` দিয়েও আবার লিখে দেখতে পারেন, দুই রকম loop-এর পার্থক্য বোঝার জন্য এটা খুব ভালো অনুশীলন।
>
> সব কোড রান করে output verify করা হয়েছে।

---

## অংশ ১: Counting ও Basic Loops

### 1. ১ থেকে ১০০ পর্যন্ত গণনা প্রিন্ট করুন।

```python
n = 1
while n <= 100:
    print(n, end=" ")
    n += 1
```

**Output:**
```text
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
```

---

### 2. ১০০ থেকে ১ পর্যন্ত উল্টো গণনা প্রিন্ট করুন।

```python
n = 100
while n >= 1:
    print(n, end=" ")
    n -= 1
```

**Output:**
```text
100 99 98 ... 3 2 1
```

---

### 3. প্রথম ১০টি সংখ্যার যোগফল বের করুন।

```python
total = 0
n = 1
while n <= 10:
    total += n
    n += 1

print("Sum of first 10 numbers:", total)
```

**Output:**
```text
Sum of first 10 numbers: 55
```

---

### 4. ব্যবহারকারীর কাছ থেকে একে একে ৩টি সংখ্যা নিয়ে তাদের যোগফল দেখান।

```python
total = 0
count = 0
while count < 3:
    num = float(input(f"Enter number {count + 1}: "))
    total += num
    count += 1

print("Sum:", total)
```

**Output (example):**
```text
Enter number 1: 5
Enter number 2: 10
Enter number 3: 15
Sum: 30.0
```

---

### 5. একটি সংখ্যার factorial বের করুন।

```python
n = int(input("Enter a number: "))

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1

print(f"{n}! = {fact}")
```

**Output (example):**
```text
Enter a number: 5
5! = 120
```

> Edge case: `n = 0` দিলে loop-এর body একবারও না চলেই `fact = 1` প্রিন্ট হবে (যেহেতু `while 1 <= 0` প্রথমেই `False`) - `0! = 1` গাণিতিকভাবে ঠিক আছে।

---

### 6. দুটি সংখ্যা (base, power) নিয়ে power-এর মান বের করুন - `**` অপারেটর ছাড়া।

```python
base = int(input("Enter base: "))
power = int(input("Enter power: "))

result = 1
i = 0
while i < power:
    result *= base
    i += 1

print(f"{base}^{power} = {result}")
```

**Output (example):**
```text
Enter base: 2
Enter power: 10
2^10 = 1024
```

---

### 7. একটি সংখ্যা নিয়ে তার প্রতিটি ডিজিটের যোগফল বের করুন।

```python
num = int(input("Enter a number: "))
original = num

total = 0
while num > 0:
    total += num % 10
    num //= 10

print(f"Sum of digits of {original} = {total}")
```

**Output (example):**
```text
Enter a number: 321
Sum of digits of 321 = 6
```

---

### 8. একটি সংখ্যা prime কিনা যাচাই করুন।

```python
n = int(input("Enter a number: "))

is_prime = True
if n < 2:
    is_prime = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
```

**Output (example):**
```text
Enter a number: 97
97 is a prime number.
```

---

## অংশ ২: Pattern Printing

### (a) বাম-সংলগ্ন বর্ধমান triangle

```python
rows = 5
row = 1
while row <= rows:
    line = ""
    col = 1
    while col <= row:
        line += "* "
        col += 1
    print(line)
    row += 1
```

**Output:**
```text
*
* *
* * *
* * * *
* * * * *
```

---

### (b) ডান-সংলগ্ন (mirror of a)

```python
rows = 5
row = 1
while row <= rows:
    line = "  " * (rows - row)
    col = 1
    while col <= row:
        line += "* "
        col += 1
    print(line)
    row += 1
```

**Output:**
```text
        *
      * *
    * * *
  * * * *
* * * * *
```

---

### (c) বাম-সংলগ্ন হ্রাসমান (upside-down a)

```python
rows = 5
row = rows
while row >= 1:
    line = ""
    col = 1
    while col <= row:
        line += "* "
        col += 1
    print(line)
    row -= 1
```

**Output:**
```text
* * * * *
* * * *
* * *
* *
*
```

---

### (d) ডান-সংলগ্ন হ্রাসমান (mirror of c)

```python
rows = 5
row = rows
while row >= 1:
    line = "  " * (rows - row)
    col = 1
    while col <= row:
        line += "* "
        col += 1
    print(line)
    row -= 1
```

**Output:**
```text
* * * * *
  * * * *
    * * *
      * *
        *
```

---

### (e) পূর্ণ পিরামিড

```python
rows = 5
i = 1
while i <= rows:
    spaces = "  " * (rows - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)
    i += 1
```

**Output:**
```text
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
```

---

### (f) উল্টো পিরামিড (mirror of e)

```python
rows = 5
i = rows
while i >= 1:
    spaces = "  " * (rows - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)
    i -= 1
```

**Output:**
```text
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
```

---

### (g) সংখ্যার বর্ধমান triangle

```python
rows = 6
row = 1
while row <= rows:
    line = ""
    col = 1
    while col <= row:
        line += str(col) + " "
        col += 1
    print(line)
    row += 1
```

**Output:**
```text
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
```

---

### (h) সংখ্যার হ্রাসমান triangle (mirror of g)

```python
rows = 6
row = rows
while row >= 1:
    line = ""
    col = 1
    while col <= row:
        line += str(col) + " "
        col += 1
    print(line)
    row -= 1
```

**Output:**
```text
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

---

### (i) একই অক্ষর row অনুযায়ী repeat, অক্ষর প্রতি row-তে বদলায়

```python
rows = 6
row = 1
while row <= rows:
    letter = chr(64 + row)  # 65 = 'A'
    line = ""
    col = 1
    while col <= row:
        line += letter + " "
        col += 1
    print(line)
    row += 1
```

**Output:**
```text
A
B B
C C C
D D D D
E E E E E
F F F F F F
```

---

### (j) row-এর repeat কমতে থাকে, অক্ষর row অনুযায়ী বদলায়

```python
rows = 6
row = 1
while row <= rows:
    letter = chr(64 + row)
    count = rows + 1 - row
    line = ""
    col = 1
    while col <= count:
        line += letter + " "
        col += 1
    print(line)
    row += 1
```

**Output:**
```text
A A A A A A
B B B B B
C C C C
D D D
E E
F
```

---

### (k) Floyd's Triangle

```python
rows = 6
row = 1
counter = 1
while row <= rows:
    line = ""
    col = 1
    while col <= row:
        line += str(counter) + " "
        counter += 1
        col += 1
    print(line)
    row += 1
```

**Output:**
```text
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
```

---

### (l) Pascal's Triangle

```python
rows = 5
prev_row = []
row = 1
while row <= rows:
    current_row = []
    col = 0
    while col <= row - 1:
        if col == 0 or col == row - 1:
            current_row.append(1)
        else:
            current_row.append(prev_row[col - 1] + prev_row[col])
        col += 1
    print(" ".join(str(x) for x in current_row))
    prev_row = current_row
    row += 1
```

**Output:**
```text
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

**Hint যেভাবে কাজ করে:** প্রতিটা নতুন row-এর প্রথম আর শেষ মান সবসময় `1`; মাঝের প্রতিটা মান আগের row-এর `prev_row[col-1] + prev_row[col]`। তাই একটা `prev_row` লিস্টে আগের row জমা রাখতে হয়।

---

### (m) অক্ষরের বর্ধমান diagonal

```python
rows = 6
row = 1
while row <= rows:
    line = ""
    col = 1
    while col <= row:
        line += chr(64 + col) + " "
        col += 1
    print(line)
    row += 1
```

**Output:**
```text
A
A B
A B C
A B C D
A B C D E
A B C D E F
```

---

### (n) (j)-এর মতোই লেআউট কিন্তু ডানে সংলগ্ন (mirrored)

```python
rows = 6
row = 1
while row <= rows:
    letter = chr(64 + row)
    count = rows + 1 - row
    spaces = "  " * (row - 1)
    line = ""
    col = 1
    while col <= count:
        line += letter + " "
        col += 1
    print(spaces + line)
    row += 1
```

**Output:**
```text
A A A A A A
  B B B B B
    C C C C
      D D D
        E E
          F
```

---

### (o) Checkerboard triangle

```python
rows = 5
row = 1
while row <= rows:
    line = ""
    col = 1
    while col <= row:
        line += str((row + col + 1) % 2) + " "
        col += 1
    print(line)
    row += 1
```

**Output:**
```text
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
```

> Hint-এ ভুলে `(row + col) % 2` লেখা হয়েছিল - আসল formula `(row + col + 1) % 2`, কারণ প্রথম ঘর (`row=1, col=1`) থেকে `1` দিয়ে শুরু করতে হবে।

---

## অংশ ৩: Series

### 9. Fibonacci series - ব্যবহারকারীর দেওয়া সংখ্যক টার্ম পর্যন্ত

```python
terms = int(input("How many terms? "))

a, b = 1, 1
count = 0
while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
```

**Output (example, terms = 9):**
```text
How many terms? 9
1 1 2 3 5 8 13 21 34
```

---

### 10. `2, 4, 8, 16, 32, 64, 128, 256`

```python
term = 2
while term <= 256:
    print(term, end=" ")
    term *= 2
```

**Output:**
```text
2 4 8 16 32 64 128 256
```

---

### 11. `1, 4, 7, 10, ..., 40`

```python
term = 1
while term <= 40:
    print(term, end=" ")
    term += 3
```

**Output:**
```text
1 4 7 10 13 16 19 22 25 28 31 34 37 40
```

---

### 12. `1, -4, 7, -10, ..., -40`

```python
term = 1
sign = 1
while term <= 40:
    print(sign * term, end=" ")
    term += 3
    sign *= -1
```

**Output:**
```text
1 -4 7 -10 13 -16 19 -22 25 -28 31 -34 37 -40
```

---

### 13. `1, 5, 11, 19, 29, ...`

```python
term = 1
step = 4
count = 0
while count < 5:
    print(term, end=" ")
    term += step
    step += 2
    count += 1
```

**Output:**
```text
1 5 11 19 29
```

---

### 14. `(1) + (1+2) + (1+2+3) + ...` - n টার্ম পর্যন্ত

```python
n = int(input("How many terms? "))

group = 1
while group <= n:
    num = 1
    subtotal = 0
    parts = []
    while num <= group:
        subtotal += num
        parts.append(str(num))
        num += 1
    print(f"({'+'.join(parts)}) = {subtotal}")
    group += 1
```

**Output (example, n = 4):**
```text
How many terms? 4
(1) = 1
(1+2) = 3
(1+2+3) = 6
(1+2+3+4) = 10
```

---

### 15. `(2) + (2+4) + (2+4+6) + ...` - n টার্ম পর্যন্ত

```python
n = int(input("How many terms? "))

group = 1
while group <= n:
    num = 2
    subtotal = 0
    parts = []
    count = 1
    while count <= group:
        subtotal += num
        parts.append(str(num))
        num += 2
        count += 1
    print(f"({'+'.join(parts)}) = {subtotal}")
    group += 1
```

**Output (example, n = 4):**
```text
How many terms? 4
(2) = 2
(2+4) = 6
(2+4+6) = 12
(2+4+6+8) = 20
```

---

### 16. `(1) + (1+3) + (1+3+5) + ...` - n টার্ম পর্যন্ত

```python
n = int(input("How many terms? "))

group = 1
while group <= n:
    num = 1
    subtotal = 0
    parts = []
    count = 1
    while count <= group:
        subtotal += num
        parts.append(str(num))
        num += 2
        count += 1
    print(f"({'+'.join(parts)}) = {subtotal}")
    group += 1
```

**Output (example, n = 4):**
```text
How many terms? 4
(1) = 1
(1+3) = 4
(1+3+5) = 9
(1+3+5+7) = 16
```

---

### 17. `(1²) + (1²+3²) + (1²+3²+5²) + ...` - n টার্ম পর্যন্ত

```python
n = int(input("How many terms? "))

group = 1
while group <= n:
    num = 1
    subtotal = 0
    parts = []
    count = 1
    while count <= group:
        subtotal += num ** 2
        parts.append(f"{num}^2")
        num += 2
        count += 1
    print(f"({'+'.join(parts)}) = {subtotal}")
    group += 1
```

**Output (example, n = 4):**
```text
How many terms? 4
(1^2) = 1
(1^2+3^2) = 10
(1^2+3^2+5^2) = 35
(1^2+3^2+5^2+7^2) = 84
```

---

### 18. `(2²) + (2²+4²) + (2²+4²+6²) + ...` - n টার্ম পর্যন্ত

```python
n = int(input("How many terms? "))

group = 1
while group <= n:
    num = 2
    subtotal = 0
    parts = []
    count = 1
    while count <= group:
        subtotal += num ** 2
        parts.append(f"{num}^2")
        num += 2
        count += 1
    print(f"({'+'.join(parts)}) = {subtotal}")
    group += 1
```

**Output (example, n = 4):**
```text
How many terms? 4
(2^2) = 4
(2^2+4^2) = 20
(2^2+4^2+6^2) = 56
(2^2+4^2+6^2+8^2) = 120
```
