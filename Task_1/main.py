def total_salary(path):
    salaryList =[]
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
         
            for line in lines:
               _ , salary = line.strip().split(",")

               salaryList.append(int(salary))
        totalSum = sum(salaryList)
        averageSum = int( totalSum / len(salaryList) )     
        return totalSum, averageSum
    
    except Exception as e:
        print("The file is not found or its contents are corrupted") 
        return None, None   

totalSum ,averagaSum = total_salary("D:\\goit-algo-hw-04\\Task_1\\salary.txt")  
print(f"The total amount of wages: {totalSum} , Average salary: {averagaSum}")  