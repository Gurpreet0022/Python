def display_menu():
    print("Menu:")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Remove a task")
    print("4.Exit")
    
def add_tasks(tasks):
    task=input("Enter a new task:")
    tasks.append(task)
    print("Task added successfully.")
    
def view_tasks(tasks):
    if tasks:
        print("Your tasks:")
        for idx,task in enumerate(tasks,1):
            print(f"{idx}.{task}")
    else:
        print("No task added yet.")
        
def remove_tasks(tasks):
    view_tasks(tasks)
    task_num=int(input("Enter the task number to remove:"))-1
    if 0 <=task_num < len(tasks):
        removed_task=tasks.pop(task_num)
        print(f"Removed task:{remove_tasks}")
    else :
        print("Invalid task number.")
        
def main():
    tasks=[]
    
    while True:
       display_menu()
       choice=input("Enter your choice:")
       
       if choice=="1":
           add_tasks(tasks)
       elif choice=="2":
           view_tasks(tasks)
       elif choice =="3":
           remove_tasks(tasks)
       elif choice=="4":
           print("Goodbye!")
           break
       else:
           print("Invalid choice. Please try again.") 
           
main()                      
       
                       
                            
    