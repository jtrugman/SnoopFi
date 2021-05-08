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
*Note* by default the application runs on local port 3000

To kill the server do a 
`control c`


## Docker Usage
We have also incorporated deployment via a docker container in this project. To build and run the application via docker please follow the steps below. 

### Build the Docker Container
`cd /server`
`docker build -t snoopfi .`

### Run Docker Container
`sudo docker run -dp 3000:3000 snoopfi`
*Note* by default the application runs on local port 3000

The `-dp` option allows you to run the docker container 'detached' which means that you are able to map the port the server is running on within the docker container (ie 3000 in SnoopFi's case) with another port on your local machine. This is useful if you are running multiple different servers or multiple versions of the same server on the same machine.

### Kill the Docker Container
`docker ps`
*copy the CONTAINER ID
`docker kill CONTAINER_ID`

## Postman Usage
We have built a [postman](https://www.postman.com/) collection to make it easier to document how our API works and the HTTP requests/responses to communicate with it. 

This Postman collection is stored in postman.json file in the server directory. To open the file in Postman you have to download the Postman Application (or run it via the webapp) and click the import button. It will then prompt you to upload a postman json file. Either navigate to this file or click and drag it into the application. This will import the collection and allow you to use it like a regular Postman collection made in the application. For more details on how to import a Postman Collection see this guide made by Postman https://learning.postman.com/docs/getting-started/importing-and-exporting-data/


### Testing the API via Postman
Testing APIs in Postman is an important step before deployment to insure that it works correctly. For testing the SnoopFi API via Postman the first step is the run the server (this can be done by either Docker or Node). Then navigating to the SnoopFi Postman Collection (see previous section about how to import the collection). After navigation you can click on the request you want to test/send and configure the url and request body parameters. Once done inputing the paramters you want to send click the blue "send" button to send the request. The response from the server should appear below the request body and if you are running either via node in the terminal or exec'd into the docker container you should see a Morgan log for the request you send on the respective server side. 
