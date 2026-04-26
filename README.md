# Library Management System — Python Project 3

A menu-driven Library Management System built in Python. Supports adding books, issuing them to students, returning them, and calculating overdue fines automatically.

---

## Project Structure

```
library_management/
├── main.py       # All logic and entry point
└── README.md
```

---

## How to Run

Make sure Python 3 is installed, then run:

```bash
python main.py
```

No external libraries required. Only the built-in `datetime` module is used.

---

## Features

| Feature | Description |
|---|---|
| Add Book | Add a new book or restock an existing one by Book ID |
| View Books | Display all books with availability count |
| Issue Book | Issue a book to a student with a custom due date |
| Return Book | Return a book and auto-calculate fine if overdue |
| View History | Full log of all issued and returned books with fines |

---

## How It Works

### Data Storage
Two dictionaries hold all data in memory during runtime:
- `books` — stores book details and available quantity
- `issued_books` — stores every issue record with status and fine

### Issue Logic
- Each issue generates a unique Issue ID (`bookID_serialNumber`)
- Due date is calculated using `datetime.now() + timedelta(days=n)`
- Book quantity is decremented on issue, restored on return

### Fine Calculation
Fines are calculated on a **weekly escalating rate**:

| Week Overdue | Daily Rate |
|---|---|
| Week 1 | ₹10/day |
| Week 2 | ₹20/day |
| Week 3 | ₹60/day |
| Week 4+ | Continues to multiply |

The longer the delay, the higher the daily rate — incentivising early returns.

### Return Logic
- Looks up the Issue ID from active records
- Compares return date to due date using `timedelta`
- If overdue: calculates and displays fine
- If on time: confirms no fine

---

## Concepts Used

| Concept | Where |
|---|---|
| `datetime` / `timedelta` | Issue date, due date, overdue calculation |
| Nested dictionaries | `books` and `issued_books` data stores |
| Functions | Each feature is a separate function |
| `while True` loop | Keeps the menu running until user exits |
| f-strings | All formatted output |
| Escalating `while` loop | Fine calculation logic |

---

## Sample Output

```
==================================================
LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add Book
2. View All Books
3. Issue Book
4. Return Book
5. View History
6. Exit
==================================================

Enter your choice (1-6): 3

--- ISSUE BOOK ---
Book ID    Title                     Author          Available
============================================================
B001       Python Basics             Saurav          3

Enter Book ID to issue: B001
Enter Student Name: Rahul
Enter number of days to issue book for: 7

✓ Book issued successfully!
Book: Python Basics
Student: Rahul
Issue Date: 2026-04-26
Due Date: 2026-05-03
Issue ID: B001_1
```

---

## Known Limitations

- Data is not saved to a file — all records reset when the program exits
- No login or admin authentication
- Book ID must be remembered by the user; no search feature

---

## Author

**Saurav**
B.Tech CSE — Chandigarh Engineering College (CGC)
Semester 2 — Python Programming Lab
