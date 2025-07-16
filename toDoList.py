

def main():

    print("Welcome to your to-do list!")
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Read tasks")
    print("3. Delete a task")
    print("4. Update a task")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        time = input("Enter the time: ")
        date = input("Enter the date: ")

        addtasks(task, time, date)
    elif choice == "2":
        readtasks()
    elif choice == "3":
        deletetasks()
    elif choice == "4":
        updatetasks()
    else:
        print("Invalid choice. Please try again.")
    
   





def addtasks(task, time, date):
    with open('tasks.txt', 'a') as file:
        file.write(f"{task} - {time} - {date}\n")


def readtasks():

    with open('tasks.txt', 'r') as file:
       tasks = file.readlines()
    for task in tasks:
        print(task.strip())

def deletetasks():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

    print("Which task would you like to delete?")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task.strip()}")

    choice = int(input("Enter the number of the task you want to delete: "))
    tasks.pop(choice-1)

    with open('tasks.txt', 'w') as file:
        file.writelines(tasks)

def updatetasks():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()

    print("Which task would you like to update?")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task.strip()}")

    choice = int(input("Enter the number of the task you want to update: "))
    task = input("Enter the new task: ")
    time = input("Enter the new time: ")
    date = input("Enter the new date: ")

    try:
        tasks[choice-1] = f"{task} - {time} - {date}\n"
    
    except IndexError:
        print("task doesn't exist. Please try again.")

    with open('tasks.txt', 'w') as file:
        file.writelines(tasks)

if __name__ == '__main__':
    main()