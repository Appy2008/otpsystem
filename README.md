Features-
1. App is login protected.  That is, to view its content, users must be logged in. 
2. If a visiting user is already logged in, they will be presented with their email address. 
3. If a visiting user is not logged in, they will be presented with a login screen.  To login into the application:
 a. User enter their email address and presses “Request OTP” button
 b. At this point, the application makes a HTTP POST request to the backend
 c. Backend returns 200 OK if OTP was successfully generated 
d. Backend returns non-200 status code upon errors 
e. Backend will simply print the generated OTP on backend terminals 
f. Generated OTPs will be unique and completely random 
g. As a user, goto backend terminal and copy the printed OTP code 
h. Enters the OTP on the web page and presses “Verify OTP” button 
i. At this point, application makes a HTTP POST request to backend

Setup instructions
1) Install Python, Django and the dependencies (using pip installer)
2) Clone the project on local and open in any code editor
3) Make migrations to initiate and create database using commands
a) python manage.py makemigrations
b) python manage.py migrate
4) Run the server on local using command
python manage.py runserver
