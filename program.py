# # question 1-----------------------------------------
# numbers = []

# # Take 5 integer inputs from the user
# for i in range(5):
#     num = int(input(f"Enter integer {i + 1}: "))
    
#     # Check if the number is greater than or equal to 9
#     if num >= 9:
#         # Add the number to the list of valid numbers
#         numbers.append(num)

# # Calculate the sum of the remaining numbers
# sum_of_numbers = sum(numbers)

# # Print the result
# print(f"The sum of numbers greater than or equal to 9 is: {sum_of_numbers}")



        
# # question 2 -----------------------------------------------------------------------
# # Taking input for the first integer
# num1 = int(input("Enter the first integer: "))

# # Taking input for the second integer
# num2 = int(input("Enter the second integer: "))

# # Calculating and printing the product
# product = num1 * num2
# print(f"The product of {num1} and {num2} is: {product}")

# # if product > 500:
# if product > 500:
#     # Calculating and printing the sum
#     total_sum = num1 + num2
#     print(f"The product is greater than 500. The sum of {num1} and {num2} is: {total_sum}")

# elif product < 500:
#     # Printing a message
#     print("Hello! LNB code is running.")

# else:
#     # Printing the product
#     print(f"The product of {num1} and {num2} is: {product}")
    
    
    
    
# # question 3----------------------------------------------------------------------
# user_input = input("Enter a string: ")

# # Calculate the length of the string
# length_of_string = len(user_input)

# # Display characters based on the specified conditions
# if length_of_string > 7:
#     # Display only those characters present in even index numbers
#     result_string = user_input[::2]
#     print(f"The length is greater than 7. Characters at even indices: {result_string}")
# else:
#     # Display only those characters present in odd index numbers
#     result_string = user_input[1::2]
#     print(f"The length is less than or equal to 7. Characters at odd indices: {result_string}")




# question 4-------------------------------------------------------------------
   
# L1 = [11, 21, 24, 12, 18]
# L2 = [14, 44, 25, 37, 13]

# # Create a new list L3 containing items in the specified pattern
# L3 = L1[1::2] + L2[::2]

# # Print the result
# print("List L1:", L1)
# print("List L2:", L2)
# print("List L3:", L3)

# # Create a new list L3 containing items in the specified pattern
# L3 = L1[1::2] + L2[::2]

# # Print the result
# print("List L1:", L1)
# print("List L2:", L2)
# print("List L3:", L3)
# L2 = []

# # Create a new list L3 containing items in the specified pattern
# L3 = L1[1::2] + L2[::2]

# # Print the result
# print("List L1:", L1)
# print("List L2:", L2)
# print("List L3:", L3)



#password generator ======================
# a= (input("enter your name "))
# b= (input("enter your mail id "))
 
 
import random
import string

generatepassword= ("length =12")
all_characters = string.ascii_letters + string.digits + '@'
password = ( random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) +'@' +''.join(random.choice(all_characters)) )
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)
generatedpassword = generatepassword()
print("Generated Password:", generatedpassword)




#question 6===========================================================
import csv
from datetime import datetime

def create_csv():
    csv_file_path = input("Enter the path for the CSV file (e.g., data.csv): ")
    
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Amount', 'DOB']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header to the CSV file
        writer.writeheader()

        # User input for creating the CSV file
        while True:
            id_input = input("Enter ID (10 characters - first 5 uppercase letters, last 5 digits): ")
            amount_input = float(input("Enter Amount: "))
            dob_input = input("Enter DOB (YYYY-MM-DD): ")

            # Write the user input to the CSV file
            writer.writerow({'ID': id_input, 'Amount': amount_input, 'DOB': dob_input})

            add_more = input("Do you want to add more entries? (yes/no): ").lower()
            if add_more != 'yes':
                break

