# =====Importing Libraries===========
from datetime import datetime


# ====Functions====
# Login Functions


def login():
    # This function creates a dictionary of usernames and passwords, then
    # prompt the user to enter their username/password before checking
    # them against the values in the dictionary
    user_dict = {}
    with open("user.txt", "r") as user_file:
        for line in user_file:
            line = line.split(", ")
            user_dict[line[0]] = line[1]
    while True:
        user = input("Username: ")
        if user in user_dict:
            break
        else:
            print("Username not recognised, please try again.\n")
    while True:
        password = input("Password: ")
        if password == user_dict[user].strip("\n"):
            print("Login Successful")
            break
        else:
            print("Password incorrect, please try again.\n")
    return user


# Menu Functions

def reg_user():
    # Creates a new user with specified username/password
    if username == "admin":

        # admin chooses a username for new user, will reject username if
        # already in user.txt file
        print("\nYou have chosen to create a new user account.\n")
        user_exists = True
        new_username = ""
        new_password = ""
        while user_exists:
            new_username = input("Please choose a username for the new user: ")
            with open("user.txt", "r") as details:
                user_list = []
                for i in details:
                    i_split = i.split(", ")
                    user_list.append(i_split[0])
                if new_username not in user_list:
                    user_exists = False
                else:
                    print("\nThis username already exists, please enter a new one.\n")

        # admin enters and confirms a password for new user
        password_confirmed = False
        while not password_confirmed:
            new_password = input(f"Please choose a password for {new_username}: ")
            password_reenter = input("Please confirm the password: ")
            if new_password == password_reenter:
                password_confirmed = True
            else:
                print("The entered passwords don't match, please try again.")

        # New user credentials are written to the user.txt file and confirmation message printed
        with open("user.txt", "a") as details:
            details.write("\n" + f"{new_username}, {new_password}")
        print(f"\nUser account \"{new_username}\" created," +
              "please try signing in with the new credentials to confirm.\n\n")

    # This returns non admin accounts to menu with message
    else:
        print("\n\nThe user registration function is restricted to the admin account.\n\n")


def add_task():
    # User enters details of task to be written to file, task_confirmed
    # boolean prevents unverified details being written
    print("\nYou have chosen to add a task to the manager.\n")
    task_confirmed = False
    task_title = ""
    task_user = ""
    task_desc = ""
    task_start = ""
    task_due = ""
    while not task_confirmed:

        # Asks user to choose a username to assign the task to and confirms
        # that it is a valid username
        task_user = user_exists_task(input("Please choose a user to set a task for: "))

        # Asks user to input the title, description and due date of the task.
        # Current date also defined.
        task_title = input("Please enter a title for the task: ")
        task_desc = input("Please describe the task: ")
        current_date = datetime.now()
        task_start = current_date.strftime("%d %b %Y")
        task_due = input("Please enter a due date for the task (Formatted 1 Jan 2000): ")

        # User confirms that details entered are all correct prior to file being written
        print(80 * "_" + f'''\n
    Task:                    {task_title}
    Assigned to:             {task_user}
    Due Date:                {task_due}
    Start Date:              {task_start}

    Task Description:
    {task_desc}\n''' + 80 * "_" + "\n")
        task_correct = ""
        while task_correct != "y" and task_correct != "n":
            task_correct = input("Are the details of the task above correct? (y/n): ")
            if task_correct == "y":
                task_confirmed = True
            elif task_correct == "n":
                print("\nTask details not confirmed, please re-enter the details for the task.\n")
                break
            else:
                print("Please choose a valid response (y/n)\n")

    # This formats and writes the confirmed task details to the tasks.txt file
    # Commas temporarily replaced with ":.:" in the task description/titles,
    # as they are used as delimiters when reading files
    task_title = task_title.replace(",", ":.:")
    task_desc = task_desc.replace(",", ":.:")
    task_final = f"{task_user}, {task_title}, {task_desc}, {task_start}, {task_due}, No"
    with open("tasks.txt", "a") as task_file:
        task_file.write("\n" + task_final)
    print("Task has been added to manager.\n\n")


def user_exists_task(user):
    # This function checks a user exists when editing or adding tasks
    user_exists = False
    while not user_exists:
        with open("user.txt", "r") as details:
            user_list = []
            for i in details:
                i_split = i.split(", ")
                user_list.append(i_split[0])
            if user in user_list:
                user_exists = True
            else:
                user = input("\nThis user doesn't exist, please enter a valid username: ")
    return user


def view_all():
    # Opens tasks.txt and copies each line to "line" list then prints task.
    # Commas are reintroduced during print step
    print("\nYou have chosen to view all tasks.\n")
    with open("tasks.txt", "r") as tasks:
        line_count = -1
        for line_string in tasks:
            line_count += 1
            line = line_string.split(", ")
            print(80 * "_" + f'''\n
    Task:                    {line[1].replace(":.:", ",")}
    TaskID:                  {line_count}
    Assigned to:             {line[0]}
    Due Date:                {line[3]}
    Start Date:              {line[4]}
    Task Completed:          {line[5]}

    Task Description:
    {line[2].replace(":.:", ",")}\n''' + 80 * "_" + "\n")


