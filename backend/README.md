# Backend Docker Container

## Access the backend test site at `localhost:8080/api`
---
### Updating The Container
---
When making any changes to the backend files, make sure to update all containers from within the three container stack folder using:
-  `$ docker compose up --force-recreate --build -d`

### Adding Python Libraries
---
If you add any python libraries, it is important to `$ pip freeze --all > requirements.txt` so that the docker container is able to install and update all dependencies for the backend whenever rebuilding the container.