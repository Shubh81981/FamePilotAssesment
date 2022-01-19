
data = {"aman.py":"aman","aman.txt":"aman","shubham.py":"shubham"}
def group_by_owners(file):
    n = int(input("enter how many people data you want to enter: "))
    for value in range(n):
        owner_name = input("enter owner name: ")
        file_name = input("enter file name: ")
        data[file_name] = owner_name
        
    temp_dict = {}
    for key,value in data.items():
        if value not in temp_dict:
            temp_dict[value]=[key]
        else:
            temp_dict[value].append(key)
    print(temp_dict)


group_by_owners(data)




