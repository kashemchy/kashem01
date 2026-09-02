# Ostad Batch 12 — Live Class 05

## Module 2: Logic & Condition Building
### বিষয়: if এর ভেতরে if, Truthy/Falsy, আর ডিবাগিং

---

## এই ক্লাসের পর আপনি যা যা পারবেন

- একটা `if` এর ভেতরে আরেকটা `if` লিখতে পারবেন
- বুঝতে পারবেন কখন Nested if লাগে, আর কখন শুধু `and` দিয়েই কাজ চলে
- `if name:` এর মতো ছোট্ট করে শর্ত লিখতে পারবেন (Truthy/Falsy)
- কোড ভুল করলে ভয় না পেয়ে `print()` বসিয়ে ভুলটা নিজে খুঁজে বের করতে পারবেন
- চারটে সাধারণ ভুল চিনতে পারবেন, আর তাদের error message পড়তে পারবেন

---

## আগের ক্লাসে যা শিখেছিলেন (ঝালাই)

| যা শিখেছিলেন | মানে |
|---|---|
| `if` | শর্ত সত্যি হলে ভেতরের কাজটা করুন |
| `else` | শর্ত মিথ্যা হলে এই কাজটা করুন |
| `elif` | আগেরটা না মিললে এটা দেখুন |
| `==` `!=` `>` `<` `>=` `<=` | দুটো জিনিস মিলিয়ে দেখার চিহ্ন |
| `and` | দুটো শর্তই সত্যি হতে হবে |
| `or` | যেকোনো একটা সত্যি হলেই চলবে |
| `not` | উল্টে দিন |

চলো একটা ছোট্ট উদাহরণ দিয়ে গরম হয়ে নিই।

**`examples/01_one_if.py`**

```python
rain = "yes"                    # we write the value ourselves

if rain == "yes":               # the question Python asks
    print("Take an umbrella.")  # runs when the answer is yes
else:
    print("No umbrella today.")

print("Now go outside.")        # outside the if, so it always runs
```

**আউটপুট:**

```
Take an umbrella.
Now go outside.
```

শেষ লাইনটা কেন সবসময় আসে? কারণ ওটা `if` এর ভেতরে নয়, বাইরে। সামনে কোনো স্পেস নেই।

---

## ১. Nested Condition — if এর ভেতরে if

### গল্পটা আগে শুনুন

আপনি চিড়িয়াখানার গেটে দাঁড়িয়ে আছেন। গেটম্যান প্রথমে জিজ্ঞেস করবে:

> **"টিকিট আছে?"**

টিকিট না থাকলে কথা এখানেই শেষ। ভেতরে ঢোকাই হবে না। বয়স কত, সেটা জানার আর দরকারই নেই।

কিন্তু টিকিট থাকলে সে আপনাকে ভেতরে ঢুকতে দেবে, আর **তারপর** দ্বিতীয় প্রশ্নটা করবে:

> **"আপনার বয়স কত? ১০ এর কম হলে একটা বেলুন ফ্রি!"**

খেয়াল করুন — দ্বিতীয় প্রশ্নটা প্রথম প্রশ্নের উত্তরের উপর নির্ভর করছে। প্রথমটার উত্তর "না" হলে দ্বিতীয় প্রশ্নটা করাই হয় না।

**এটাকেই বলে Nested Condition — একটা `if` এর ভেতরে আরেকটা `if`।**

### কোডে সেই গল্পটা

**`examples/02_if_inside_if.py`**

```python
ticket = "yes"
age = 8

if ticket == "yes":                        # outer question
    print("Ticket OK. Come in!")

    if age < 10:                           # inner question
        print("You get a free balloon!")
    else:
        print("Enjoy the zoo!")

else:
    print("Please buy a ticket first.")
```

**আউটপুট:**

```
Ticket OK. Come in!
You get a free balloon!
```

### সিঁড়ির মতো করে দেখুন

