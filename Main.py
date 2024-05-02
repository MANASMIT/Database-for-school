import Modules as md
def main():
    entity_type = ['Departments', 'Teachers', 'Students']
    while True:
        print("Select an entity type:")
        for i, entity in zip(range(1, 5), entity_type):
            print(f"{i}. {entity}")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == '0':
            break
        try:
            choice = int(choice)
            if choice not in range(1, 4):
                raise ValueError
        except ValueError:
            print("Please enter a number between 1 and 3")
            continue    

        selected_entity  = entity_type[choice - 1]
        filename = selected_entity + ".json"
        entity_data = md.load_data(filename)
        
        while True:
            print(f"\nOptions for {selected_entity}: \n 1.Add \n 2.Delete \n 3.Search \n 4.Modify \n 0.Exit")
            operation = input("Enter operation number:")

            if operation == '0':
                break
            
            elif operation == '1':
                if(choice == 1):
                    entity_data = md.add_department(entity_data)
                    md.save_data(filename, entity_data)
                    print("Department added successfully.")

                elif (choice == 2):
                    entity_data = md.add_teacher(entity_data)
                    md.save_data(filename, entity_data)
                    print("Teacher added successfully.")

                elif (choice == 3):
                    entity_data = md.add_student(entity_data)
                    md.save_data(filename, entity_data)
                    print("Student added successfully.")

            elif operation == '2':
                length = len(entity_data) + 1
                for entity in entity_data[selected_entity]:
                    my_list = list(entity.items())
                    for i in range(0,length):
                        print(my_list[i][0], ':', my_list[i][1])
                    print()
                entity_id = input("Enter ID of the entity to delete: ")
                entity_ids = int(entity_id)  
                entity_data = md.delete_entity(entity_data, entity_ids,selected_entity)
                md.save_data(filename, entity_data)
                print("Entity deleted successfully.")

            elif operation == '3': 
                search_name = input("Enter name to search: ")
                x = md.search_entity(entity_data, search_name,selected_entity)

            elif operation == '4':
                x = int(input("DO you want to view the content of this entity before modifing? \n 1.Yes \n 2.No \n"))
                if x == 2:
                    pass
                elif x == 1:
                    length = len(entity_data) + 1
                    for entity in entity_data[selected_entity]:
                        my_list = list(entity.items())
                        for i in range(0,length):
                            print(my_list[i][0], ':', my_list[i][1])
                        print()
                id = int(input("Enter id value of the group which you want to modify: "))
                mod = md.modify_entity(entity_data,id,selected_entity)
                md.save_data(filename, mod)

if __name__ == "__main__":
    main()