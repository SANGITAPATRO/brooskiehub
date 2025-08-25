#!/usr/bin/env python3
"""
Colorful CLI Calculator with history logging
Author: Sangita Kankal
"""

from colorama import init, Fore, Style
import pyfiglet

# Initialize colorama
init(autoreset=True)

HISTORY_FILE = "calc_history.txt"

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x: float, y: float) -> float:
    return x ** y

def log_history(entry: str):
    with open(HISTORY_FILE, "a") as file:
        file.write(entry + "\n")

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            content = file.read()
            print(Fore.YELLOW + "\nCalculation History:\n")
            print(content if content else "No history yet.")
    except FileNotFoundError:
        print("No history file found.")

def main():
    title = pyfiglet.figlet_format("CLI Calculator")
    print(Fore.CYAN + title)

    while True:
        print(Fore.GREEN + """
Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (^)
6. View History
7. Exit
""")

        choice = input(Fore.YELLOW + "Enter choice (1-7): ")

        if choice == "7":
            print(Fore.CYAN + "Goodbye! 👋")
            break
        elif choice == "6":
            show_history()
            continue
        elif choice in {"1", "2", "3", "4", "5"}:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = add(num1, num2)
                    operator = "+"
                elif choice == "2":
                    result = subtract(num1, num2)
                    operator = "-"
                elif choice == "3":
                    result = multiply(num1, num2)
                    operator = "*"
                elif choice == "4":
                    result = divide(num1, num2)
                    operator = "/"
                elif choice == "5":
                    result = power(num1, num2)
                    operator = "^"
                print(Fore.MAGENTA + f"\nResult: {num1} {operator} {num2} = {result}\n")
                log_history(f"{num1} {operator} {num2} = {result}")

            except ValueError as e:
                print(Fore.RED + f"Error: {e}")
        else:
            print(Fore.RED + "Invalid choice! Please select from 1 to 7.")

if __name__ == "__main__":
    main()