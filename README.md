# Cloud-Native Monitoring App

<p align="center">

  <img width="720" src="https://github.com/Rajdeep1311/cloud-native-monitoring-app/assets/113296626/b1ba653f-7104-4fa0-adff-eb9ba30221c2" />
 
</p>

A simple cloud-native monitoring app using Python modules with a bit of design using HTML and containerized it using Docker, the app is deployed in the Kubernetes cluster.

## Writing the Script

We need an IDE or Integrated Development Environment like Visual Studio Code or PyCharm for writing the code as they provide us with suggestions and point out the mistakes in the code. We need to import a few Python modules like the **psutil** for getting the system health metrics and the **Flask** module for running the application in Flask. We can also include a warning message to be displayed if the CPU or Memory Utilization goes above 80 percent. Lastly, we need to include the port number for example **0.0.0.0**, the local host to host the application.

We can include an HTML file and some styles so that our site looks a bit decent. You can find the **index.html** file in the templates folder.

## Setting the Stage

The **requirements.txt** file consists of all the required plugins/modules for the project to run smoothly. If we are working in a proper IDE, we can install the plugins manually or we can run the following command:

```sh
pip install -r requirements.txt
```
Next, we need to install docker in your system. For installing Docker in your system you can refer to the [Docker Documentation](https://docs.docker.com/engine/install/)

After installing Docker, we need to write a Dockerfile for creating a Docker image and ultimately Docker container(s). Using the following commands we need to create the docker image and docker container:

Build the Docker image
```sh
docker build -t <app name> <path where you want to build the image>
```
Example:
```sh
docker build -t flask-cpu-memory-app .
```
Run the Docker container
```sh
docker run -p 5000:5000 <app name>
```
Example:
```sh
docker run -p 5000:5000 flask-cpu-memory-app
```
This command maps port 5000 of the container to port 5000 on your host machine, allowing you to access the Flask app at **http://localhost:5000/**

Assuming you have already built an image and we need to push it to our Docker Hub repository, we would follow these steps:

Log in to Docker Hub
 ```sh
docker login
```
Enter your username and password when prompted.

Push the image to Docker Hub
```sh
docker push yourusername/<app name>:latest
```
Example
```sh
docker push rajdeep1311/flask-cpu-memory-app:latest
```

## Conducting the Play