```
if বাইরের শর্ত:                    <-- ধাপ ১
    এই লাইনগুলো চলে বাইরেরটা সত্যি হলে
    if ভেতরের শর্ত:                <-- ধাপ ২
        এই লাইনগুলো চলে দুটোই সত্যি হলে
    else:
        বাইরেরটা সত্যি, ভেতরেরটা মিথ্যা
else:
    বাইরেরটা মিথ্যা — ভেতরের if টা Python পড়েই না
```

প্রতি ধাপে ৪টা স্পেস। PyCharm বা VS Code এ Tab চাপলে ৪টা স্পেস নিজে থেকেই বসে যায়।

> **নিজে চেষ্টা করুন:** ফাইলটায় `ticket = "no"` করে চালান। বেলুনের কথাটা কি আসে? আসে না — কারণ বাইরের প্রশ্নের উত্তরই "না" ছিল।

---

## ২. স্পেস কয়টা — সেটাই সব ঠিক করে দেয়

Python এ স্পেস শুধু সুন্দর দেখানোর জিনিস নয়। **স্পেসই বলে দেয় কোন লাইন কার ভেতরে আছে।**

একই চারটে লাইন, শুধু স্পেসের জায়গা বদলে দিলে প্রোগ্রাম দুরকম উত্তর দেয়।

**`examples/03_indentation_matters.py`**

```python
age = 10
money = 500

print("--- Version 1: the second if is INSIDE the first one ---")

if age >= 18:
    print("You are an adult.")
    if money >= 100:
        print("You can buy the ticket.")

print("--- Version 2: the second if is OUTSIDE ---")

if age >= 18:
    print("You are an adult.")
if money >= 100:
    print("You can buy the ticket.")
```

**আউটপুট:**

```
--- Version 1: the second if is INSIDE the first one ---
--- Version 2: the second if is OUTSIDE ---
You can buy the ticket.
```

কী হলো এখানে?

| | দ্বিতীয় `if` কোথায় | বয়স ১০ (১৮ এর কম) হলে | ফল |
|---|---|---|---|
| Version 1 | ভেতরে | বাইরের শর্ত মিথ্যা, তাই ভেতরে ঢোকাই হলো না | কিছুই ছাপা হলো না |
| Version 2 | বাইরে | দ্বিতীয় `if` একদম আলাদা, নিজের মতো চলল | টিকিটের লাইনটা ছাপা হলো |

---

## ৩. Nested if না-কি `and`? — কোনটা কখন

এই দুটো কোড একই কাজ করে বলে মনে হয়:

```python
if age >= 18 and nid == "yes":
    print("You can vote!")
```

```python
if age >= 18:
    if nid == "yes":
        print("You can vote!")
```

তাহলে পার্থক্যটা কোথায়? **পার্থক্য হলো, ব্যবহারকারী কী উত্তর পাবে সেখানে।**

| | `and` দিয়ে | Nested if দিয়ে |
|---|---|---|
| কখন ভালো | সব শর্ত মিলে **একটামাত্র** সিদ্ধান্ত | প্রতিটা শর্তের জন্য **আলাদা** মেসেজ |
| না মিললে | সবার জন্য একই মেসেজ | "বয়স হয়নি" আর "NID নেই" — আলাদা কারণ |
| কোড | ছোট, এক নজরে পড়া যায় | একটু বড়, কিন্তু বেশি সাহায্য করে |
| ইনপুট | সব ইনপুট আগেই নিতে হয় | দরকার হলে তবেই পরের ইনপুট নেওয়া যায় |

**দুটোই সঠিক।** প্রশ্নটা শুধু এটুকু — ব্যবহারকারী কোন উত্তরটা পেলে বেশি উপকৃত হবে?

### এবার input() দিয়ে

**`examples/04_nested_voting.py`**

```python
age = int(input("Enter your age: "))

if age >= 18:
    nid = input("Do you have an NID? (yes/no): ")

    if nid == "yes":
        print("You can vote!")
    else:
        print("Get your NID first, then you can vote.")

else:
    print("You are not 18 yet. Wait a few more years!")
```

