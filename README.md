
# Django, Docker Container

This is a simple project using Python, Django, Bootstrap, MySQL as project implementation. Whereas, Docker is use for deployment. The project is simple application with few features that include Authentication followed by few having CURD operations and you can export the data to excel format as well.
## Requirements
Basic requirement for running this project is.
- direnv
- docker

## Set Variables

Rename the file name from .envrc.template to .envrc and provide the values to these variables. 
- MYSQL_HOSTPORT=
- MYSQL_INTERNALPORT=
- MYSQL_USER=
- MYSQL_PASSWORD=
- MYSQL_DATABASE=

Now execute
```bash
  direnv allow
```

## Running Project

To runs this project just execute this docker command.

```bash
  docker-compose up -d
```