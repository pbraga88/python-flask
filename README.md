# **flask-rest-api-mysql-v1.2**
This is a simple Flask RESTful API which uses mysql for data storage. Both API and mysql are containerized using podman.

## **Description**
The goal of this project is to demonstrate how to come up with a Flask RESTful API using containers. For that purpose, containers are created for both API and mysql to be orchestrated by a pod. The final objective is to serve the color.json file and to be able to read it (as whole or per element) as well as to add new elements using http CRUD methods. 

## **Dependencies**
podman version 3.2.3 or above\
Ubuntu 20.04

## **Installation (Creating the pod)**
Pull latest mysql image
```
podman pull mysql
```
Build flask-rest-api-mysql-v1.2 from Dockerfile
```
podman build -t flask-rest-api-mysql-v1.2 .
```
Play the pod based on the Kubernetes .yaml file:
```
podman play kube ./flask-mysql-pod.yam
```
## **Executing CRUD methods**
Once the pod is up, one can now send the http CRUD commands.\
The follow examples use 'curl' linux tool, but other tools like postman should get the job done just fine:
1. Retrieve the whole list of colors
    * curl -X GET http://127.0.0.1:5000/colors
2. Retrieve a single color from the list
    * curl -X GET http://127.0.0.1:5000/colors/cyan
3. Insert a new color into the list
    * curl -X POST -H "Content-Type: application/json" -d '{"color":"white","value":"#fff"}' "http://127.0.0.1:5000/colors"

## **Author**
Paulo Simplicio Braga\
paulo.braga1388@gmail.com

## **License**
This project is licensed under the GNU GPLV3 License - see the LICENSE.md file for details