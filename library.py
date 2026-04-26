from datetime import datetime, timedelta

# Dictionary to store books
books = {}

# Dictionary to store issued books
issued_books = {}

def add_book():
    """Add a new book to library"""
    print("\n--- ADD BOOK ---")
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    quantity = int(input("Enter Quantity: ").strip())

    if book_id in books:
        books[book_id]['quantity'] += quantity
    else:
        books[book_id] = {
            'title': title,
            'author': author,
            'quantity': quantity
        }
    print(f"✓ Book '{title}' added successfully!")

def view_books():
    """Display all books in library"""
    if not books:
        print("\n⚠ No books in library!")
        return

    print("\n" + "="*60)
    print(f"{'Book ID':<10} {'Title':<25} {'Author':<15} {'Available':<10}")
    print("="*60)
    for bid, details in books.items():
        print(f"{bid:<10} {details['title']:<25} {details['author']:<15} {details['quantity']:<10}")
    print("="*60)

def issue_book():
    """Issue a book to a student"""
    print("\n--- ISSUE BOOK ---")
    view_books()

    book_id = input("\nEnter Book ID to issue: ").strip()

    if book_id not in books:
        print("✗ Book not found!")
        return

    if books[book_id]['quantity'] <= 0:
        print("✗ Book not available!")
        return

    student_name = input("Enter Student Name: ").strip()
    days = int(input("Enter number of days to issue book for: ").strip())

    # Deduct from quantity
    books[book_id]['quantity'] -= 1

    # Record issue
    issue_id = f"{book_id}_{len(issued_books) + 1}"
    issue_date = datetime.now()
    due_date = issue_date + timedelta(days=days)

    issued_books[issue_id] = {
        'book_id': book_id,
        'book_title': books[book_id]['title'],
        'student_name': student_name,
        'issue_date': issue_date,
        'due_date': due_date,
        'days_allowed': days,
        'status': 'issued'
    }

    print(f"\n✓ Book issued successfully!")
    print(f"Book: {books[book_id]['title']}")
    print(f"Student: {student_name}")
    print(f"Issue Date: {issue_date.strftime('%Y-%m-%d')}")
    print(f"Due Date: {due_date.strftime('%Y-%m-%d')}")
    print(f"Issue ID: {issue_id}")

def return_book():
    """Return a book and calculate fine if overdue"""
    print("\n--- RETURN BOOK ---")

    if not issued_books:
        print("✗ No issued books!")
        return

    print("\nCurrently Issued Books:")
    print("="*60)
    for iid, record in issued_books.items():
        if record['status'] == 'issued':
            print(f"{iid} | {record['book_title']} | {record['student_name']}")
    print("="*60)

    issue_id = input("\nEnter Issue ID to return: ").strip()

    if issue_id not in issued_books:
        print("✗ Invalid Issue ID!")
        return

    record = issued_books[issue_id]

    if record['status'] == 'returned':
        print("✗ Book already returned!")
        return

    return_date = datetime.now()
    days_overdue = (return_date - record['due_date']).days

    # Restore book quantity
    books[record['book_id']]['quantity'] += 1

    # Update status
    record['status'] = 'returned'
    record['return_date'] = return_date

    print(f"\n✓ Book returned successfully!")
    print(f"Book: {record['book_title']}")
    print(f"Student: {record['student_name']}")
    print(f"Return Date: {return_date.strftime('%Y-%m-%d')}")
    print(f"Due Date: {record['due_date'].strftime('%Y-%m-%d')}")

    # Calculate fine if overdue
    if days_overdue > 0:
        fine = 0
        week = 1
        remaining_days = days_overdue

        while remaining_days > 0:
            days_in_this_week = min(remaining_days, 7)

            # Calculate multiplier: Week 1 = 10, Week 2 = 20, Week 3 = 60, etc.
            multiplier = 1
            for i in range(1, week + 1):
                multiplier *= i

            daily_rate = 10 * multiplier
            fine += days_in_this_week * daily_rate

            remaining_days -= days_in_this_week
            week += 1

        record['fine'] = fine
        print(f"\n⚠ BOOK OVERDUE!")
        print(f"Days Overdue: {days_overdue}")
        print(f"Fine: ₹{fine}")
    else:
        record['fine'] = 0
        print(f"\n✓ No fine - Book returned on time!")

def view_history():
    """View all issued and returned books"""
    if not issued_books:
        print("\n⚠ No history!")
        return

    print("\n" + "="*80)
    print(f"{'Issue ID':<15} {'Book':<20} {'Student':<15} {'Status':<10} {'Fine (₹)':<10}")
    print("="*80)
    for iid, record in issued_books.items():
        fine = record.get('fine', 0)
        print(f"{iid:<15} {record['book_title']:<20} {record['student_name']:<15} {record['status']:<10} {fine:<10}")
    print("="*80)

def show_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. View All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View History")
    print("6. Exit")
    print("="*50)

# Main program
while True:
    show_menu()
    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        view_history()
    elif choice == '6':
        print("\nThank you for using Library Management System!")
        break
    else:
        print("\n✗ Invalid choice! Try again.")
