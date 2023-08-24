## Overview
This project is about deploying a language detection model on a server as an API service in a Python web application. 

The data for the model is developed in jupyter notebook, then a model pipeline object is created and saved which takes in a string and returns a string output of what langauge the input string is in. The model is delivered FastAPI, a web framework for deploying APIs that facilitates get and post requests. A JSON object is returned (eg:{'lagnauge':'English}) containing the prediction value, and Pydantic is used to validate the data types passed to be only strings. 

The application is packaged in a docker container starting with a Uvicorn and Gunicorn (web server and gateway) image container. The instructions to install the dependencies with pip are in the docker file. This docker file can then be deployed on a Heroku server either as a pre-built docker image or via building the image on Heroku. I chose the latter and use a heroku.yml to deploy it on Heroku. 
The instructions for deploying a Docker image with a yaml file:
https://devcenter.heroku.com/articles/build-docker-images-heroku-yml


## Stack
Model:
- Scikit-learn

Web application:
- FastAPI
- Pydantic

Container and dependency management:
- Docker 
- Uvicorn and Gunicorn Docker image

Server:
- Heroku
