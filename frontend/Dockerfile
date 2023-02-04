# The backend/Dockerfile contains the documentation for the Dockerfile Instructions
FROM node:16-slim

ARG NODE_ENV=production
ENV NODE_ENV $NODE_ENV

ARG PORT=3000
ENV PORT $PORT

RUN npm i npm@latest -g

WORKDIR /app/frontend

COPY package.json package-lock.json ./

RUN npm install

COPY . .

# add node_modules/.bin/ to PATH environment variable to make sure binaries can be executed
ENV PATH /app/node_modules/.bin:$PATH

EXPOSE $PORT

CMD [ "npm", "run", "dev" ]
