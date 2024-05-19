import os
import time

"""
things to add:
- make it so that every time it shows all task, todew rechecks task status. change status to overdue if date has passed
"""
class Task:
    def __init__(self):
        self.detail = input("Task Details: ")
        self.description = input("Task Description (Optional): ")
        
        self.setDate()

        if (self.day != 0):
            self.setTime()

        else:
            self.time = ""
            self.hour = self.minute = -1
            
        self.setPriority()
        self.status = "Ongoing"

    def setDate(self):
        while True:
            self.date = input("Input Due Date (DD/MM/YYYY): ")

            if (self.date == "" or self.date == "-"):      
                print("Task has no due date.")
                self.day = self.month = self.year = 0
                return
            
            elif not("/" in self.date):
                print("Invalid date input. Please try again.\n")
                continue
            
            self.day, self.month, self.year = map(int, self.date.split("/"))    
            
            if (self.year < curr_year):         
                print("Year has passed! Please try again.\n")
                continue
            
            if (self.year > curr_year + 5): 
                print("Date is too far in the future. Please try again.\n")
                continue

            if (self.month < curr_month and self.year == curr_year):
                print("Month has passed! Please try again.\n")
                continue

            if (self.day < curr_day and self.month == curr_month and self.year == curr_year):
                print("Date has passed! please try again.\n")
                continue

            if (self.month < 1 or self.month > 12):
                print("Invalid Month input. Please try again.\n")
                continue

            if (self.day < 1 or self.day > 31):
                print("Invalid day input. Please try again.\n")
                continue

            if (self.month < 8):
                if (self.month == 2):
                    if (self.year % 4 == 0):
                        if (self.day > 29):
                            print(f"February {self.year} only goes up to the 29th. Please try again.\n")
                            continue

                    elif (self.day > 28):
                        print(f"February {self.year} only goes up to the 28th. Please try again.\n")
                        continue

                elif (self.month % 2 == 0 and self.day > 30):
                    print(f"This month only goes up to the 30th. Please try again.\n")
                    continue

            else:
                if (self.month % 2 == 1 and self.day > 30):
                    print(f"This month only goes up to the 30th. Please try again.\n")
                    continue

            break

    def setTime(self):
        while True:
            self.time = input("Set Time (HH:MM): ")         

            if (self.time == "" or self.time == "-"):
                self.hour = self.minute = -1
                return
            
            elif not(":" in self.time):
                print("Invalid time input. Please try again.\n")
                continue
            
            self.hour, self.minute = map(int, self.time.split(":"))

            if (self.hour < 0 or self.hour > 23):
                print("Invalid hour input. Please try again.\n")
                continue

            if (self.minute < 0 or self.minute > 59):
                print("Invalid minute input. Please try again.\n")
                continue

            if (self.date == curr_date):
                if (self.hour < curr_hour):
                    print("Hour has passed. Please try again.\n")
                    continue

                if (self.hour == curr_hour and self.minute < curr_minute):
                    print("Minute has passed. Please try again.\n")
                    continue

            break


    def setPriority(self):
        if (self.date == "" or self.date == "-"):
            self.priority = 6
            return

        day_gap = int(self.day) - int(curr_day)
        month_gap = int(self.month) - int(curr_month)   
        year_gap = int(self.year) - int(curr_year) 
        
        if (year_gap > 1):
            self.priority = 5
            return
        
        if (year_gap == 1):
            if (curr_month != 12 or self.month != 1):
                self.priority = 5
                return

            month_gap = 1
        
        if (month_gap > 1):
            self.priority = 5
            return

        if (month_gap == 1):
            if (day_gap >= 0):
                self.priority = 5
                return

            if (curr_month < 8):
                if (curr_month == 2):
                    if (curr_year % 4 == 0):
                        day_gap = (29 - curr_day) + self.day
                        
                    else:
                        day_gap = (28 - curr_day) + self.day

                elif (curr_month % 2 == 0):
                    day_gap = (30-curr_day) + self.day

                elif (curr_month % 2 == 1):
                    day_gap = (31-curr_day) + self.day

            else:
                if (curr_month % 2 == 0):
                    day_gap = (31-curr_day) + self.day

                elif (curr_month % 2 == 1):
                    day_gap = (30-curr_day) + self.day

        if (0 <= day_gap <= 2):
            self.priority = 1
            return
        
        elif (3 <= day_gap <= 4):
            self.priority = 2
            return
        
        elif (5 <= day_gap <= 7):
            self.priority = 3
            return
        
        elif (8 <= day_gap <= 10):
            self.priority = 4
            return
        
        elif (day_gap > 10):
            self.priority = 5
            return
        
        else:
            self.priority = 6


