# todo list using file handling
# importing os for checking whether the task.txt file already exist in the directory or not
# if it is present then we will not create another task.txt
import os


def check():
    path = os.getcwd()  # this is fetch the current working directory path

    is_existing = os.path.exists(path)
    if is_existing == True:
        return True
    return False


def createTask():
    file = open('task.txt', 'a')
    print("Enter your task, if finish type done")
    while True:
        task = str(input("->"))
        if task == 'done' or task == 'DONE':
            file.close()
            return
        file.write(task)
        file.write('\n')



def display():
    file = open('task.txt', 'r')
    i=1
    for lines in file:
        print(i,".",lines)
        i+=1
    file.close()


def markComplete():
    display()
    print("Enter the Serial number/numbers of task you want to mark completed,if finished type 'Done' :")
    numbers=[]
    # file=open('task.txt','a')
    while True:
        sl_no=input("->")
        if sl_no=='done' or sl_no=="Done":
            break
        numbers.append(int(sl_no))
    for number in len(numbers):
        print(number)

    # for line in file:
    #     for number in numbers:
    #         if line ==number:
    lines = []
    # read file
    with open("task.txt", 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()

    # Write file
    with open("task.txt", 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            # delete line 5 and 8. or pass any Nth line you want to remove
            # note list index starts from 0
            if number not in numbers:
                fp.write(line)
    fp.close()
    print("Updating list...")
    display()



def markAllComplete():
    file=open('task.txt','w')
    print("Wohooo!! All task marked completed!!")
    file.write('')
    file.close()


print("Welcome to your ToDo List Application")
print("checking the files in your directory....", )
if check() == True:
    print("Yes, the file exists in your directory, we will append on that file.")
else:
    print("Unable to find the file. We will need to create a file for storing tasks")
    print("Creating...")
    file = open('task.txt', 'x')
    file.close()
print("Operations:"
      "\n1.Create a task"
      "\n2.Show pending tasks"
      "\n3.Mark a task complete"
      "\n4.Mark all tasks complete")
operation = int(input("choose your operation (1/2/3/4): "))
if operation == 1:
    createTask()
elif operation == 2:
    display()
elif operation == 3:
    markComplete()
elif operation == 4:
    markAllComplete()
else:
    print("Invalid Operation!!")
