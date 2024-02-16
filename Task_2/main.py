def get_cats_info(path):
    catsInfoList = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                id, name , age = line.strip().split(",")
                catsInfoList.append({"id" :id, "name" :name, "age" :age})
        return catsInfoList     
    except Exception as e:
        print("The file is not found or its contents are corrupted") 
        return None, None        
    
result = get_cats_info("D:\\goit-algo-hw-04\\Task_2\\catsList.txt") 
print(result) 