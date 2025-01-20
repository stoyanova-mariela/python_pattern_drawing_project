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

    elif choice == 'end':
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