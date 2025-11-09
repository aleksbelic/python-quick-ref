import csv

# Reading from a CSV file:
with open('./data/user-data.csv') as my_csv_file:
    csv_reader = csv.reader(my_csv_file)
    for row in csv_reader:
        name, email, age = row
        print(f'Name: {name}, Email: {email}, Age: {age}')

'''
Name: Alice, Email:  alice@example.com, Age:  28
Name: Bob, Email:  bob@example.com, Age:  34
Name: Charlie, Email:  charlie@example.com, Age:  25
'''

# Reading from a CSV file with a header row:
with open('./data/user-data-with-header.csv') as my_csv_file_with_header:
    csv_dict_reader = csv.DictReader(my_csv_file_with_header)
    for row in csv_dict_reader:
        print(f'Name: {row["name"]}, Email: {row["email"]}, Age: {row["age"]}')

'''
Name: Alice, Email:  alice@example.com, Age:  28
Name: Bob, Email:  bob@example.com, Age:  34
Name: Charlie, Email:  charlie@example.com, Age:  25
'''

# Writing to a CSV file from a list of dictionaries:
some_user_data = [
    {'name': 'David', 'email': 'david@example.com', 'age': 30},
    {'name': 'Eva', 'email': 'eva@example.com', 'age': 22},
    {'name': 'Frank', 'email': 'frank@example.com', 'age': 27},
]
with open('./data/write-user-data.csv', 'w') as write_user_data_csv_file:
    csv_dict_writer = csv.DictWriter(write_user_data_csv_file, fieldnames=['name', 'email', 'age'])
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(some_user_data)