**তিনটে রান, তিনটে আলাদা পথ:**

```
Enter your age: 20
Do you have an NID? (yes/no): yes
You can vote!
```

```
Enter your age: 20
Do you have an NID? (yes/no): no
Get your NID first, then you can vote.
```

```
Enter your age: 15
You are not 18 yet. Wait a few more years!
```

তৃতীয় রানে NID এর প্রশ্নটা **আসেইনি**। কারণ `input()` লাইনটা বাইরের `if` এর ভেতরে বসানো। বাইরের শর্ত মিথ্যা, তাই ওই লাইনটা Python ছুঁয়েও দেখেনি।

> **এটাই Nested if এর আসল সুবিধা** — অপ্রয়োজনীয় প্রশ্ন করাই হয় না।

---

## ৪. Truthy আর Falsy — খালি মানেই "না"

### আবার একটা গল্প

টিফিন বাক্স হাতে নিয়ে ঝাঁকালে যদি কোনো শব্দ না হয়, আপনি বুঝে যান বাক্সটা খালি। Python ও ঠিক এভাবেই ভাবে।

- **খালি জিনিস** মানে "না" → একে বলে **Falsy**
- **ভেতরে কিছু আছে** মানে "হ্যাঁ" → একে বলে **Truthy**

### তালিকাটা মুখস্থ নয়, বুঝে নিন

| Falsy (Python এর কাছে মিথ্যা) | কেন |
|---|---|
| `0` | শূন্য মানে কিছু নেই |
| `0.0` | দশমিকেও শূন্য মানে কিছু নেই |
| `""` | খালি লেখা, ভেতরে একটাও অক্ষর নেই |
| `False` | এ তো মিথ্যাই |
| `None` | মানে "কিছুই না" |

**Truthy:** উপরের পাঁচটা ছাড়া বাকি প্রায় সবকিছু। যেকোনো শূন্য-নয় সংখ্যা (`7`, `-3`, `3.14`), আর অক্ষরওয়ালা যেকোনো লেখা (`"hi"`, `"Rafi"`)।

### নিজের চোখে দেখে নিন

**`examples/05_truthy_falsy.py`**

```python
print("--- FALSY: Python reads these as False ---")
print("bool(0)      =", bool(0))
print("bool(0.0)    =", bool(0.0))
print('bool("")     =', bool(""))
print("bool(None)   =", bool(None))

print("--- TRUTHY: Python reads these as True ---")
print("bool(7)      =", bool(7))
print("bool(-3)     =", bool(-3))
print('bool("hi")   =', bool("hi"))
print('bool("0")    =', bool("0"))
```

**আউটপুট:**

```
--- FALSY: Python reads these as False ---
bool(0)      = False
bool(0.0)    = False
bool("")     = False
bool(None)   = False
--- TRUTHY: Python reads these as True ---
bool(7)      = True
bool(-3)     = True
bool("hi")   = True
bool("0")    = True
```

**সবচেয়ে মজার লাইনটা কোনটা? সবার শেষেরটা!**

`"0"` এর দুই পাশে কোটেশন চিহ্ন আছে। তাই এটা সংখ্যা শূন্য **নয়** — এটা একটা লেখা। আর লেখাটা খালি নয়, ভেতরে একটা অক্ষর আছে। তাই এটা **Truthy**।

### এবার কাজে লাগাই

আগে লিখতে হতো `if name != "":` — এখন শুধু `if name:` লিখলেই হবে। দুটোর মানে একই, কিন্তু দ্বিতীয়টা পড়তে সহজ।

**`examples/06_empty_name.py`**

```python
name = input("What is your name? ")

if name:
    print("Hello,", name)
else:
    print("You did not write anything!")
```

**দুটো রান:**

```
What is your name? Rafi
Hello, Rafi
```

