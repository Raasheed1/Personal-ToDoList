import json
from datetime import date, datetime, date
print("======TO.DO.LIST============")
FILE_PATH = "tasks.json"
# Load existing tasks
Task = []
try:
    with open(FILE_PATH, "r") as f:
        data = json.load(f)
        for t in data:
            t["Due_Date"] = datetime.strptime(t["Due_Date"], "%Y-%m-%d").date()
        Task = data
except FileNotFoundError:
    Task = []
except json.JSONDecodeError:
    print("Error reading existing task file, starting fresh.")
    Task = []

def save_to_file():
    try:
        with open(FILE_PATH, "w") as f:
            json.dump(  #convert it into jason formate
                [
                    {
                        "New_Task": t["New_Task"],
                        "Description": t.get("Description", ""),
                        "Category": t.get("Category", "General"),
                        "Due_Date": t["Due_Date"].strftime("%Y-%m-%d"),
                        "Status": t["Status"]
                    }
                    for t in Task
                ],
                f,
                indent=4
            )
    except Exception as e:
        print(f"Error saving file: {e}")

#to add a new Task
def new_task_add():
    addTask = {}
    addTask["New_Task"] = input("Enter your new Task: ")
    addTask["Description"] = input("Enter task description: ")
    print("=======>Task Category <=======\n1.Work\n2.Personal\n3.Urgent ")
    category=int(input("Enter the category Number :"))
    if category==1:
        addTask["Category"] = "Work"
    elif category==2:
        addTask["Category"] = "Personal"
    else:
        addTask["Category"] = "Urgent"        
    while True:
        try:
            DueDate = input("Enter the Due Date (YYYY-MM-DD): ")
            dueDate = datetime.strptime(DueDate, "%Y-%m-%d").date()
            addTask["Due_Date"] = dueDate
            break
        except ValueError:
            print("Invalid date format. Enter as given format (YYYY-MM-DD).")
            continue

    addTask["Status"] = False
    Task.append(addTask)
    save_to_file()
    print("Task successfully Added\n")

#To view all task    
def view_all_Task():
    for i, View in enumerate(Task, start=1):
                    print(f"{i}. Task: {View['New_Task']} | Category: {View.get('Category', 'General')}")
                    print(f"   Description: {View['Description']}")
                    print(f"   Due Date: {View['Due_Date']}")
                    print("   Status:", "Completed" if View["Status"] else "Not completed")
                    print() 

#To view Priority Task
def view_piro_task():
    print("===> PRIORITY <===")
    for i, View in enumerate(Task, start=1):
        days_left = (View["Due_Date"] - date.today()).days
        if days_left <= 3:
            print("!!! High priority !!!")
            print(f"Task end in {days_left} day(s)")
        else:
            print(f"Task name: {View['New_Task']}, due in {days_left} days.")
        print()

#To view pending Task
def view_pending_task():  
    print("===> Pending Tasks <===")
    for i, View in enumerate(Task, start=1):
        if not View["Status"]:
            print(f"{i}. Task: {View['New_Task']}, Due Date: {View['Due_Date']}")
            print()      

#Mark the task
def mark_as_complete():
    print("Select the Task number")
    for i, Tasks in enumerate(Task, start=1):
        print(i, Tasks["New_Task"])
    while True:    
        try:
            chose = int(input("Enter the task number: "))
            if 1 <= chose <= len(Task):
                Task[chose - 1]["Status"] = True
                save_to_file()
                print("Task marked as completed")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")
            continue

#to edit the task
def edit_all_task():
    print("==> Select the task number <==")
    for i, tasks in enumerate(Task, start=1):
        print(f"{i}. Task: {tasks['New_Task']}")
    try:
        choose = int(input("Enter the task number: "))
        if 1 <= choose <= len(Task):
            Task[choose - 1]["New_Task"] = input("Enter new task name: ")
            Task[choose - 1]["Description"] = input("Enter new description: ")
            Task[choose - 1]["Category"] = input("Enter new category: ")
            while True:
                try:
                    update_date = input("Enter new Due Date (YYYY-MM-DD): ")
                    alter_date = datetime.strptime(update_date, "%Y-%m-%d").date()
                    Task[choose - 1]["Due_Date"] = alter_date
                    break
                except ValueError:
                    print("Invalid date format.")
                    continue
            save_to_file()
            print("Task successfully updated\n")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

#to delet the task
def delet_task():
    print("Select the task number")
    for i, Tasks in enumerate(Task, start=1):
        print(i, Tasks["New_Task"])
    while True:    
        try:
            num = int(input("Enter task number: "))
            if 1 <= num <= len(Task):
                del Task[num - 1]
                save_to_file()
                print("Task deleted successfully")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")
            continue

#Main Body of the Code
while True:
    print("Enter your needed operation")
    print("1.Add new Task\n2.View all task\n3.Mark the completed task\n4.Edit or Delete task\n5.Exit")
    try:
        user_interface = int(input("Select the Operation: "))
    except ValueError:
        print("=> Enter only number <=")
        continue

    match user_interface:
        case 1:
            new_task_add()
        case 2:
            if not Task:
                print("No task added")
            else:
                view_all_Task()
                view_piro_task()
                view_pending_task()
                
        case 3:
            if not Task:
                print("No tasks to mark completed")
            else:
                mark_as_complete()

        case 4:
            print("1.Edit / 2.Delete")
            try:
                choose = int(input("Enter your choice: "))
            except ValueError:
                print("Enter 1 or 2 only.")
                continue
            match choose:
                case 1:
                    if not Task:
                        print("No tasks here.")
                    else:
                        edit_all_task()

                case 2:
                    if not Task:
                        print("No tasks here.")
                    else:
                        delet_task()

        case 5:
            print("Exiting... Goodbye!")
            break

        case _:
            print("Invalid option, please choose between 1 to 5.")
