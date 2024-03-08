def main():
    while True:
        print("\n1.add task \n2.delet task \n3.display all tasks\n4.updata the task\n5.To exit \n")
        user=int(input("enter you choice "))
        if(user==1):
             addtask()
        elif(user==2):
            delete_task()
        elif(user==3):
            printTasks()
        elif(user==4):
            updata_task()
        elif(user==5):
            break
        else:
            print("enter vailed input")
        
        
        
#add a task
def addtask():
    with open("todo.csv","a") as file:
        file.write( input("enter the task : ")+",status:incomplete \n")
        
#deleat a task
def delete_task():
    task_list = []
    printTasks()
    i = int(input("Enter the number of the task you want to delete: "))
    with open("todo.csv") as file:
        for line in file:
            task_list.append(line.strip())
        if(len(list)>=i):
            del task_list[i-1]
        with open("todo.csv", "w") as file:
            for task in task_list:
                file.write(task + "\n")
            print("Task deleted successfully")
        

#updata a task
def updata_task():
    task_list = []
    printTasks()
    i = int(input("Enter the number of the task you want to updata: "))
    new_task=input("enter the nuw task : ")
    with open("todo.csv") as file:
        for line in file:
            task_list.append(line.strip())
        task_list[i-1]=new_task
        with open("todo.csv", "w") as file:
            for task in task_list:
                file.write(task + "\n")
            print("Task deleted successfully")
#print all tasks
def printTasks():
    i=1
    with open("todo.csv","r") as file:
       for line in file:
           row=line.rstrip().split(",")
           print(f"{i}.{row[0]}\n{row[1]} ")
           i+=1


main()