```
What is your name?
You did not write anything!
```

দ্বিতীয় রানে কিছু না লিখেই শুধু Enter চাপা হয়েছে। তখন `name` এর ভেতরে ছিল `""` — খালি লেখা, অর্থাৎ Falsy।

> **মজার প্রশ্ন:** শুধু একটা স্পেস চেপে Enter দিলে কী হবে? উত্তর — `Hello,` আসবে! কারণ একটা স্পেসও একটা অক্ষর, তাই লেখাটা খালি নয়।

---

## ৫. দুটো শেখা একসাথে — ছোট্ট একটা Login

**`examples/07_login.py`**

```python
username = input("Username: ")

if username:
    password = input("Password: ")

    if password == "1234":
        print("Login successful! Welcome,", username)
    else:
        print("Wrong password!")

else:
    print("Username cannot be empty.")
```

এখানে আজকের দুটো জিনিসই একসাথে আছে:

- **বাইরের `if`** → Truthy/Falsy (নাম আদৌ লিখেছে তো?)
- **ভেতরের `if`** → সাধারণ তুলনা (পাসওয়ার্ড মিলল তো?)

**তিনটে পথ:**

| আপনি যা লিখলেন | কী হবে |
|---|---|
| `rafi` তারপর `1234` | `Login successful! Welcome, rafi` |
| `rafi` তারপর `abcd` | `Wrong password!` |
| কিছু না লিখে Enter | `Username cannot be empty.` — পাসওয়ার্ড **চাওয়াই হলো না** |

---

## ৬. ডিবাগিং — ভুল খুঁজে বের করার কৌশল

### প্রথমে মনের কথাটা

কোড চালানোর পর লাল লেখা দেখলে অনেকেই ভয় পেয়ে যায়। ভয়ের কিছু নেই।

> **Error মানে ব্যর্থতা নয়। Error হলো ঠিকানা।**

Python কখনো শুধু "ভুল হয়েছে" বলে না। সে বলে দেয় — কোন ফাইলে, কত নম্বর লাইনে, কী ধরনের ভুল। এ তো সাহায্য!

**নিয়ম:** লাল লেখার **সবার নিচের লাইনটা আগে পড়ুন।** সেখানেই ভুলের নাম আর কারণ লেখা থাকে।

### কৌশলটা: সন্দেহের জায়গায় print() বসান

**`examples/08_debug_print.py`**

```python
number = input("Type a number: ")

print("DEBUG 1:", number, type(number))       # what came from input()

number = int(number)                          # turn the text into a number

print("DEBUG 2:", number, type(number))       # what it became

if number == 10:
    print("Yes, it is 10!")
else:
    print("No, it is not 10.")
```

**আউটপুট (10 লিখলে):**

```
Type a number: 10
DEBUG 1: 10 <class 'str'>
DEBUG 2: 10 <class 'int'>
Yes, it is 10!
```

দুটো DEBUG লাইনে সংখ্যাটা হুবহু একই দেখাচ্ছে — `10` আর `10`। কিন্তু পাশের কথাটা আলাদা:

- `<class 'str'>` মানে **লেখা**
- `<class 'int'>` মানে **সংখ্যা**

এই পাশের কথাটাই আসল খবর। আর সেটাই `type()` দেখিয়ে দেয়।

### ডিবাগ করার ৩টি ধাপ

1. সন্দেহজনক লাইনের ঠিক আগে বসান: `print("DEBUG:", variable, type(variable))`
2. স্ক্রিনে যা দেখলেন, নিজের প্রত্যাশার সাথে মেলান — বেশিরভাগ ভুল এখানেই ধরা পড়ে
3. ভুল ঠিক হয়ে গেলে DEBUG লাইনগুলো **মুছে দিন** — ওগুলো আপনার জন্য, ব্যবহারকারীর জন্য নয়

---

## ৭. চারটে সাধারণ ভুল — আর তাদের আসল error message