def view_mine():
    # Opens tasks.txt and copies each line to "line" list then prints task
    # if username matches logged-in user
    # Commas are reintroduced during print step
    # Dependent on "edit_task" and "mark_complete" functions
    print("\nYou have chosen to view your tasks.\n")
    with open("tasks.txt", "r+") as tasks:
        line_count = -1
        for line_string in tasks:
            line_count += 1
            line = line_string.split(", ")
            if line[0] == username:
                print(80 * "_" + f'''\n
    Task:                    {line[1].replace(":.:", ",")}
    TaskID:                  {line_count}
    Assigned to:             {line[0]}
    Due Date:                {line[3]}
    Start Date:              {line[4]}
    Task Completed:          {line[5]}

    Task Description:
    {line[2].replace(":.:", ",")}\n''' + 80 * "_" + "\n")
    print("End of tasks.\n\n")
    while True:
        edit_choice = input('''Would you like to:
return to menu - r
mark task as complete - m
edit task - e
: ''')
        if edit_choice == "r":
            print("\n\n")
            break
        elif edit_choice == "m":
            mark_complete()
        elif edit_choice == "e":
            edit_task()
        else:
            print("Please choose a valid option.\n")


def mark_complete():
    # This function allows a user to mark a task as completed
    edit_choice = int(input("\nPlease enter the TaskID of the task you wish to mark complete: "))
    line_count = -1
    tasks = open("tasks.txt", "r")
    updated_tasks = []
    for line in tasks:
        line_count += 1
        line = line.split(", ")
        if line_count == edit_choice and (line[0] == username or username == "admin"):
            if line[5] == "Yes\n":
                print("Task already marked as complete.\n\n")
            else:
                line[5] = "Yes\n"
                print(f"Task {edit_choice} marked as complete\n\n")
        elif line_count == edit_choice and line[0] != username:
            print("\nPlease choose a valid TaskID (task must be assigned to your account).\n")
        line = ", ".join(line)
        updated_tasks.append(line)
    updated_tasks = "".join(updated_tasks)
    tasks = open("tasks.txt", "w")
    tasks.write(updated_tasks)


def edit_task():
    # This function allows a user to edit the assigned user and due date for a task
    edit_choice = int(input("\nPlease enter the TaskID of the task you wish to edit: "))
    line_count = -1
    tasks = open("tasks.txt", "r")
    updated_tasks = []
    for line in tasks:
        line_count += 1
        line = line.split(", ")
        if line_count == edit_choice and line[0] == username and line[5] != "Yes\n":
            print(80 * "_" + f'''\n
            Task:                    {line[1].replace(":.:", ",")}
            TaskID:                  {line_count}
            Assigned to:             {line[0]}
            Due Date:                {line[3]}
            Start Date:              {line[4]}
            Task Completed:          {line[5]}

            Task Description:
            {line[2].replace(":.:", ",")}\n''' + 80 * "_" + "\n")

            # Loops allow user to reassign task or change due date
            while True:
                reassign = input("Would you like to reassign this task? (y/n): ")
                if reassign.lower() == "y" or reassign.lower() == "yes":
                    line[0] = user_exists_task(input("Who should this task be reassigned to?: "))
                    break
                elif reassign.lower() == "n" or reassign.lower() == "no":
                    break
                else:
                    print("\nPlease choose a valid response.\n")
            while True:
                reschedule = input("Would you like to change the due date for this task? (y/n): ")
                if reschedule.lower() == "y" or reassign.lower() == "yes":
                    line[3] = input("What should the new due date be? (Formatted 1 Jan 2000): ")
                    break
                elif reschedule.lower() == "n" or reassign.lower() == "no":
                    break
                else:
                    print("\nPlease choose a valid response.\n")
            print("\nTask updated.\n\n")

        elif line_count == edit_choice and line[0] == username and line[5] == "Yes\n":
            print("This task is already marked as complete, so cannot be edited.")

        # Blocks invalid users from editing tasks
        elif line_count == edit_choice and line[0] != username:
            print("\nPlease choose a valid TaskID (task must be assigned to your account).\n")

        line = ", ".join(line)
        updated_tasks.append(line)

    # Writes updated task data to tasks.txt
    updated_tasks = "".join(updated_tasks)
    tasks = open("tasks.txt", "w")
    tasks.write(updated_tasks)


def show_stats():
    # This code returns the contents of the user_overview and the task_overview reports
    # and will generate them if needed
    print(80 * "_")
    gen_users_report()
    gen_tasks_report()
    print(80 * "_")
    with open("task_overview.txt", "r") as task_overview:
        print("\n\n====Task Overview====\n")
        for line in task_overview:
            print(line.strip("\n"))
    with open("user_overview.txt", "r") as user_overview:
        print("\n\n====User Overview====\n")
        for line in user_overview:
            print(line.strip("\n"))


