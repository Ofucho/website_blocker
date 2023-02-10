README

This code is designed to block access to websites during working hours and allow access to these websites outside working hours.

Dependencies
Python 3
time library
datetime library
Usage
Clone this repository to your local machine
Replace the file path for host_path with the location of your system's hosts file.
Replace the websites in the website_list with the websites you want to block access to.
Run the code with python filename.py
Functionality
The code sets the working hours to be from 5am to 7pm, this can be changed by modifying the start_work and end_work variables.
If the current time is within working hours, the code will block access to the websites in website_list by adding redirects to the hosts file.
If the current time is outside working hours, the code will remove the redirects to the website_list websites in the hosts file, allowing access.
Note
Make sure to run the code as an administrator to have sufficient permissions to modify the hosts file.
This code is meant for Windows operating systems, the location of the hosts file may be different for other operating systems.
This code should be used at your own discretion and the author is not responsible for any potential harm caused by running this code.
