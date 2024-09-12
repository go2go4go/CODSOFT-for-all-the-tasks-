#My name is Ganat Ahmed 
#Here I will use python to help me as biotechnologist arrange steps of experiment of GENE CLONING in laboratory
#Steps are in order : 
#prepartion of competent cells
#Extraction of gDNA of plant
#Isolation of X gene by PCR
#Ligation of X gene and vector or (plasmid)
#Transformation of ligation product into competent cells
# Mini prep for isolation plasmids
# Confirmation by digesion with restriction enzymes 

"""
1)Add your tasks to list
2)Mark task as completed
3)view tasks
4)Exit
"""
print("please, Enter your name:")
name=input("Your name is:")
print("Hello,"+name)
Message="""1)Add your tasks to list
2-Mark task as completed
3-view tasks
4-Exit"""
print(Message)
def Add_task():
   task=input("Enter ypur task:")
   task_info={"task":task,"completed":False}
   Tasks.append(task_info)
   print("Your task is added successfully.")

def Mark_task_completed():
   incomplete_tasks=[task for task in Tasks if task["completed"]==False] 
   if len(incomplete_tasks)==0:
        print("Sorry..There is no tasks to mark as complete") 
        return
   for i, task in enumerate(incomplete_tasks):
         print(f"{i+1}-{task['task']}")
         print("..."*20)
         task_number=int(input("choose the task as complete:"))
         incomplete_tasks[task_number-1]["completed"]=True
        # print(Tasks)
         print("Your tasks marked successfully")
def view_tasks():
    if not Tasks:
       print("Sorry,no tasks to view")
       return
    for i,task in enumerate(Tasks):
       if task["completed"]:
          status="✔"
       else:
          status="❌"
       print(f'{i+1}.{task["task"]}.{status}')

Tasks=[]
while True:
    print(Message)
    choice=input("Enter your choice:")  
    if choice=="1":
        Add_task()
    elif choice=="2":
       Mark_task_completed()
    elif choice=="3":
      view_tasks()
    elif choice=="4":
       break   
    else:
     print("Sorry...That is wrong ")


