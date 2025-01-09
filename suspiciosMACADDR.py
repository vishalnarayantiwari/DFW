import csv


def find_suspicious_devices(file_path):

  # List of allowed vendors

  allowed_vendors = ["HP", "Dell"]


  # Open the CSV file

  with open(file_path, 'r') as file:

    reader = csv.DictReader(file)

     

    # List to store suspicious MAC addresses

    suspicious_devices = []


    # Iterate through each row in the file

    for row in reader:

      vendor = row['Vendor']

      mac_address = row['MAC Address']

       

      # Check if the vendor is not in the allowed list

      if vendor not in allowed_vendors:

        suspicious_devices.append(mac_address)


  # Print the suspicious MAC addresses

  print("Suspicious MAC Addresses:")

  for mac in suspicious_devices:

    print(mac)


# Specify the input file

file_path = 'pre_process.csv'


# Call the function

find_suspicious_devices(file_path)

#give csv file
#python3 q16.py
