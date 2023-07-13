# Sentiment Analyzer

## About
This project is a containerized full-stack web application built by a team of 5 computer science students (Stefan Zupancic, Jonalton Hamilton, Kyle Lukaszek, Tiffiny Haluschak, Logan Hagen) at the University of Guelph as the cumulative project for a senior-level software engineering course. It is meant to teach and demonstrate how containerization can streamline the development process, how CI/CD can maintain codebase robustness, and how Agile principles can encourage a high development velocity. The application performs sentiment analysis and presentation on over 3000 Twitter posts and 200 Reddit posts pertaining to the topic "universal basic income". These posts were gathered over the course of a month using the previously free and available APIs offered by Twitter and Reddit. Continual API calls have been disabled due to recent API policy changes by both Twitter and Reddit (as of July 2023).

## How To Use
1. Clone repository
2. Navigate to the root folder of the repository.
3. Initiate container build and run by using command ```docker compose up``` or ```docker compose up -d``` (ignores logs).
4. Navigate to ```localhost:3000```
5. Enter ```docker compose down --volume``` to tear down the container stack and delete the local volume.

## Note
- The Q&A module uses the OpenAPI AI to generate responses. This requires an OpenAI API key. If you have one that you would like to use, enter the following command ```echo OPENAI_API_KEY=<apikeyhere> > .env``` to create an environment file that Docker Compose will use during the build.


## Known Issues
- Occasionally, the graph for the sentiment analysis for all posts takes longer than expected to load.
