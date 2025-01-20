# Python Pattern Drawing Project
Welcome to my project! This Python project is designed to work with nested loops, conditional statements and varying user inputs in order to create unique patterns in the output console.

---

## Project Overview:
The main purpose of this project is to create various **patterns** using Python's printing capabilities. In this program users can choose from different patterns, provide necessary inputs, and see the results displayed in the terminal.

## Objectives:
- Working with **nested loops**.
- Using **if-elif-else conditions** to implement logic.
- Handling **user input** to create dynamic patterns.
- Understanding **alignment** using spaces and characters.

## Implemented patterns:
1) **Right-angled Triangle**  
```
*
**
***
****
*****
```

2) **Square with Hollow Center**  
```
*****
*   *
*   *
*   *
*****
```

3) **Diamond**  
```
  *
 ***
*****
 ***
  *
```

4) **Left-angled Triangle**  
```
****
***
**
*
```

5) **Hollow Square**  
```
******
*    *
*    *
*    *
*    *
******
```

6) **Pyramid**  
```
   *
  ***
 *****
*******
```

7) **Reverse Pyramid** 
```
*******
 *****
  ***
   *
```

8) **Rectangle with Hollow Center**  
```
********
*      *
*      *
********
```

---

## User Instructions:

1) **Run the Program**  
Start the program and choose a pattern from the menu.  

2) **Input Dimensions**  
Provide necessary inputs (e.g., number of rows or size of the shape).  

3) **See the Result**  
Enjoy the output directly in your terminal.  

4) **Try Again!**  
You can run the program again to explore different patterns.

---

## Python Code:

Below is the **code** with comments that guide through the project activities. 

```python
print("Welcome to the Python Pattern Drawing Program!")
print("\nChoose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")
print("*  (Type command \"end\" to end the program)")

while True:
    choice = input("\nEnter the number corresponding to your choice: ")

    if choice in ['1', '3', '4', '6', '7']:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in ['2', '5']:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))

    if choice == '1':  # Right-angled Triangle
        for i in range(1, rows+1):
            print('*' * i)

    elif choice == '2':  # Square with Hollow Center
        for i in range(1, size+1):
            if i == 1 or i == size:
                print('*' * size)
            else:
                print('*' + (' ' * (size - 2)) + '*')

    elif choice == '3':  # Diamond
        mid = rows // 2

        for i in range(rows):
            if i < mid:
                stars = 2 * i + 1
            else:
                stars = 2 * (rows - i - 1) + 1

            spaces = (rows - stars) // 2
            print(" " * spaces + "*" * stars + " " * spaces)

    elif choice == '4':  # Left-angled Triangle
        for i in range(rows, -1, -1):
            print('*' * i)

    elif choice == '5':  # Hollow Square
        for i in range(1, size + 3):
            if i == 1 or i == size + 2:
                print('*' * (size + 2))
            else:
                print('*' + (' ' * size) + '*')

    elif choice == '6':  # Pyramid
        for i in range(rows):
            for j in range(rows - i - 1):
                print(' ', end='')
            for k in range(2 * i + 1):
                print('*', end='')
            print()

    elif choice == '7':  # Reverse Pyramid
        for i in range(rows, 0, -1):
            for j in range(rows - i):
                print(' ', end='')
            for k in range(2 * i - 1):
                print('*', end='')
            print()

    elif choice == '8':  # Rectangle with Hollow Center
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        for i in range(1, height + 1):
            if i == 1 or i == height:
                print('*' * width)
            else:
                print('*' + (' ' * (width - 2)) + '*')

    elif choice == 'end':  # Ends the program
        print('Goodbye! ')
        break

    else:
        print("Invalid choice! Please restart the program with command \"restart\": ", end='')
        option = input()
        while option != 'restart':
            print('Invalid command! Enter again:', end=' ')
            option = input();
        else:
            continue
```