def gen_tasks_report():
    # This function generates the task_overview.txt file with statistics
    # pertaining to all tasks on the system
    with open("tasks.txt", "r") as task_file:
        total_tasks = 0
        total_complete = 0
        total_overdue = 0
        for task in task_file:
            task = task.split(", ")
            total_tasks += 1
            due_date = datetime.strptime(task[4], "%d %b %Y")
            if task[5] == "Yes\n":
                total_complete += 1
            elif due_date < datetime.today():
                total_overdue += 1
        total_incomplete = total_tasks - total_complete
        percentage_incomplete = round((total_incomplete / total_tasks) * 100, 2)
        percentage_overdue = round((total_overdue/total_tasks) * 100, 2)

        # Formats and write statistic information to task_overview.txt
        with open("task_overview.txt", "w") as task_overview:
            task_overview.write("The task report for this system is as follows:\n\n" +
                                f"Total Number of Tasks: {total_tasks}\n" +
                                f"Total Tasks Completed: {total_complete}\n" +
                                f"Total Tasks Incomplete: {total_incomplete}\n" +
                                f"Percentage Incomplete: {percentage_incomplete}%\n"
                                f"Total Tasks Overdue: {total_overdue}\n" +
                                f"Percentage Overdue: {percentage_overdue}%\n")
    print("task_overview.txt generated successfully")


def gen_users_report():
    # Generates a .txt report on user statistics
    # Generates list of users from user.txt and counts total tasks
    all_users = []
    total_tasks = 0
    with open("user.txt", "r") as users:
        for line in users:
            line = line.split(", ")
            all_users.append(line[0])
    with open("tasks.txt", "r") as tasks:
        for i in tasks:
            total_tasks += 1

    # Compares user.txt list against tasks.txt, then gathers
    # Statistics related to each username
    user_details = []
    for user in all_users:
        user_total_tasks = 0
        user_tasks_complete = 0
        user_tasks_overdue = 0
        with open("tasks.txt", "r") as tasks:
            for task in tasks:
                task = task.split(", ")
                due_date = datetime.strptime(task[4], "%d %b %Y")
                if task[0] == user:
                    user_total_tasks += 1
                    if task[5] == "Yes\n":
                        user_tasks_complete += 1
                    if due_date < datetime.today():
                        user_tasks_overdue += 1

            # Calculates percentage values for report
            user_percentage_complete = 0
            user_percentage_overdue = 0
            user_percentage_incomplete = 0
            if user_total_tasks > 0:
                user_percentage_total = round((user_total_tasks / total_tasks) * 100, 2)
                if user_tasks_complete > 0:
                    user_percentage_complete = round((user_tasks_complete / user_total_tasks) * 100, 2)
                else:
                    user_percentage_complete = 0
                user_tasks_incomplete = user_total_tasks - user_tasks_complete
                user_percentage_incomplete = 100 - user_percentage_complete
                if user_tasks_incomplete > 0 and user_tasks_overdue > 0:
                    user_percentage_overdue = round((user_tasks_overdue / user_tasks_incomplete) * 100, 2)
                else:
                    user_percentage_overdue = 0
            else:
                user_percentage_total = 0
            # Appends user_details list with formatted information for printout
            user_details.append(f"Username: {user}\n" +
                                f"User total tasks: {user_total_tasks}\n" +
                                f"% of tasks assigned to user: {user_percentage_total}%\n" +
                                f"% of tasks complete: {user_percentage_complete}%\n" +
                                f"% of tasks incomplete: {user_percentage_incomplete}%\n"
                                f"% of incomplete tasks overdue: {user_percentage_overdue}%\n")

    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(f"Total Number of Tasks: {total_tasks}\n\n")
        for user in user_details:
            user_overview.write(user + "\n")

    print("user_overview.txt generated successfully")


# ====Login Section====
# Calls login function and defines username
username = login()

# ====Main Program====
# Loop prevents program exit on completion of task
print("\n" + 29 * "#" + "\n#  Welcome to Task Manager  #\n" + 29 * "#")
while True:

    # Presents menu to user, additional option for "statistics" if username is "admin"
    print(80 * "_" + '''\nSelect one of the following options below:
a - Adding a task
va - View all tasks
vm - View my tasks
e - Exit''')
    if username == "admin":
        print('''\nADMIN OPTIONS:
r - Registering a user
gr - Generate Reports
s - View program statistics''')
    menu = input("\nYour choice: ")
    
    # This option allows users to create new user login credentials if admin
    if menu == 'r' and username == "admin":
        reg_user()

    # This option allows the user to enter a task into the manager
    elif menu == 'a':
        add_task()
        
    # This option allows you to view all tasks currently stored in tasks.txt
    elif menu == 'va':
        view_all()

    # This option allows users to view their tasks only
    elif menu == 'vm':
        view_mine()
            
    # This option only presents itself to the admin account + checks if user attempting to access it is admin
    elif menu == "s" and username == "admin":
        show_stats()

    # Generates user_overview.txt and task_overview.txt report files
    elif menu == "gr" and username == "admin":
        gen_users_report()
        gen_tasks_report()
        print("\n")

    # This option quits the program
    elif menu == "e":
        print("Tata for now!")
        exit()

    # This prevents the program from throwing an error if an invalid choice is made
    else:
        print("\nYou have made an invalid choice, please try again\n")