### ভুল ১: Indentation

`if` লাইনের পরের লাইনটা ভেতরে না ঢোকালে কোড একদমই চলবে না।

```python
age = 20
if age >= 18:
print("You are eligible to vote.")
```

**Python যা বলবে:**

```
  File "err.py", line 3
    print("You are eligible to vote.")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
```

Tab আর Space মিশিয়ে ফেললেও একই সমস্যা হয়। যেকোনো একটা ব্যবহার করুন।

### ভুল ২: `=` আর `==` গুলিয়ে ফেলা

| চিহ্ন | মানে | কোথায় |
|---|---|---|
| `=` | ডান পাশের মানটা বাম পাশে **বসান** | ভ্যারিয়েবল বানানোর সময় |
| `==` | দুই পাশ **সমান কি না দেখুন** | `if` এর ভেতরে |

```python
x = 5
if x = 5:
    print("five")
```

**Python যা বলবে:**

```
  File "err.py", line 2
    if x = 5:
       ^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

দেখলে? Python নিজেই বলে দিচ্ছে `==` লিখতে হবে।

### ভুল ৩: ছোট হাতের আর বড় হাতের অক্ষর

`"Yes"` আর `"yes"` — Python এর কাছে এই দুটো **আলাদা** জিনিস।

ব্যবহারকারী কীভাবে টাইপ করবে আপনি সেটা ঠিক করে দিতে পারেন না। কেউ লিখবে `yes`, কেউ `Yes`, কেউ `YES`।

**সমাধান: `.lower()`** — এটা যেকোনো লেখাকে ছোট হাতের বানিয়ে দেয়। তুলনার ঠিক আগে একবার চালিয়ে নিন।

**`examples/09_case_lower.py`**

```python
answer = input("Do you like ice cream? (Yes/No): ")

print("DEBUG: you typed ->", answer)

if answer == "yes":
    print("Test 1 (no .lower()): Yummy!")
else:
    print("Test 1 (no .lower()): Oh, okay.")

if answer.lower() == "yes":
    print("Test 2 (with .lower()): Yummy!")
else:
    print("Test 2 (with .lower()): Oh, okay.")
