# Backend Docker Container

## Access the backend test site at `localhost:8080/api`
---
### Updating
---
When making any changes to the backend files, make sure to update all containers from within the three container stack folder using:
-  `$ docker compose build --no-cache`

### Adding Python Libraries
---
If a python library needs to be added to the backend, make sure to add the libraries to the python virtual environment that exists within the backend folder "venv".

To access the virtual environment, simply CD into the backend directory and then execute the command:

- `$ . venv/Scripts/activate`

Once you are in the virtual environment, you are free to use `pip` to install any python libraries we might need.

If you add any python libraries, it is important to `$ pip freeze > requirements.txt` so that the docker container is able to install and update all dependencies for the backend once `$ docker compose build --no-cache` is executed.