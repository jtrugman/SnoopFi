# SnoopFi Server
## Methodology
The SnoopFi server is a nodejs server which hosts a REST API for processing and distributing the data collected by our Raspberry Pi based application. It uses a few open source packages to help in this endeavor. The first is [morgan](https://www.npmjs.com/package/morgan). Morgan is a middleware used for logging HTTP requests, when running the application via nodejs these logs will appear in the terminal. When running the application via docker you have to use the command:
docker exec -it snoopfi /bin/bash

This command will allow you to access the terminal within the docker container. 

There is also [express](https://www.npmjs.com/package/express) which is a web framework that simplifys the request - response process when dealing with HTTP requests. 

In addition to morgan and express we use [body parser](https://www.npmjs.com/package/body-parser) which is an easy to use middleware for parsing HTTP request bodies. 

For distributing the data collection from the raspberry pi via email we use the package [nodemailer](https://www.npmjs.com/package/nodemailer) which allows us to send emails from the gmail account we created for this project "ee629tm@gmail.com".


## Node Usage
We have included package.json and package-lock.json files in order to make the application easier to port to other devices or users who want to run it. In order to start the application the traditional route with Node.js there are two steps: The first is to download all the dependancies included in the package-lock.json file and the second is to run the server. 

To install all the dependancies use the following command when in the /server directory:
`npm install`

Then run the following command to start the server when in the /server directory:
`npm server.js`

To kill the server do a 
`control c`


## Docker Usage
We have also incorporated deployment via a docker container in this project. To build and run the application via docker please follow the steps below. 

### Build the Docker Container
`cd /server`
`docker build -t snoopfi .`

### Run Docker Container
`sudo docker run -dp 3000:3000 snoopfi`

### Kill the Docker Container
`docker ps`
*copy the CONTAINER ID
`docker kill CONTAINER_ID`
