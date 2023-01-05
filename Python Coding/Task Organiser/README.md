# Task Manager - Archie Macdonald #

## Description ##
 This project is a task_management tool for creating, altering 
 and assigning tasks to users



## Contents: ##
1. Functions
2. Login
3. Main Menu Options
4. Input Files
5. Output Files
6. Planned Changes
7. Changelog


## 1) Functions ##

 Below you will find a list of functions used in this project
 and descriptions of how they work. Also included are any
 dependencies between functions.

### Login Functions ###

 __login__:             Reads the user.txt file and creates a dictionary mapping
                   each username against it's respective password. The user is
                   then prompted to enter their username, which is rejected if
                   not in the dictionary, and their password, which is rejected
                   if not correct for the respective username. Returns the
                   username as a value for use in the main program.

### Main Menu Functions ###

 __reg_user__:          Allows the admin user to create new user accounts. This
                   function will check the new username against the existing
                   list using a similar method to username_check. If it 
                   already exists, it will ask for a new one. It then will
                   ask for a password, which must be confirmed by the user
                   before the program will write the new user to "user.txt".
                   New user details are appended to "user.txt".

 __add_task__:          Allows user to create a new task and assign it to a user.
                   It will check that the assigned username exists before 
                   allowing the author to enter in the task details. These
                   include: user assigned, task title, task description and
                   the due date. It will also automatically generate the
                   date of creation and mark the task as incomplete.
                   The user will then be asked to confirm the task details
                   that are printed on-screen. Once confirmed, they are
                   written to the tasks.txt file. If the user selects "no"
                   at this point, they will be prompted to re-enter the
                   task details.

 Dependent on - user_exists_task(), datetime

 __user_exists_task__:  Checks that a username exists in the user.txt file by
                   checking each line of the file individually.

 __view_all__:          Reads tasks.txt and prints each task onscreen in a user-
                   friedly fashion. Also assigns each task a "TaskID" based
                   on their respective line in the file.

 __view_mine__:         Similar to view_all, but will only print tasks assigned
                  to currently logged in user. This is done by splitting
                   each line into lists and checking the username value of
                   the task against that of the logged in user "username".
                   After printing out the tasks, it will prompt users to
                   select one of three options: return to menu (r), 
                   mark task complete (m), or edit task (e). Return to menu
                   will end the function, but the other two will run the
                   mark_complete and edit_task functions respectively.

 Dependent on - mark_complete, edit_task

 __mark_complete__:     This function will allow a user to enter the TaskID of
                   a task to mark it as complete by editing the line in the 
                   tasks.txt file. If the selected task is already marked 
                   as complete, then it will return a message saying such.
                   Users are only able to mark tasks as complete if that
                   task is assigned to them.

 __edit_task__:         Allows the user to edit task that are assigned to them
                   by changing either/both the assigned user and the due
                   date. Once the user has edited these details, the task
                   is written to tasks.txt.

 Dependent on - user_exists_task


 __show_stats__:        This choice is only visible and accessible for the admin
                   account. Will generate reports on the users and tasks on
                   the system, then print the contents of those reports to
                   the screen in a user-freindly fashion.

 Dependent on - gen_tasks_report, gen_users_report

 __gen_tasks_report__:  This function generates a .txt file containing statistics
                   pertaining to the tasks stored in tasks.txt along with 
                   printing a confirmation message. Included are:

> Total Number of Tasks  
> Total Tasks Completed  
> Total Tasks Incomplete  
> % Incomplete  
> Total Tasks Overdue  
> % Overdue  

 Dependent on - datetime

 Output - task_overview.txt

 __gen_users_report__:  This function generates a .txt file containing statistics
                   for each user on the system along with printing a 
                   confirmation message. Included are: 
                   
> Total Tasks on System (Once)  
> Username  
> User total tasks  
> % of tasks assigned to user  
> % of tasks complete  
> % of tasks incomplete  
> of incomplete tasks overdue  

 Dependent on - datetime  

 Output - user_overview.text


## 2) Login ##

 When starting the program, users will be asked to login. Incorrect usernames
 or passwords will be rejected and the user prompted to try again. New users
 can be created using the admin account.


## 3) Main Menu ##

 The main menu offers four basic options to all users:

> a - Adding a task  
> va - View all tasks  
> vm - View my task  
> e - exit  

 Entering an invalid choice will reprint the menu and ask the user to try
 again. In addition to these options, the admin account will be presented
 with three additional options which only they can access:

> r - Registering a user  
> gr - Generate Reports  
> s - View program statistics  


## 4) Input Files ##

 This program requires two files in the same directory as it, the user.txt
 file and the __tasks.txt__ file.

 __user.txt__:  This file contains the username and password for each user. This
           information must be in the format:

> username1, password1  
> username2, password2  
> username3, password3  
> etc...  

 __tasks.txt__: This file contains all of the information on the tasks stored
           in the system. Each task has it's own line and must be formatted
           as such:
           
> username, title, description, creation date, due date, completed y/n

 The due date must be in the format __"1 Jan 2000"__ and the task
 completed entry must be __"Yes"__ or __"No"__.

 Due to the use of commas as delimiters, all commas within the task
 title and description are converted to ":.:" in the .txt file.

 In case of error when running view_all or view_mine functions,
 make sure that there is not a blank line inserted at bottom
 of tasks.txt file.


## 5) Output Files ##

 Alongside being able to edit the contents of user.txt and tasks.txt, the 
 program can also create two more files: __user_overview__ and __task_overview__.
 These files contain information on the user assigned tasks and all tasks
 respectively. They are generated either by choosing the generate reports
 or statistics option on the main menu as an admin. Every time these options
 are run, the files are overwritten, so make sure to move these files to a
 different location for archiving.


## 6) Planned Changes ##

 __Date Formatting__ - Currently users can enter due dates in any format as they
                  are stored as a string. I plan to implement a system that
                  checks entered dates are legible to the datetime function.
 
 __Admin Editing__   - This will allow the admin to edit tasks that are assigned
                  to other users. I plan to implement this in an admin
                  only option in the view_all function.

## 7) Changelog ##

### Version 2: ###  

 *Introduced generate report function and altered the statistics options on the
  menu to use the .txt reports for presenting information  

 *New login function completes login checks in a single function rather than three
  and uses a dictionary instead of lists  

 *Ability to edit and mark tasks as complete introduced  

 *Add new user function moved to hidden admin menu for clarity  

 *Majority of code now moved to seperate functions  

 *Some small visual changes made to printout of menus  


