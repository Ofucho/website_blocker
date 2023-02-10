import time  # Import the time module
from datetime import datetime as dt  # Import the datetime module and rename it as "dt" for ease of use

host_temp = 'hosts'  # Define a variable for the file name
host_path = r"C:\Windows\System32\drivers\etc\hosts"  # Define a variable for the file path
redirect = '127.0.0.1'  # Define a variable for the redirect IP address
website_list = ['www.instagram.com', 'instagram.com', 'www.facebook.com', 'facebook.com',
                'www.twitter.com', 'twitter.com', 'www.linkedin.com', 'linkedin.com', 'www.gmail.com', 'gmail.com']  # Define a list of websites to block

while True:  # Enter an infinite loop
    start_work = dt(dt.now().year, dt.now().month, dt.now().day, 1)  # Define the start of work hours as 5am of the current day
    end_work = dt(dt.now().year, dt.now().month, dt.now().day, 19)  # Define the end of work hours as 7pm of the current day
    if start_work < dt.now() < end_work:  # Check if the current time is within work hours
        print('Coding time...')
        with open(host_path, 'r+') as file:  # Open the "hosts" file in read and write mode
            content = file.read()  # Read the contents of the file
            for site in website_list:  # Loop through the list of websites to block
                if site in content:  # If the website is already in the file, skip it
                    pass
                else:
                    file.write(redirect+' '+site+'\n')  # If the website is not in the file, add it
    else:
        with open(host_path,'r+') as file:  # Open the "hosts" file in read and write mode
            content = file.readlines()  # Read the contents of the file as lines
            file.seek(0)  # Set the file pointer to the beginning of the file
            for line in content:  # Loop through the lines
                if not any(site in line for site in website_list):  # Check if the line contains a website in the list
                    file.write(line)  # If not, write the line to the file
            file.truncate()  # Truncate the file to remove any unnecessary lines
        print('Alert!!! Burnout..')  # Print a message
    time.sleep(5)  # Pause the loop for 5 seconds
