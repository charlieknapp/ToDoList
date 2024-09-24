import os, random

todo = []
try:
  f = open("todolist.txt","r")
  todo = eval(f.read())
  f.close()
except:
  f = open("todolist.txt","w")
  f.close()

f = open(f"backup{random.randint(1,1000000000)}.txt","w")
f.write(str(todo))
f.close()

def add(list):
  what = input("What is it? ")
  when = input("When is it due? ")
  how = input("Priority(high, medium, low)? ")
  list.append([what, when, how])
def prettyprint(list):
  for item in list:
    print(f"{item[0]} | {item[1]} | {item[2]}")
def view(list):
  view = input("View all or view priority? ")
  if view == "all":
    prettyprint(list)
  elif view == "priority":
    priority = input("What priority? ")
    for item in list:
      if item[2] == priority:
        print(f"{item[0]} | {item[1]} | {item[2]}")
def remove(list):
  item = input("What would you like to remove? ")
  for i in range(len(list)):
    if list[i][0] == item:
      list.remove(list[i])
def edit(list):
  item = input("What would you like to edit? ")
  for i in range(len(list)):
    if list[i][0] == item:
      list[i][0] = input("What is it? ")
      list[i][1] = input("When is it due? ")
      list[i][2] = input("How important is it? ")
while True:
  menu = input("What would you like to do?(add, view, remove, edit, exit) \n").lower().strip()
  if menu == "add":
    add(todo)
  elif menu == "view":
    view(todo)
  elif menu == "remove":
    remove(todo)
  elif menu == "edit":
    edit(todo)
  elif menu == "exit":
    break
  else:
    print("Enter a valid input")
  f = open("todolist.txt","w")
  f.write(str(todo))
  f.close()