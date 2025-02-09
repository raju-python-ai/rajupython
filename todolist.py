def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add? "))
            for i in range(n_tasks):
                task = input(f"Enter task {i + 1}: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")
        
        elif choice == '2':
            print("\nTasks:")
            if not tasks:
                print("No tasks available.")
            else:
                for index, task in enumerate(tasks): 
                    status = "Done" if task['done'] else "Not done"
                    print(f"{index + 1}. {task['task']} - {status}")
        
        elif choice == '3':
            if not tasks:
                print("No tasks available to mark as completed.")
            else:
                task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True  
                    print("Task marked as done!")
                else:
                    print("Invalid task number.")
        
        elif choice == '4':
            print("Exiting To-Do List App... GOODBYE!")
            break
        
        else:
            print("Invalid choice. Please try again.")

main()
