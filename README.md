
# Django, Docker Container and GCP App Engine

This is a simple project using Python, Django, Bootstrap, MySQL as project implementation.
Whereas, Docker and App Engine are used for deployment (Note: Both Deployments are done seprately.
This git repo have 3 branches. Main, Docker-Container and AppEngine ). 
The project is simple application with few features that include Authentication followed by few forms
having CURD operations and you can export the data to excel format as well.





## Installation

To install this project navigate to the directory "SalesPurchase" 
then follow the instructions below.

Building a virtual environment:
Creating virtual enviornment is necessary to avoid any unwanted issue
that arise. More than that to avoid poluting local Python environment.

```bash
  Python -m venv venv
```
Here second venv is directory name where your environment would be created.
You can name is what ever you want. Now you need to activate the virtual 
environment. Activating virtual environmnet varies the type of 
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
  (venv) ..\SalesPurchase\venv\Scripts>
```
Now as you have sucessfully activated your virtual environment lets move
toward installing dependencies. Now run the following bash command in your activated
environment this will install your project dependencies.

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
Deployment at docker not required much effort just checkout Docker-Container
branch. Here 2 new files are added one is docker compose file and other is DockerFile.
Just run the below mentioned command the app would be deployed locally on your docker 
in the form of container make sure you are using a proper internet connection. What I 
personally experience is I was using cisco anyconnect where mysql container was running 
but when the application container try to connect mysql container it gives error can't 
connect to mysql.

There would be 2 standalone continer MySQl and Python-Django.
```bash
  docker-compose up -d db
```

```bash
  docker-compose up -d web
```
you just run two services 1 is for MySQl database and other is python
mentioned in docker-compose file. Now your app would be deployed at localhost port 9000.

## Deployment at GCP App Engine
I use the same application for deploymment in Gcloud App Engine. You can only deploy 
1 app each project. You need to register your app url in setting.py file in "ALLOWED_HOSTS".
create app.yaml , .gcloudignore and main.py files and paste the below mentioned code in those files.
before that just create a new database with name "DB1" at Gcloud SQL MySQl.

app.yaml
```bash
# [START django_app]
runtime: python37
handlers:
# This configures Google App Engine to serve the files in the app's
# static directory.
- url: /static
  static_dir: static/
# This handler routes all requests not caught above to the main app. 
# It is required when static routes are defined, but can be omitted 
# (along with the entire handlers section) when there are no static 
# files defined.
- url: /.*
  script: auto  
# [END django_app]
```

.gcloudignore
```bash
# This file specifies files that are *not* uploaded to Google Cloud
# using gcloud. It follows the same syntax as .gitignore, with the addition of
# "#!include" directives (which insert the entries of the given .gitignore-style
# file at that point).
#
# For more information, run:
#   $ gcloud topic gcloudignore
#
.gcloudignore
# If you would like to upload your .git directory, .gitignore file or files
# from your .gitignore file, remove the corresponding line
# below:
#.git
#.gitignore

# Python pycache:
__pycache__/
# Ignored by the build system
/setup.cfg
```
main.py
```bash
from Registration.wsgi import application
# App Engine by default looks for a main.py file at the root of the app
# directory with a WSGI-compatible object called app.
# This file imports the WSGI-compatible object of the Django app,
# application from mysite/wsgi.py and renames it app so it is
# discoverable by App Engine without additional configuration.
# Alternatively, you can add a custom entrypoint field in your app.yaml:
# entrypoint: gunicorn -b :$PORT mysite.wsgi
app = application
```


Add cloud_sql_proxy to your project root directry available at gcloud documentation
where your manage.py resides and follow the instruction mentioned with that documentation
to connect your app running locally connected with cloud database and run all the migrations.

Now replace the DATABASES present in settings.py with the below mentioned script with
your Gcloud database credentials.

```bash
# [START db_setup]
if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/[YOUR-CONNECTION-NAME]',
            'USER': '[YOUR-USERNAME]',
            'PASSWORD': '[YOUR-PASSWORD]',
            'NAME': '[YOUR-DATABASE]',
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect 
    # to Cloud SQL via the proxy.  To start the proxy via command line: 
    #    $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306 
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': '[YOUR-DATABASE]',
            'USER': '[YOUR-USERNAME]',
            'PASSWORD': '[YOUR-PASSWORD]',
        }
    }
# [END db_setup]
```

All of these steps are already done in git repo, you just need to create 
App Engine app, change settings.py according to your credentials and 
run the below mentioned command.
```bash
gcloud app deploy
```
```bash
gcloud app browse
```