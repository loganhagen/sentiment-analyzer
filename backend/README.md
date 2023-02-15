# Backend Docker Container

## Access the backend test site at `localhost:8080/api`
---
### Accessing the Dev Container
---
1. Make sure the three container stack is built and running on your machine
2. In vscode click on "Open a remote container" in the bottom left corner
3. Click on "Open folder in Container" from the dropdown menu
4. Select the "backend" folder from the project's root directory
5. The dev environment should open with all dependencies and vscode extensions installed

---
### Updating The Container
---
When making any changes to the backend files, make sure to update all containers from within the three container stack folder using:
-  `$ docker compose up --force-recreate --build -d`
---
### Adding Python Libraries
---
If you add any python libraries, it is important to `$ pip freeze --all > requirements.txt` so that the docker container is able to install and update all dependencies for the backend whenever rebuilding the container.
---
### Linting
run `$ pylint --rcfile .pylintrc src/` from within the backend folder
---