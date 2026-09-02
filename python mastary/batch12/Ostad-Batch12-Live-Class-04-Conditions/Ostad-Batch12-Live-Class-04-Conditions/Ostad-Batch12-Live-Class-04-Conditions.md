# Ostad Batch 12 — Live Class 04
## Module 2: Logic & Condition Building
### Topic: if, else, elif, Logical Operators (and, or, not)

---

## ভূমিকা (Recap)

Module 1-এ আমরা শিখেছি:
- `print()`, `input()`
- Variables ও Data Types (`int`, `float`, `str`, `bool`)
- Type conversion, `type()`, `id()`

আজ থেকে আমরা প্রোগ্রামকে **সিদ্ধান্ত নিতে** শেখাবো — অর্থাৎ, কোনো শর্ত (condition) সত্যি হলে এক কাজ, মিথ্যা হলে আরেক কাজ।

---

## ১. `if` স্টেটমেন্ট

প্রোগ্রামে কোনো শর্ত true হলেই শুধু একটা ব্লক কোড রান হবে — এটাই `if` এর কাজ।

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
```

**গুরুত্বপূর্ণ:** Python-এ `{}` ব্র্যাকেট নেই, ব্লক বোঝাতে **indentation (স্পেস)** ব্যবহার হয়। এটা ভুল করলে `IndentationError` আসবে।

---

## ২. `if-else`

শর্ত মিথ্যা হলে কী হবে সেটাও বলে দেওয়া যায়।

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("This is an Even number")
else:
    print("This is an Odd number")
```

---

## ৩. `if-elif-else`

একাধিক শর্ত যাচাই করতে হলে `elif` (else if) ব্যবহার করি।

```python
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A+")
elif marks >= 60:
    print("Grade: A")
elif marks >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")
```

Python উপর থেকে নিচে শর্তগুলো একে একে চেক করে, যেই শর্ত প্রথম সত্যি হয় সেটার ব্লক রান করে বাকিগুলো বাদ দিয়ে দেয়।

---

## ৪. Comparison Operators (Recap + New)

| Operator | অর্থ |
|---|---|
| `==` | সমান |
| `!=` | সমান না |
| `>` | বড় |
| `<` | ছোট |
| `>=` | বড় বা সমান |
| `<=` | ছোট বা সমান |

⚠️ সাধারণ ভুল: `=` (assignment) আর `==` (comparison) গুলিয়ে ফেলা।

---

## ৫. Logical Operators: `and`, `or`, `not`

একের অধিক শর্ত একসাথে চেক করার জন্য।

```python
age = int(input("Enter your age: "))
has_id_card = input("Do you have an NID? (yes/no): ")

if age >= 18 and has_id_card == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

- `and` → দুটো শর্তই সত্যি হতে হবে
- `or` → যেকোনো একটি সত্যি হলেই চলবে
- `not` → শর্তকে উল্টে দেয় (True → False)

```python
is_raining = True

if not is_raining:
    print("You can go outside.")
else:
    print("Stay home, it's raining.")
```

---

## Class Activity

1. একটি বছর নিয়ে চেক করো সেটি Leap Year কিনা (`%` operator + `and`/`or` ব্যবহার করে)।
2. তিনটি সংখ্যার মধ্যে সবচেয়ে বড়টি বের করো `if-elif-else` দিয়ে।

## Homework

`examples/` ফোল্ডারে থাকা প্রতিটি ফাইল রান করে দেখো এবং নিজে নিজে ভ্যালু বদলে টেস্ট করো। এরপর নিচের প্রোগ্রামটি লেখো:
- ইউজারের কাছ থেকে ৩টি বিষয়ের নম্বর নিয়ে গড় (average) বের করো এবং গড়ের ভিত্তিতে গ্রেড দেখাও।

## পরবর্তী ক্লাস

Live Class 05: Nested Conditions, Truthy/Falsy Values, Debugging
