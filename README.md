
# Django, Docker Container and GCP App Engine

This is a simple project using Python, Django, Bootstrap, MySQL as project implementation.
Whereas, Docker and App Engine are used for deployment (Note: Both Deployments are done seprately). 
The project is simple application with few features that include Authentication followed by few forms
having CURD operations and you can export the data to excel format as well.





## Installation

To install this project navigate to the directory "BuildingProperApp" 
then follow the instructions below.

Building a virtual environment:
Creating virtual envirnment is necessary to avoid any unwanted issue
that arise. More than that to avoid poluting local Python envirnment.

```bash
  Python -m venv venv
```
Here second venv is directory name where your environment would be created.
You can name is what ever you want. Now you need to activate the virtual 
envirnment. Activating virtual envirnemnet varies the type of 
operating system  you are using.

Windows 
```bash
  venv\Scripts\activate
```

Linux\MacOs
```bash
  source venv/bin/activate
```
Your Output would be some what like this.
```bash
  (venv) ..\DjangoApplication\BuildingProperApp
```
Now as you have sucessfully activated your virtual environment lets move
toward installing dependencies. Now run the following bash command in your activated
envirnment this will install your project dependencies.

Navigate to Registration directory
```bash
  cd Registration
```
After this 
```bash
  pip install -r requirements.txt
```
This will install all the necessary required for running this project. 

Database Requirement:

If you want to run this project locally then you need an active MySQL 
database server running. Where you need to open new database name "DB1".
You can do this in 2 ways either using MySQL bash session or MySQL workbench
using GUI. When using bash session you can run the following query.

```bash
  create database DB1;
```

## Running Application

Finally if you are well aware of Using Django framework than you don't need help from here
you can skip this part. This section will include testing server and making migrations.

Testing server by running requires you to navigate to the directory where your "manage.py" 
reside. In our case it resides in Registration directory. After it please run the following command.

```bash
  python manage.py runserver
```
Hopefully you will get this output
```bash
Django version 2.2, using settings 'Registration.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Our server is running sucessfully. 8000 is the default port for Django applications.

To apply migrations please run the following command.

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

The impact of these commands can be seen after running it. The end result 
of this would be an application runnning locally.

## Deployment at Docker Containers


## Deployment at GCP App Engine