class Category:
    def __init__(self, name):
        self.name = name
        self.tasks = []

class ToDew:
    def __init__(self):
        self.categories = [Category("Homework"), 
                           Category("Exam"), 
                           Category("Organization"), 
                           Category("Social"), 
                           Category("Others")]
        
        self.completedTasks = []

    def addTask(self):
        print("||====== Add Task ======||")
        print("Today's Date\t:", curr_date)
        print("Time\t\t:", curr_time)
        print()       

        print("Where to add task?\n")
        for i in range(len(self.categories)):
            print(f"[{i+1}] {self.categories[i].name}")

        print()
        location = input("Input Category Number\t: ")
        print()

        category = None
        for i in range(len(self.categories)):
            if (location == str(i+1)):
                category = self.categories[i]
                break
    
        if (category is None):
            print("Category Number not found. Please try again.")
            return
        
        task = Task()
        category.tasks.append(task)

    def deleteTask(self):
        print("||====== Delete Task ======||")
        self.showAllTasks()
        print("===================================")
        detail = input("Task Detail to Delete\t: ")
        print()

        for category in self.categories:
            for task in category.tasks:
                if (task.detail.lower() == detail.lower()):
                    print(f"'{task.detail}' in '{category.name}' has been deleted.")
                    category.tasks.remove(task)
                    return
        
        print("Unfortunately, the task could not be found. Try again?")
        time.sleep(2)

    def searchTask(self) :
        print("||====== Search Task ======||")
        detail = input("Task Detail to Search\t: ")

        for category in self.categories :
            for task in category.tasks :
                if task.detail == detail :
                    print("< Task Found >")
                    print(category.name)  
                    print(f"{task.detail}\n{task.date} | {task.time}\n{task.description}")
                else :
                    print("Said task cannot be found.")

    def completeTask(self):
        print("||=== Complete Task ===||")
        self.showAllTasks()
        print("===================================")
        detail = input("Completed Task\t: ")
        print()

        for category in self.categories:
            for task in category.tasks:
                print(task.detail.lower, detail.lower())
                if (task.detail.lower() == detail.lower()):
                    print(f"Congratulations! '{task.detail}' in '{category.name}' has been completed!")
                    task.status = "Completed"
                    self.completedTasks.append(task)
                    category.tasks.remove(task)
                    return
                
        print("Unfortunately, task was not found. Try again?")
        time.sleep(10)

    def showAllTasks(self):
        os.system('cls')
        self.sortDateAndTime("asc")
        self.checkOverdue()

        print("||=== Displaying All Tasks ===||")

        for c in self.categories:
            print(f"{c.name}:")
            print("==============")

            number = 1
            for t in c.tasks:
                print(f"({number}) '{t.detail}' | Priority {t.priority} - ", end = "")

                if (t.day == 0):
                    print(f"No Due Date ({t.status})")

                elif (t.hour == -1):
                    print(f"{t.date} ({t.status})")

                else:
                    print(f"{t.date}, {t.time} ({t.status})")

                if (t.description != ""):
                    print(f"    Description: {t.description}")

                number += 1

            print()
            
        print("Completed Tasks:")
        print("==============")
        if (len(self.completedTasks) == 0):
            print("No task completed yet.")
            
        else:
            number = 1

            for task in self.completedTasks:
                print(f"({number}) '{task.detail}'")

                number += 1

        print()

        option = input("Press enter to continue... ")

    def editTask(self):
        print("||=== Edit Task ===||")
        self.showAllTasks()
        print("=====================================")
        task = input("Task to Edit: ")

        print("\nProperty to Change")
        print("[1] Task Details")
        print("[2] Task Description")
        print("[3] Due Date")
        print("[4] Time")
        print("[5] Taks Status")
        change = input("Input Code: ")

        for c in self.categories:
            for t in c.tasks:
                if (t.detail.lower() == task.lower()):
                    if (change == "1"):
                        t.detail = input("Task Details: ")
                        
                    elif (change == "2"):
                        t.description = input("Task Description: ")

                    elif (change == "3"):
                        t.setDate()
                        t.setPriority()

                    elif (change == "4"):
                        t.setTime()

                    else:
                        print("Unfortunately, code is invalid. Try again?")

                    return
        
        print("Unfortunately, task was not found. Try again?")
        time.sleep(2)
                
    def topPriorities(self):
        self.sortDateAndTime("desc")

        top = []
        count = 0

        for c in self.categories:
            i = len(c.tasks)-1

            while (i >= 0):
                x = c.tasks[i]
                i -= 1

                if (x.priority == 1 and (x.status == "Ongoing" or x.status == "Overdue")):
                    top.append(x)
                    count += 1

        print(f"Priority 1 Task Amount: {count}")
        print("", f"{'DETAILS':20}", f"{'DEADLINE':20}", f"{'PRIORITY':10}", f"{'STATUS':12}", sep = " | ", end = " |\n")
        print("=======================================================================================")
        for task in top:
            print("", f"{task.detail:20}", f"{task.date+", "+task.time:20}", f"{task.priority:10}", f"{task.status:12}", sep = " | ", end = " |\n")
        print("=======================================================================================")

        option = input("Press enter key to continue: ")

    def sortDateAndTime(self, sort_type):
        if (sort_type == "asc"):
            for c in self.categories:
                for iteration in range(len(c.tasks)):
                    for index in range(len(c.tasks)-iteration-1):
                        if (c.tasks[index].year > c.tasks[index+1].year):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

                        elif (c.tasks[index].month > c.tasks[index+1].month):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

                        elif (c.tasks[index].day > c.tasks[index+1].day):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

                        elif (c.tasks[index].hour > c.tasks[index+1].hour):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

                        elif (c.tasks[index].minute > c.tasks[index+1].minute):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

        elif (sort_type == "desc"):
            for c in self.categories:
                for iteration in range(len(c.tasks)):
                    for index in range(len(c.tasks)-iteration-1):
                        if (c.tasks[index].year < c.tasks[index+1].year):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

                        elif (c.tasks[index].month < c.tasks[index+1].month):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

                        elif (c.tasks[index].day < c.tasks[index+1].day):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

                        elif (c.tasks[index].hour < c.tasks[index+1].hour):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

                        elif (c.tasks[index].minute < c.tasks[index+1].minute):
                            temp = c.tasks[index]
                            c.tasks[index] = c.tasks[index+1]
                            c.tasks[index+1] = temp

    def displayPriority(self):
        priorities = [
            [], [], [], [], [], []
        ]

        for c in self.categories:
            for task in c.tasks:
                priorities[task.priority-1].append(task)

        for i in range(len(priorities)):
            print(f"Priority {i+1}")
            print("================")

            number = 1
            for task in priorities[i]:
                if (task.hour == -1):
                    if (task.day == 0):
                        print(f"({number}) {task.detail}")

                    else:
                        print(f"({number}) {task.detail} - {task.date}")

                else:
                    print(f"({number}) {task.detail} - {task.date}, {task.time}")

                if (task.description == "-" or task.description == ""):
                    number += 1
                    continue

                else:
                    print(f"    Task Description: {task.description}")
            
            print()

        option = input("Press enter to continue: ")

    def checkOverdue(self):
        for c in self.categories:
            for t in c.tasks:
                if (t.day == 0):
                    continue

                if (t.year < curr_year):
                    t.status = "Overdue"
                    continue

                elif (t.year == curr_year):
                    if (t.month < curr_month):
                        t.status = "Overdue"
                        continue

                    elif (t.month == curr_month):
                        if (t.day < curr_day):
                            t.status = "Overdue"
                            continue

                        elif (t.day == curr_day):
                            if (t.hour == -1):
                                continue

                            if (t.hour < curr_hour):
                                t.status = "Overdue"
                                continue

                            elif (t.hour == curr_hour):
                                if (t.minute < curr_minute):
                                    t.status = "Overdue"
                                    continue

    def menu(self):
        while True:
            os.system("cls")
            print("||=== ToDew ===||")
            print("Today's Date\t:", curr_date)
            print("Time\t\t:", curr_time)
            print()

            print("[1] Add Task")
            print("[2] Delete Task")
            print("[3] Search Task")
            print("[4] Edit Task")
            print("[5] Complete Task")

            print()
            print("[6] Display by Priority")

            print()
            print("[7] Show Top Priorities")
            print("[8] Show All Tasks")

            print()
            print("[9] Progress Day")
            print("[10] Progress Minute")
            print("[11] Exit")
            print("||========================||")
            option = input("Input Menu Code: ")

            print("\nLoading...")
            os.system('cls')

            if (option == "1"):
                self.addTask()
            
            elif (option == "2"):
                self.deleteTask()

            elif (option == "3"):
                self.searchTask()

            elif (option == "4"):
                self.editTask()
            
            elif (option == "5"):
                self.completeTask()

            elif (option == "6"):
                self.displayPriority()
                continue
            
            elif (option == "7"):
                self.topPriorities()
                continue

            elif (option == "8"):
                self.showAllTasks()
                continue

            elif (option == "9"):
                progressDate()
                continue

            elif (option == "10"):
                progressTime()
                continue

            elif (option == "11"):
                break

            else:
                print("Unfortunately, code is invalid. Try again?\n")
                continue

            print()
            self.showAllTasks()
            progressTime()
            print()

            if (curr_hour == 0 and curr_minute == 0):
                progressDate()
            

