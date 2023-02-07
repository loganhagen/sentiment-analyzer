# Frontend Docker Container

## Access the frontend site at `localhost:3000`
---
### Accessing the Dev Container
---
1. Make sure the three container stack is built and running on your machine
2. In vscode click on "Open a remote container" in the bottom left corner
3. Click on "Open folder in Container" from the dropdown menu
4. Select the "frontend" folder from the project's root directory
5. The dev environment should open with all dependencies and vscode extensions installed
---

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.
