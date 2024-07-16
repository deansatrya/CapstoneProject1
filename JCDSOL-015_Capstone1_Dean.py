import tabulate  
  
patient_data = [  
    {'ID': 1, 'Name': 'John Doe', 'Disease': 'Flu', 'Room': 1, 'Gender': 'Male', 'Age': 30, 'Address': 'Jalan 1'},  
    {'ID': 2, 'Name': 'Jane Doe', 'Disease': 'Covid', 'Room': 2, 'Gender': 'Female', 'Age': 25, 'Address': 'Jalan 2'},  
    {'ID': 3, 'Name': 'Bob Smith', 'Disease': 'Broken Leg', 'Room': 3, 'Gender': 'Male', 'Age': 40, 'Address': 'Jalan 3'},  
    {'ID': 4, 'Name': 'Alice Brown', 'Disease': 'Headache', 'Room': 4, 'Gender': 'Female', 'Age': 28, 'Address': 'Jalan 4'},  
    {'ID': 5, 'Name': 'Mike Davis', 'Disease': 'Fever', 'Room': 5, 'Gender': 'Male', 'Age': 35, 'Address': 'Jalan 5'}  
]  

backup_data = []  
  
def display_patient_data():  
    print(tabulate.tabulate(patient_data, headers='keys', tablefmt='pretty'))  
  
def add_patient_data():  
    while True:  
        id = input('Enter patient ID: ')  
        while not id.isdigit() or int(id) in [patient['ID'] for patient in patient_data]:  
            id = input('Invalid ID. Please enter a unique and valid ID: ')  
        name = input('Enter patient name: ').title()
        while not name.replace(' ', '').isalpha():
            name = input('Invalid name. Please enter a valid name: ').title()  
        disease = input('Enter disease: ').title()  
        while not disease.replace(' ', '').isalpha():  
            disease = input('Invalid disease. Please enter a valid disease: ').title()  
        room = input('Enter room number: ')  
        while not room.isdigit() or int(room) <= 0:  
            room = input('Invalid room number. Please enter a valid room number: ')  
        gender = input('Enter gender (Male/Female): ').title()
        while gender not in ['Male', 'Female']:  
            gender = input('Invalid gender. Please enter Male or Female: ') .title() 
        age = (input('Enter age: '))  
        while not age.isdigit() or int(age) <= 0:  
            age = (input('Invalid age. Please enter a valid age: '))
        address = input('Enter address: ').title()   
        while not address:  
            address = input('Invalid address. Please enter a valid address: ').title()
        patient_data.append({'ID': int(id), 'Name': name, 'Disease': disease, 'Room': int(room), 'Gender': gender, 'Age': age, 'Address': address})    
        print('Patient data added successfully!')  
        cont = input('Do you want to add another patient? (y/n): ')  
        if cont.lower()!= 'y':  
            break  
  
def update_patient_data():  
    while True:  
        id = input('Enter patient ID to update: ')  
        while not id.isdigit():  
            id = input('Invalid ID. Please enter a valid ID: ')  
        id = int(id)  
        for patient in patient_data:  
            if patient['ID'] == id:  
                name = input('Enter new name: ').title()  
                while not name.replace(' ', '').isalpha():  
                    name = input('Invalid name. Please enter a valid name: ').title()   
                patient['Name'] = name  
                disease = input('Enter new disease: ').title()   
                while not disease.replace(' ', '').isalpha():
                    disease = input('Invalid disease. Please enter a valid disease: ').title()   
                patient['Disease'] = (disease)  
                room = input('Enter new room number: ')  
                while not room.isdigit() or int(room) <= 0:  
                    room = input('Invalid room number. Please enter a valid room number: ')  
                patient['Room'] = room  
                gender = input('Enter new gender (Male/Female): ').title() 
                while gender not in ['Male', 'Female']:  
                    gender = input('Invalid gender. Please enter Male or Female: ').title()  
                patient['Gender'] = gender  
                age = input('Enter new age: ')  
                while not age.isdigit() or int(age) <= 0:  
                    age = input('Invalid age. Please enter a valid age: ')  
                age = int(age)  
                patient['Age'] = age  
                address = input('Enter new address: ').title()   
                while not address:  
                    address = input('Invalid address. Please enter a valid address: ').title()   
                patient['Address'] = address  
                print('Patient data updated successfully!')  
                return  
        print('Patient not found!')  
        cont = input('Do you want to try again? (y/n): ')  
        if cont.lower()!= 'y':  
            break  
  
def delete_patient_data():  
    global backup_data  
    while True:  
        id_or_name = input('Enter patient ID or name to delete: ').title()  
        for patient in patient_data:  
            if id_or_name.isdigit() and patient['ID'] == int(id_or_name) or patient['Name'] == id_or_name:  
                backup_data.append(patient)  
                patient_data.remove(patient)  
                print('Patient data deleted successfully!')  
                return  
        print('Patient not found!')  
        cont = input('Do you want to try again? (y/n): ')  
        if cont.lower()!= 'y':  
            break  
  
def filter_patient_data():  
    while True:  
        filter_by = input('Filter by (Disease, Gender, Age): ').title()
        while filter_by not in ['Disease', 'Gender', 'Age']:  
            filter_by = input('Invalid filter. Please enter disease, gender, or age: ').title()  
        filter_value = input('Enter filter value: ').title()
        while not filter_value.replace(' ', '').isalpha(): 
            filter_value = input('Invalid filter value. Please enter a valid value: ').title()  
        filtered_data = [patient for patient in patient_data if patient[filter_by.title()] == filter_value]  
        if filtered_data:  
            print(tabulate.tabulate(filtered_data, headers='keys', tablefmt='pretty'))
        else:  
            print('No matching data found!')  
        cont = input('Do you want to filter again? (y/n): ')  
        if cont.lower()!= 'y':  
            break  
  
def display_deleted_data():  
    if backup_data:
        backup_data.sort(key=lambda x: x['ID'])
        print(tabulate.tabulate(backup_data, headers='keys', tablefmt='pretty'))  
    else: 
        print('No deleted data available!')  
  
def undo_delete():  
    if backup_data:  
        id_or_name = input('Enter patient ID or name to restore: ').title()  
        for patient in backup_data:  
            if id_or_name.isdigit() and patient['ID'] == int(id_or_name) or patient['Name'] == id_or_name:  
                patient_data.append(patient)
                patient_data.sort(key=lambda x: x['ID'])  #membuat function yang fungsi nya untuk me return list yang berisi kolom id1
                backup_data.remove(patient)  
                print('Patient data restored successfully!')  
                return  
        print('Patient not found!')  
    else:  
        print('No deleted data available to restore!')  
  
def exit_program():  
    print('Exiting program. Goodbye!')  
  
while True:
    print('')  
    print('Hospital Patient Management System')  
    print('1. Display patient data')  
    print('2. Add patient data')  
    print('3. Update patient data')  
    print('4. Delete patient data')  
    print('5. Filter patient data')  
    print('6. Display deleted data')  
    print('7. Undo delete')  
    print('8. Exit')  
    choice = input('Enter your choice: ')
    print('')  
    if choice == '1':  
        display_patient_data()  
    elif choice == '2':  
        add_patient_data()  
    elif choice == '3':  
        update_patient_data()  
    elif choice == '4':  
        delete_patient_data()  
    elif choice == '5':  
        filter_patient_data()  
    elif choice == '6':  
        display_deleted_data()  
    elif choice == '7':  
        undo_delete()  
    elif choice == '8':  
        exit_program()  
        break  
    else:  
        print('Invalid choice. Please try again!')
