import re
class Expense_Tracker:
  def __init__(self):
    pass 
  def info(self):
    self.date=input("Enter a date: ").strip()
    self.category=input("Enter category: ").strip()
    self.description=input("Enter description: ").strip()
    while True:
      try:
        self.amount=input("Enter amount: ").strip()
        float(self.amount)
        break
      except ValueError:
        print("Invalid amount. Please enter a valid number.")
    with open("file.txt","a") as f:
      f.write("________________________\n")
      f.write(f"Date: {self.date}\n")
      f.write(f"Category: {self.category}\n")
      f.write(f"Description: {self.description}\n")
      f.write(f"Amount: {self.amount}\n")
      f.write("Expense added successfully!\n")
      f.write("___________________________\n")
  def view(self):
    with open("file.txt","r") as f:
      lines=f.readlines()
      if not lines:
        print("No expenses recorded yet.")
        return
      for line in lines:
        print(line,end='')
  def search_by_date(self):
    user_date=input("Enter a date: ").strip()
    with open("file.txt","r") as f:
      lines=f.readlines()
      pattern = rf"Date:\s*{user_date}"
      found=False
      for i in range(len(lines)):
          if re.search(pattern,lines[i]):
            print("".join(lines[i-1:i+6]))
            found=True
      if not found:
        print("No expense found of that date")
  def total_spending(self):
    total = 0
    pattern = r"Amount:\s*(\d+(?:\.\d+)?)"
    with open("file.txt","r") as f:
      lines=f.readlines()
      for line in lines:
        match = re.search(pattern, line)
        if match:
          amount=float(match.group(1))
          total+=amount
    if total==0:
      print("No expense found")
    else:
      print(f"Total spending: ₹{total:.2f}")
  def search_by_category(self):
    user_category=input("Enter the category: ").strip()
    pattern = rf"Category:\s*{user_category}"
    found=False
    with open("file.txt","r") as f:
      lines=f.readlines()
      for i in range(len(lines)):
        if re.search(pattern, lines[i], re.IGNORECASE):
          print("".join(lines[i-1:i+6]))
          found=True
      if not found:
        print("No expense found for that category")
  def delete_all_expenses(self):
    confirm=input("Enter do you really want to delete (yes/no): ").lower().strip()
    if confirm == "yes":
       open("file.txt", "w").close() 
       print("All expense have been deleted successfully!")
    else:
      print("Action cancelled")
  def delete_by_date(self):
    user_date=input("Enter a date: ").strip()
    pattern= rf"Date:\s*{user_date}"
    with open("file.txt","r") as f:
      lines=f.readlines()
      new_lines=[]
      skip=False
      deleted=False
      for i in range(len(lines)):
        line=lines[i]
        if re.search(pattern,line):
          deleted = True
          skip=True
          start = max(0, i-1)
          end = min(len(lines), i+6)
          print("".join(lines[start:end]))
          continue
        if skip and "___________________________" in line:
          skip=False
          continue
        if not skip:
          new_lines.append(line)
    with open("file.txt","w") as f:
      f.writelines(new_lines)
    if deleted:
      print(f"Expense of date {user_date} deleted successfully")
    else:
      print("No expense found for that date")
  def delete_by_category(self):
    user_category=input("Enter a category: ").strip()
    pattern = rf"Category:\s*{user_category}"
    with open("file.txt","r") as f:
      lines=f.readlines()
      new_lines=[]
      skip=False
      deleted=False
      for i in range(len(lines)):
        line=lines[i]
        if re.search(pattern,line):
          deleted = True
          skip=True
          start = max(0, i-1)
          end = min(len(lines), i+6)
          print("".join(lines[start:end]))
          continue
        if skip and "___________________________" in line:
          skip=False
          continue
        if not skip:
          new_lines.append(line)
    with open("file.txt","w") as f:
      f.writelines(new_lines)
    if deleted:
      print(f"Expense for the category {user_category} deleted successfully")
    else:
      print("No expense found for that category")
  def edit_expense(self):
    while True:
      user_date=input("Enter the date which you want to edit: ")
      pattern=rf"Date:\s*{user_date}"
      with open("file.txt","r") as f:
        lines=f.readlines()
        found=False
        for i in range(len(lines)):
          line=lines[i]
          if re.search(pattern,line):
            found=True
            start = max(0, i-1)
            end = min(len(lines), i+6)
            print("".join(lines[start:end]))
            new_value=input("\nWhat you want to edit (date/category/description/amount): ").strip().lower()
            if new_value=="date":
              new_date=input("Enter new date: ").strip()
              lines[i]=f"Date: {new_date}\n"
            elif new_value=="category" and i+1 < len(lines):
              new_category=input("Enter new category: ").strip()
              lines[i+1]=f"Category: {new_category}\n"
            elif new_value=="description" and i+2 < len(lines):
              new_description=input("Enter new description: ").strip()
              lines[i+2]=f"Description: {new_description}\n"
            elif new_value=="amount" and i+3 < len(lines):
              new_amount=input("Enter new amount: ").strip()
              lines[i+3]=f"Amount: {new_amount}\n"
            else:
              print("Invalid option")
              return
            break
      if found:
        with open("file.txt","w") as f:
          f.writelines(lines)
          print("\n✅ Expense updated successfully!")
          print("🔁 Updated entry:")
          print("".join(lines[max(0, i-1):min(len(lines), i+6)]))
      else:
        print("No expense found for that date")
      more_want=input("Do you want to edit more expense(yes/no): ").lower()
      if more_want!="yes":
        break
print("_________Welcome To The Expense_Tracker_________")
obj=Expense_Tracker()
while True:
  menu=input("\nWhat you want to do\n"
  "1.Add_expense\n"
  "2.View_expense\n"
  "3.Search_by_date\n"
  "4.Search_by_category\n"
  "5.Total_spending\n"
  "6.Delete_Expense_by_date\n"
  "7.Delete_Expense_by_category\n"
  "8.Delete_all_expense\n"
  "9.Edit_expense\n"
  "Enter a number(1-9) or 'q' to quit: ").strip()
  if menu == "q":
    break
  elif menu=="1":
    obj.info()
  elif menu=="2":
    obj.view()
  elif menu=="3":
    obj.search_by_date()
  elif menu=="4":
    obj.search_by_category()
  elif menu=="5":
    obj.total_spending()
  elif menu=="6":
    obj.delete_by_date()
  elif menu=="7":
    obj.delete_by_category()
  elif menu=="8":
    obj.delete_all_expenses()
  elif menu=="9":
    obj.edit_expense()
  else:
    print("Invalid input!Please enter number(1/2/3/4/5/6/7/8/9)")