# fastapi->A web framework used to create python api's 

# advantage over flask is that it comes with type hints(data validation),auto generation of documentation

# uvicorn->a library used to run FastApi projects

# api->its an intermediatory that exists in between a client and server.

# For ex: When user makes a request using an UI an api receives the request and transfers the request to the database/server and when a server responds back again the api transfers the response to the client.

# It acts as medium

# Think like this,

# Client is a software program and server is another software program now client needs services and server is the one the that serves the client

# Through api's client issue his/her request to the server

# postman->API testing platform

# platform where we make our api calls(http calls)

# we can also make it through web browser but we use postman because we can easily pass keys and other features

# What is an endpoint?

# An api provides various services to the clients. 

# Now for ex,a client might want to read the data from the database,or probably he wants to update the database contents or he wants to delete the data in the database.

# For each of the services we will have respective locations in which these actions take place.

# this itself is an api end point. 

# Assume it like this,

# In myntra you want to buy t-shirts,you have an endpoint different from jeans(different endpoint). 

# an endpoint is basically the location of the resource on the server.

# an endpoint is basically component of api.

from fastapi import FastAPI 

# fastapi->module
# FastAPI->class

