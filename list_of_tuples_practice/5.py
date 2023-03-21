emp_db = []
n = int(input("enter the num:"))
for id in range(1001,1001+n):
    emp_name = input("enter name:")
    emp_salary = int(input("enter "))
    emp_ph_no = int(input("enter the ph-no:"))
    res = (id,emp_name,emp_salary,emp_ph_no)
    emp_db.append(res)
    print()
print(emp_db)