def validate_id_dob(id_value, dob_value):
    # Validate ID format
    if len(id_value) == 10 and id_value[:5].isalpha() and id_value[5:].isdigit():
        # Validate DOB format
        try:
            datetime.strptime(dob_value, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    return False

def process_csv(csv_file_path):
    data = {}

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Process each row in the CSV file
        for row in reader:
            id_value = row['ID']
            dob_value = row['DOB']

            if validate_id_dob(id_value, dob_value):
                key = (id_value, dob_value)
                if key in data:
                    # If entry already exists, merge the amounts
                    data[key]['Amount'] += float(row['Amount'])
                else:
                    # Otherwise, create a new entry
                    data[key] = {
                        'ID': id_value,
                        'Amount': float(row['Amount']),
                        'DOB': dob_value,
                        'Verification': 'Verified'
                    }
            else:
                # If ID or DOB is invalid, mark as 'Invalid'
                row['Verification'] = 'Invalid'
                data[(id_value, dob_value)] = row

    # Write the processed data back to the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Amount', 'DOB', 'Verification']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in data.values():
            writer.writerow(entry)

if __name__ == "__main__":
    create_csv()
    csv_file_path = input("Enter the path of the CSV file to process: ")
    process_csv(csv_file_path)
    print("Processing complete. Check the CSV file for results.")


    
    






#question 7=========================================================
import csv
from datetime import datetime

def create_csv():
    csv_file_path = input("Enter the path for the CSV file (e.g., data.csv): ")
    
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Amount', 'DOB']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header to the CSV file
        writer.writeheader()

        # User input for creating the CSV file
        while True:
            id_input = input("Enter ID (10 characters - first 5 uppercase letters, last 5 digits): ")
            amount_input = float(input("Enter Amount: "))
            dob_input = input("Enter DOB (YYYY-MM-DD): ")

            # Write the user input to the CSV file
            writer.writerow({'ID': id_input, 'Amount': amount_input, 'DOB': dob_input})

            add_more = input("Do you want to add more entries? (yes/no): ").lower()
            if add_more != 'yes':
                break

def validate_id_dob(id_value, dob_value):
    # Validate ID format
    if len(id_value) == 10 and id_value[:5].isalpha() and id_value[5:].isdigit():
        # Validate DOB format
        try:
            datetime.strptime(dob_value, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    return False

def process_csv(csv_file_path):
    data = {}

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Process each row in the CSV file
        for row in reader:
            id_value = row['ID']
            dob_value = row['DOB']

            if validate_id_dob(id_value, dob_value):
                key = (id_value, dob_value)
                if key in data:
                    # If entry already exists, merge the amounts
                    data[key]['Amount'] += float(row['Amount'])
                else:
                    # Otherwise, create a new entry
                    data[key] = {
                        'ID': id_value,
                        'Amount': float(row['Amount']),
                        'DOB': dob_value,
                        'Verification': 'Verified'
                    }
            else:
                # If ID or DOB is invalid, mark as 'Invalid'
                row['Verification'] = 'Invalid'
                data[(id_value, dob_value)] = row

    # Write the processed data back to the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Amount', 'DOB', 'Verification']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in data.values():
            writer.writerow(entry)

if __name__ == "__main__":
    create_csv()
    csv_file_path = input("Enter the path of the CSV file to process: ")
    process_csv(csv_file_path)
    print("Processing complete. Check the CSV file for results.")















    
    
    
    
# import random
# import string

# def generate_password(length=12):
#     # Combine letters, digits, and special characters
#     all_characters = string.ascii_letters + string.digits + '@'

#     # Ensure at least one uppercase letter, one lowercase letter, one digit, and one '@' symbol
#     password = (
#         random.choice(string.ascii_uppercase) +
#         random.choice(string.ascii_lowercase) +
#         random.choice(string.digits) +
#         '@' +
#         ''.join(random.choice(all_characters) for _ in range(length - 4))
#     )

#     # Shuffle the password to make it more random
#     password_list = list(password)
#     random.shuffle(password_list)
#     final_password = ''.join(password_list)

#     return final_password

# # Generate the password
# generated_password = generate_password()

# # Print the generated password
# print("Generated Password:", generated_password)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
