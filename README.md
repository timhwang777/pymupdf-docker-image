# PyMuPDF Docker Image Builder


## Table of Contents
1. [About the Project](#about-the-project)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
3. [Author](#author)
4. [References](#references)

## About the Project
This project provides a simple Docker Compose file to build a PyMuPDF image. 

Please note that this project is intended for personal use as part of my project. The Dockerfile is not written to industry standards.

## Getting Started
Follow these steps to get a local copy up and running:

1. Build the Docker image
```bash
    docker build --no-cache -t pymupdf .
```
2. For simplicity, we use `docker run` each time to build a new container and create volumes. This may result in many containers when you run `docker ps -a`. Here's how to run the container:
```bash
docker run -v "$(pwd)/data":/pymupdf/data pymupdf \
[INPUT].pdf [OUTPUT].txt
```
### Prerequisites
Ensure you have Docker daemon or Docker Desktop installed on your machine.

## Author
Timothy Hwang

## References
- [Docker Documentation](https://docs.docker.com)
- [PyMuPDF Discussions](https://github.com/pymupdf/PyMuPDF/discussions/1015)
