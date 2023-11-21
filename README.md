# Cloud-Native Monitoring Application

<p align="center">

  <img width="720" src="https://github.com/Rajdeep1311/cloud-native-monitoring-app/assets/113296626/b1ba653f-7104-4fa0-adff-eb9ba30221c2" />
 
</p>

A simple cloud-native monitoring app using Python modules with a bit of design using HTML and containerized it using Docker, the app is deployed in the Kubernetes cluster.

## Writing the Script

We need an IDE or Integrated Development Environment like Visual Studio Code or PyCharm for writing the code as they provide us with suggestions and point out the mistakes in the code. We need to import a few Python modules like the **psutil** for getting the system health metrics and the **Flask** module for running the application in Flask. We can also include a warning message to be displayed if the CPU or Memory Utilization goes above 80 percent. Lastly, we need to include the port number for example **0.0.0.0**, the local host to host the application.

We can include an HTML file and some styles to make our site look decent. You can find the **index.html** file in the templates folder.

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
You can enter your username and password when prompted.

Push the image to Docker Hub
```sh
docker push yourusername/<app name>:latest
```
Example
```sh
docker push rajdeep1311/flask-cpu-memory-app:latest
```

## Conducting the Play

We now need to install minikube for running Kubernetes. Refer to the [minikube documentation](https://minikube.sigs.k8s.io/docs/start/) for installing minikube according to your needs.

After installation use the following command to start the cluster:
```sh
minikube start
```
In Kubernetes, Pods, Deployments, and Services serve different purposes and are used together to manage and run containerized applications. Here's a brief explanation of each and why you might need separate YAML files for them:

1. **Pods:**
   - A Pod is the smallest deployable unit in Kubernetes, representing a single instance of a running process.
   - It can contain one or more containers that share the same network namespace, storage, and IP address.
   - Use Pods when you need to run a single container or multiple tightly coupled containers together on the same host.
   - You might need separate Pod files for different components of your application that need to run together.

2. **Deployments:**
   - A Deployment is a higher-level abstraction that manages the desired state of Pods using replica sets.
   - It provides features like rolling updates and rollbacks, making it easier to manage updates to your application.
   - Deployments help ensure that a specified number of Pod replicas are always available and healthy.
   - You need separate Deployment files to define different sets of desired replicas, update strategies, and other deployment-related configurations.

3. **Services:**
   - A Service is an abstraction that defines a logical set of Pods and a policy by which to access them.
   - It provides a consistent way to access your application by exposing Pods using a stable IP and DNS name.
   - Services enable load balancing, service discovery, and connectivity within a cluster or from external sources.
   - You need separate Service files to expose different sets of Pods and control how they're accessed from within and outside the cluster.

Typically, you'll use these components together to manage and deploy your applications effectively. Here's a common scenario:

1. **Pod File (app-pod.yaml):**
   - Defines the Pod template, which includes one or more containers.
   - Specifies the application's runtime configuration.

2. **Deployment File (app-deployment.yaml):**
   - Uses the Pod template from the Pod file.
   - Specifies the desired replicas, update strategy, and other deployment settings.
   - Manages the lifecycle of your application by ensuring the desired number of replicas are running.

3. **Service File (app-service.yaml):**
   - Defines a Service that exposes your application Pods to the network.
   - Specifies how the Service should route traffic to the Pods.
   - Provides a stable endpoint for accessing your application.

By using separate files for Pods, Deployments, and Services, you can manage each aspect of your application separately and maintain a clear and modular structure for your Kubernetes configuration.

Here are some samples of pod.yaml, deployment.yaml, and service.yaml files

```sh
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
spec:
  containers:
    - name: nginx-container
      image: nginx:latest
```

```sh
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sample-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: sample-app
  template:
    metadata:
      labels:
        app: sample-app
    spec:
      containers:
        - name: nginx-container
          image: nginx:latest
```

```sh
apiVersion: v1
kind: Service
metadata:
  name: sample-service
spec:
  selector:
    app: sample-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: ClusterIP
```

You can find all the required files to run the project in the GitHub repository and finally, you are ready to deploy your app.

Use these commands to apply the pod, deployment, and service files:
```sh
kubectl apply -f <file name>
```
To list all pods/deployment/service/node:
```sh
kubectl get pods
```
```sh
kubectl get deployments
```
```sh
kubectl get services
```
```sh
kubectl get nodes
```

## Project Screenshots

![Screenshot (298)](https://github.com/Rajdeep1311/cloud-native-monitoring-app/assets/113296626/c275b871-b799-466e-8193-eed9463d3326)

![Screenshot (299)](https://github.com/Rajdeep1311/cloud-native-monitoring-app/assets/113296626/27055976-c2bf-4fc8-9178-e4776e6e7aef)



To learn and apply more commands checkout [Official Kubernetes Documentation](https://kubernetes.io/docs/reference/kubectl/)

If you liked the project, do give it a star. Thank you and happy learning.