def progressDate():
    global curr_date, curr_year, curr_month, curr_day
    if (curr_month < 8):
        if (curr_month == 2):
            if (curr_year % 4 == 0):
                if (curr_day == 29):
                    curr_day = 0
                    curr_month += 1

            if (curr_day == 28):
                curr_day = 0
                curr_month += 1
            
        elif (curr_month % 2 == 0):
            if (curr_day == 30):
                curr_day = 0
                curr_month += 1
        
        elif (curr_month % 2 == 1):
            if (curr_day == 31):
                curr_day = 0
                curr_month += 1

    elif (curr_month >= 8):
        if (curr_month == 12):
            if (curr_day == 31):
                curr_day = 0
                curr_month = 1
                curr_year += 1

        elif (curr_month % 2 == 0):
            if (curr_day == 31):
                curr_day = 0
                curr_month += 1
        
        elif (curr_month % 2 == 1):
            if (curr_day == 30):
                curr_day = 0
                curr_month += 1
            
    curr_day += 1

    curr_date = ""
    if (curr_day/10 < 1):
        curr_date += "0"

    curr_date += f"{curr_day}/"

    if (curr_month/10 < 1):
        curr_date += "0"
    
    curr_date += f"{curr_month}/"
    curr_date += f"{curr_year}"

def progressTime():
    global curr_time, curr_hour, curr_minute
    if (curr_hour == 23 and curr_minute == 59):
        curr_hour = curr_minute = 0

    elif (curr_minute == 59):
        curr_minute = 0
        curr_hour += 1

    else:
        curr_minute += 1

    curr_time = ""
    if (curr_hour/10 < 1):
        curr_time += "0"

    curr_time += f"{curr_hour}:"

    if (curr_minute/10 < 1):
        curr_time += "0"
    
    curr_time += f"{curr_minute}"


if __name__ == "__main__":
    curr_date = "15/04/2024"
    curr_day, curr_month, curr_year = map(int, curr_date.split("/"))

    curr_time = "23:58"
    curr_hour, curr_minute = map(int, curr_time.split(":"))

    todew = ToDew()
    todew.menu()

"""
priority:
- 1: 1-2 days, 0-24 hours
- 2: 3-4 days
- 3: 5-7 days
- 4: 8-10 days
- 5: > 10 days
- 0: - days
"""