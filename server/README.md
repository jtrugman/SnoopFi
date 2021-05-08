## Docker Usage
### Build the Docker Container
cd /server
docker build -t snoopfi .

### Run Docker Container
sudo docker run -dp 3000:3000 snoopfi

### Kill the Docker Container
docker ps
*copy the CONTAINER ID
docker kill CONTAINER_ID