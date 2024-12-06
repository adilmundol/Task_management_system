Task Management System
Project Overview
The Simple Task Management System is a web-based application designed to simplify task management. It allows users to add, view, update, and delete tasks seamlessly. This project is built to showcase my skills in Frontend and Backend development.
Features
•	Add Tasks: Create tasks with a name, description, and due date.
•	View Tasks: Display a list of all tasks for easy tracking.
•	Update Task Status: Mark tasks as completed or pending.
•	Delete Tasks: Remove tasks that are no longer needed.
Technologies Used
•	Frontend: HTML, CSS, JavaScript
•	Backend: Django
•	Database: MySQL 
 I  implemented  this project using two methods:
    1. Django ORM(mentioned in urls)
Django’s built-in ORM was used for creating models and interacting with the database. ORM ensured smooth and secure data handling through the following:
•	Task creation
•	Querying task records
•	Updating and deleting tasks
   2. Fetch API(mentioned in urls)
The frontend interacts with the backend using the Fetch API for CRUD operations. This allows seamless communication between the frontend and the backend, ensuring real-time updates.
API Endpoints (For Backend)
•	GET /tasks: Retrieve all tasks.  http://127.0.0.1:8000/api/task/
•	POST /tasks: Create a new task. http://127.0.0.1:8000/api/task/add/
•	PUT /tasks/{id}: Update a task. http://127.0.0.1:8000/api/task/update/(id)/
•	DELETE /tasks/{id}: Delete a task. http://127.0.0.1:8000/api/task/delete/(id)/

Installation and Setup:
Ensure you have the following installed:
•	Python (for Django projects) 
•	MySQL
Steps to Run Locally
1.Clone the repository:
  git clone [repository link]  

2.Set up the virtual environment :
pip install virtualenv	
  	python3 -m venv venv_name
source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)

3. Navigate to the project directory
  cd task

4. Install the required Python packages    
pip install -r requirements.txt	
 

5. Set up the database:
•	Create a MySQL database and configure it in your settings file.(in xampp set db name=taskdata)
•	Upgrade version of MariaDB version 10.6.20
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'taskdata',
         'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',

    }
}

•	Run migrations:
             python manage.py makemigrations
             python manage.py migrate
6.1. sqlite database:
       In settings sqlite db is commented (if needed use sqlite instead of mysql)
7. Start the backend server:
python manage.py runserver  
(use port 8000)

Contribution:
This project was completed individually as part of an evaluation task.
Contact
If you have any questions or feedback, feel free to contact me:
•	Name: Adil M
•	Email: adilmundol@gmail.com