```

**আউটপুট (`Yes` লিখলে — বড় হাতের Y দিয়ে):**

```
Do you like ice cream? (Yes/No): Yes
DEBUG: you typed -> Yes
Test 1 (no .lower()): Oh, okay.
Test 2 (with .lower()): Yummy!
```

**Test 1 ভুল উত্তর দিল।** অথচ কোনো লাল লেখা এলো না, কোনো error এলো না, প্রোগ্রাম দিব্যি চলল।

> এই ধরনের ভুলের নাম **নীরব ভুল (silent bug)**। Python ধরিয়ে দেয় না — আপনাকেই টেস্ট করে ধরতে হয়। তাই প্রতিটা প্রোগ্রাম কয়েকরকম ইনপুট দিয়ে চালিয়ে দেখতে হয়।

### ভুল ৪: Type mismatch

`input()` যা আনে সেটা **সবসময়** লেখা (string)। সংখ্যার সাথে তুলনা করার আগে `int()` বা `float()` দিয়ে বদলে নিতে হয়।

এই ভুলটা ধরার সবচেয়ে সহজ উপায় — `print()` এর সাথে `type()` বসিয়ে দেখা। ঠিক যেমন ০৮ নম্বর ফাইলে করেছি।

---

## ক্লাসের কাজ (Class Activity)

**লেন ক — সবার জন্য**

1. বয়স আর দেশের নাম (country) ইনপুট নিন
2. দেশ `"Bangladesh"` হলে ভোটের বয়স ১৮ ধরে চেক করুন
3. অন্য দেশ হলে আলাদা একটা মেসেজ দেখান
4. `and` নয়, **Nested if** দিয়ে লিখুন

**লেন খ — যাঁরা একটু এগিয়ে আছেন**

1. দেশের নামটা `.lower()` দিয়ে মেলান
2. দেশের নাম ফাঁকা থাকলে Truthy/Falsy দিয়ে ধরুন
3. ইচ্ছা করে indentation ভেঙে দিয়ে error message টা পড়ুন
4. প্রতিটা শাখা অন্তত একবার চালিয়ে টেস্ট করুন

> আটকে গেলে চ্যাটে লিখুন। পুরো কোড নয় — প্রথমে **error message** টা পাঠান।

---

## বাড়ির কাজ (Homework)

1. `examples/` ফোল্ডারের **নয়টা ফাইলই** চালান। প্রতিটার নিচে "Try it yourself" অংশটা আছে, সেগুলোও করুন।
2. নিজের একটা Login প্রোগ্রাম লিখুন:
   - username ফাঁকা হলে `"Username দিতে হবে"` দেখাবে (Truthy/Falsy দিয়ে)
   - username থাকলে password `"1234"` মিললে `"Login Successful"` দেখাবে (Nested if দিয়ে)
3. ইচ্ছা করে দুটো ভুল করুন — একবার indentation ভাঙুন, একবার `==` কে `=` করুন। দুটো error message খাতায় লিখে আনুন।
4. নিজের কোডে অন্তত একবার `print("DEBUG:", x, type(x))` বসিয়ে ভেতরে কী আছে দেখে নিন।

---

## নিজেকে যাচাই করুন

এই পাঁচটা প্রশ্নের উত্তর দিতে পারলে আজকের ক্লাস আপনার হয়ে গেছে।

1. বাইরের `if` এর শর্ত মিথ্যা হলে ভেতরের `if` টার কী হয়?
2. `if name:` — এই লাইনটার মানে বাংলায় কী?
3. `bool("0")` এর উত্তর `True` না `False`? কেন?
4. `=` আর `==` এর পার্থক্য এক লাইনে বলুন।
5. "নীরব ভুল" মানে কী? একটা উদাহরণ দিন।

<details>
<summary>উত্তর দেখতে এখানে ক্লিক করুন</summary>

1. Python ভেতরের `if` টা পড়েই না — একদম লাফ দিয়ে `else` এ চলে যায়
2. "name খালি নয় তো?"
3. `True` — কারণ কোটেশনের ভেতরে থাকায় এটা সংখ্যা শূন্য নয়, একটা অক্ষরওয়ালা লেখা
4. `=` মান বসায়, `==` মান মেলায়
5. যে ভুলে কোনো error আসে না, প্রোগ্রাম চলে, কিন্তু উত্তরটা ভুল — যেমন `.lower()` ছাড়া `"Yes" == "yes"` মেলানো

</details>

---

## আজকের সারাংশ

| ধারণা | এক লাইনে |
|---|---|
| Nested if | একটা শর্তের ভেতরে আরেকটা; বাইরেরটা মিথ্যা হলে ভেতরেরটা চলেই না |
| Nested if না `and` | আলাদা মেসেজ দরকার হলে Nested if, একটামাত্র সিদ্ধান্ত হলে `and` |
| Indentation | স্পেসই বলে দেয় কোন লাইন কার ভেতরে |
| Falsy | `0`, `0.0`, `""`, `False`, `None` |
| Truthy | বাকি প্রায় সবকিছু |
| `if name:` | "name খালি নয় তো?" |
| ডিবাগিং | `print()` + `type()` বসান, দেখুন, ঠিক করুন, তারপর মুছে দিন |
| Error message | শত্রু নয় — বন্ধু। নিচের লাইনটা আগে পড়ুন |

---

## পরবর্তী ক্লাস

**Live Class 06: Mini Project — Grade Evaluator ও Age Checker**

আজ পর্যন্ত শেখা সবগুলো টুকরো জুড়ে আমরা সত্যিকারের ছোট প্রোগ্রাম বানাব। নতুন কোনো সিনট্যাক্স নেই — শুধু বানানো।
