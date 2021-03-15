#imports the libary date and time
#uses the built in module from dateand time known as timedelta and date
import datetime
from datetime import timedelta, date

#gives the preset bool value to false
#reads and edits into the user file
user_f = open('user.txt','r+')
login = False 



#while loop that will run until login value is changed to True
#asks user for they name
#asks user for the password
while login == False:  
    name = str(input("Please enter your username\n Username:"))
    password = str(input("Pleae enter your password\nPassword:"))



#for loop that iterates over the the entire file
#splits the string at the , and space and assigns the values before the , and after the " "
    for line in user_f :
        valid_name, valid_password = line.split(", ")#valid_name and valid_password which will be assigned to the wordds before and after the comma in the split function
        


#if statement that comapers the users name and password to the one saved in the file

        if name == valid_name and password == valid_password.strip():
            login = True 


#if statement that will run if the above if statement doesn't work which will result in login remaining false 
#seek function that takes us back to the start of the file   
#closing of the file   
    if login == False:       
        print("You have entered the inccorect password or username please retry") 
    user_f.seek(0)
user_f.close()



#reopening of the file but insted of writing/reading we are appending
user_f = open("user.txt","a+")
user_count = open('user.txt','r')
task_count = open('tasks.txt','r')
all_task1 = []
all_users1 = []
#if statemnet that will run only if loging == True and name is equal to admin
#user input that is stored in the variable select
#else statement that will run if the if statment is false 
if login == True and name == "admin": 
    select = input("\nPlease enter a choice from the list below\ns - stats\nr - register user(ONLY ADMIN)\na - add task\nva - view all task\nvm - view my task\ne- exit\n Enter choice here:")
    if select == "s":
        i = 0
        n = 0
        for line in user_count:
            all_users1 = line
            i+=1
        for line in task_count: 
            all_task1 = line
            n+=1 
    print("\nThis is how many tasks there are - ",n,"\n This is how many users there are -",i)          

else:
    select = input("\nPlease enter a choice from the list below\nr - register user(ONLY ADMIN)\na - add task\nva - view all task\nvm - view my task\ne- exit\n Enter choice here:")


#log with the bool value of False 
#while loop that will run while name is not = admin 
#the print function will be printed if the while loop is not broken
log = False
while name != "admin":
    print("Please loggin as admin to add a new user !")
    break
    
#if statement that will run if name is equal to admin
#nested if statement that will check if the variable select is equal to r
#and if the if statment is true the inputs new_name and new_password will be displayed 
if name == "admin":
    if select == "r":
        new_name = input("\nPlease enter a new user name :")
        new_password = input("Please enter a new password :")

#if log is false then the following confirm password will be run
#and user inputs are stored in confirm_n and confirm_p 
        if log == False:
            print("\nPlease confirm your Name and Password below")
            confirm_n = str(input("confirm Name here:"))
            confirm_p = str(input("Confrim Password here:"))
    
#if both the users first input and second inputs are true then the following statement will be displayed
#and the preset bool value will be changed to true
        if confirm_n == new_name and new_password == confirm_p:
            print("your new name and Password has been confirmed!!")
            log = True


#if the bool value is true then the if statement will run
#user_f.write will add our new name and password to the file
if log == True: 
    user_f.write( "\n" + new_name + ", " + new_password )
user_f.close()


#file opened and stored in task_f variable and is set to append 
#if the variable select is equal to a then the if statement will run 
#the print function will dislay its message
#the var complete will have the preset value of no 
#the var user will ask the user for they name 
#task will ask the user for what task they need to do 
#num_day stores the number of days the useer has to complete the task
#due_date combines the num_days and the current date for a due date
#formated_date is the current date that is in the correct formate
#formated_date1 is the due_date but in the correct format
#note we dont need this append var but i just find it to be alot neater and easier for future code 
#and we finally all of this to our file with the write() function
#and we close and save the file
task_f = open('tasks.txt','a+')
if select == "a" :
    print("This is for a new task")
    complete = "No"
    user = str(input("\nPlease enter your name or the name of the user\nEnter here:"))
    task = str(input("\nPlease enter the task you have to do\nEnter here:"))
    num_days = int(input("Please enter the number of days they have to do the task from today\nEnter here:"))
    due_date = Date_required = date.today() + timedelta(days=num_days)
    today = datetime.datetime.now()
    formated_date = str(today.strftime("%d %b %Y"))
    formated_date1 = str(due_date.strftime("%d %b %Y"))
    append = user+ ", "+ task +", " + formated_date+ ", " + formated_date1 + ", " + complete+"\n"
    task_f.write(append)

task_f.close()


#we open the file in read only and store it in task_f
#we create a empty list and store it in all tasks
#if the variable select is equal to va the the if statement will run
#for loop that will read over the file and enumerate of the file 
#pushes our information in the file into our empty list and strips the white spaces at the end and front
#increments our c/count value by one 
#prints out all the tasks and the number of the task
task_f = open("tasks.txt","r")
all_task = []

if select == "va":
    
    for c,i in enumerate(task_f):
        all_task =i.strip()
        c+=1
        print("\n"+str(c)+ ".)"+ all_task)

task_f.close()


#opens the file tasks and stores its value in the var task_f
#var my_tasks with a value of a empty string
#if statement that will check if the variable select is equal to vm 
#for loop that will run once the if statment is true and it will read over the tasks file
#split variable that reads info before and after the comma
#if statment that will run if name is equal to the name in the file 
#prints out all the tasks in the file with the name provided
#task file closed and saved
task_f = open('tasks.txt','r')
my_task = ""

if select == "vm":
    for line in task_f: 
        my_task = line.strip()
        split = my_task.strip().split(',')
        if split[0] == name:
            print(my_task,"\n")
task_f.close()



