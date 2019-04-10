#!/usr/bin/python
# -*- coding: UTF-8 -*-

import docker

client = docker.from_env()

# Pull an image
# 等价于"docker pull"
image = client.images.pull("alpine:latest")
print image.tags

# Run a container
# 等价于"docker run alpine echo hello world"
# By default, it will wait for the container to finish and return its logs
container = client.containers.run("alpine", ["echo", "hello", "world"])
print container

# Run a container in the background
# 等价于"docker run -d bfirsh/reticulate-splines"
container = client.containers.run("bfirsh/reticulate-splines", detach=True)
print container.id
# Print the logs of a specific container
container = client.containers.get(container.id)
print container.logs()

# List and manage containers(only list containers that are running)
# 等价于 "docker ps"
for container in client.containers.list():
    print container.id

# Stop & Remove all containers
# 等价于"docker ps -a"
for container in client.containers.list(all=True):
    container.stop()
    container.remove(force=True)

# List all images
for image in client.images.list():
    print image.attrs

# Commit a container to create an image from its contents
container = client.containers.run("alpine", ["touch", "/helloworld"], detach=True)
container.wait()
image = container.commit("helloworld")
print image.id
