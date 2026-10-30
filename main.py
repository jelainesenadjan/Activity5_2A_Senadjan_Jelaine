from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

print("FUNDAMENTAL DATA STRUCTURES")
print("1. Array Stack")
print("2. Linked List Stack")
print("3. Circular Array Queue")
print("4. Linked List Queue")

choice = int(input("Choose implementation: "))

if choice == 1:
    structure = ArrayStack(5)
    kind = "stack"

elif choice == 2:
    structure = LinkedStack()
    kind = "stack"

elif choice == 3:
    structure = ArrayQueue(5)
    kind = "queue"

elif choice == 4:
    structure = LinkedQueue()
    kind = "queue"

else:
    print("Invalid choice")
    exit()

while True:
    print("\n1. Insert")
    print("2. Remove")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Check if Full")
    print("6. Display")
    print("7. Exit")

    operation = input("Choose operation: ")

    try:
        if operation == "1":
            value = input("Enter value: ")

            if kind == "stack":
                structure.push(value)
            else:
                structure.enqueue(value)

            print("Value inserted successfully.")

        elif operation == "2":
            if kind == "stack":
                print("Removed:", structure.pop())
            else:
                print("Removed:", structure.dequeue())

        elif operation == "3":
            if kind == "stack":
                print("Top element:", structure.peek())
            else:
                print("Front element:", structure.peek_front())

        elif operation == "4":
            print("Is empty:", structure.is_empty())

        elif operation == "5":
            if kind == "stack" or kind == "queue":
                if hasattr(structure, "is_full"):
                    print("Is full:", structure.is_full())
                else:
                    print("Not applicable.")

        elif operation == "6":
            print("Current elements:", structure.display())

        elif operation == "7":
            print("Program ended.")
            break

        else:
            print("Invalid operation.")

    except (IndexError, OverflowError) as error:
        print("Error:", error)