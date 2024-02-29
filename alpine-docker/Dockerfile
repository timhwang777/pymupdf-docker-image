# This is another version of the Dockerfile that uses the Alpine image.
# Be aware that even though the Alpine image is small, the dependencies are not.
# The whole Python installation could be around 800MB.

FROM alpine:latest

LABEL maintainer="dev@ychwang.io"

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    g++ \
    make \
    musl-dev \
    linux-headers \
    clang16-libclang \
    swig \
    python3-dev

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install your packages
RUN pip install --upgrade pip
RUN pip install PyMuPDF

# Set the working directory
WORKDIR /pymupdf

# Copy the current directory contents into the container at /pymupdf
COPY . /pymupdf

# Run the application
ENTRYPOINT ["python3", "extract.py"]