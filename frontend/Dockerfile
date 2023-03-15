FROM node:16-slim

# Do not set NODE_ENV in Dockerfile as vite/react-scripts handles it internally
ARG PORT=3000
ENV PORT $PORT

# Install latest npm for all security fixes
RUN npm i npm@latest -g

# It is better to install the dependencies first in a 
# different directory and point the node_modules/.bin to the PATH
WORKDIR /app

# Copy package.json and package-lock.json as they are the least likely to change
COPY package.json package-lock.json ./

# Install dependencies using npm ci. ci is a better practice as it removes the node_modules
# and reinstalls the dependencies from scratch.
RUN npm ci && npm cache clean --force

# point the node_modules/.bin to the PATH so that we can run the scripts like vite, react-scripts
ENV PATH /app/node_modules/.bin:$PATH
ENV PUBLIC_API_URL http://localhost:8080/api/

# Copy the rest of the files in a nested directory
WORKDIR /app/frontend

COPY . .

EXPOSE $PORT

# It is better to run npm build and serve the project using a web server like nginx
# instead of running npm run dev. npm run dev is not meant for production
CMD ["npm", "run", "dev"]
