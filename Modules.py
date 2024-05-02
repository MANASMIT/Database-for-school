import json
from datetime import datetime
def val_date(input):
    try:
        datetime.strptime(input,'%d/%m/%Y')
    except ValueError:
        print("Invalid date format")
    else:
        return True
    
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_department(data):
    date = input("Enter creation date as DD/MM/YYYY: ")
    if val_date(date) == True:
        new_department = {
                "id": len(data['Departments']) + 1,
                "creation_date": date,
                "name": input("Enter department name: ")
            }   
    data['Departments'].append(new_department)
    return data

# Function to add a record for a teacher
def add_teacher(data):
    new_teacher = {
        "id": len(data['Teachers']) + 1,
        "name": input("Enter teacher name: "),
        "subject": input("Enter subject taught: "),
        "department_id": int(input("Enter department: ")),
        "address": input("Enter address: "),
        "phone_no": input("Enter phone number: ")
    }
    data['Teachers'].append(new_teacher)
    return data

# Function to add a record for a student
def add_student(data):
    new_student = {
        "id": len(data['Students']) + 1,
        "name": input("Enter student name: "),
        "roll_no": input("Enter roll number: "),
        "subject": input("Enter subject: "),
        "marks": int(input("Enter marks: ")),
        "department": input("Enter department: ")
    }
    data['Students'].append(new_student)
    return data

def delete_entity(data, id, sele):
    for i in data[sele]:
        if i["id"] == id:
            index_to_remove = id-1
            break

    if index_to_remove != None:
        removed_department = data["Departments"].pop(index_to_remove)
        print("Removed department:", removed_department)
    else:
        print("Department with id =", id, "not found")
    return data

def search_entity(data, search_query,sele):
        length = len(data) + 1
        found = False
        try:
            for entity in data[sele]:
                    if entity['name'] == search_query:
                        print("\n", sele,"Information:")
                        my_list = list(entity.items())
                        for i in range(0,length):
                            print(my_list[i][0], ':', my_list[i][1])
                        print("Data found corresponding to query name")
                        found = True
        except Exception as e:
            print("Error occurred while searching:",e)
        if found == False:
            print(f"No entities matching query name ",'"'+search_query+'"', "found under",sele)

def modify_entity(data, id,sele):
    for entity in data[sele]:
        if entity["id"] == id:
            print("Which key parameter do you want to change?")
            key = input("Enter key here: ")
            if key in entity:
                print("Which value do you want to change it to?")
                value = input("Enter value here: ")
                entity[key] = value
    return data

