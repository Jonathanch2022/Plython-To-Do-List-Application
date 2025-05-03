from typing import final
task = []
commands = ["add", "delete", "view", "quit"] #List of commands that can be used in the application]

def addTask(): #Add a task to the task list
  aTask = input("Enter a task to add: ") #Prompt the user to enter a task to add to the task list
  task.append(aTask)
  print("Task added successfully!")
  
def deleteTask(): #Remove a task from the task list 
   valid = False
   while True:
       aTask = input("Enter the index of the task to delete: ") #Prompt the user to enter the index of the task to be deleted from the task list)
       if aTask.upper() == "QUIT": #Check if the user wants to quit the application
        quit_App(0)
      
       elif aTask.isdigit() == False: #Check if the input is a digit
        raise Exception("Invalid input! Please enter a valid non negative whole number.") #Raise an exception if the input is not a digit)
        print("Invalid input! Please enter a valid non negative whole number.")               
       elif int(aTask) > len(task) - 1: #Check if the input is greater than the length of the task list
        print("Invalid input! Please enter a valid index.")
       else:
          break
   task.pop(int(aTask)) #Remove the task from the task list
   print("Task deleted successfully!")
  
def viewTask(): #List all tasks in the task list
  tIndex = 0
  for t in task: #Loop through the task list and print each task with its index
    print(f"{tIndex}: {t}")
    tIndex += 1
  return(task)

def quit_App(exitcode): #Quit the application
  if exitcode == 0:
   print("Good Bye!") # Print message and Exit the application
    
  exit(0)
 
def app_Start():
  try:
      print("Welcome to the To-Do Application")
      print("What would you like to do?")
      print("Below are the list of commands you can use:")
      x = 0
      for i in commands: #Loop through the list of commands and print each command with its index
        x += 1
        match x: #Match the index of the command with its corresponding action
          case 1: 
            print(f"{x}: {i.upper()} - Adds a task to the task list") 
          case 2:
            print(f"{x}: {i.upper()} - Deletes a task from the task list")
          case 3:
            print(f"{x}: {i.upper()} - View all tasks in the task list")
          case 4:
            print(f"{x}: {i.upper()} - Quits the application")
      
      run()  
  except:
    quit_App(1)#Quit application if an exception is raised
  finally:
    print("Thank you for using the To-Do Application!" #Print message when the application is closed
    )
    
def run():
  xinput = ""
  while xinput != "quit": #Loop until the user enters "quit"
    xinput = input("Enter a command name: ") #Prompt the user to enter a command
    match xinput.upper(): #Match the input with the corresponding action
      case  "ADD"| "1":
        addTask() 
      case "DELETE" | "2":
        deleteTask()
      case "VIEW" | "3":
        viewTask()
      case "QUIT" | "4":
        quit_App(0)
      case _:
        print ("Invalid command! Please try again.") #Print message if the input is not a valid command
        
app_Start(); #Start the application

