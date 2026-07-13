salary1 = [25000, 30000, 45000]
salary2 = [28000, 35000, 40000]

all_salary = []

for i in salary1:
    all_salary.append(i)

for i in salary2: 
    all_salary.append(i)

all_salary.sort() 

print("Employee Salary Report:")  
print(all_salary)