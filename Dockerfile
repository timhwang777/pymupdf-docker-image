FROM python:3.11-slim

LABEL maintainer="dev@ychwang.io"

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install packages
RUN pip install --upgrade pip
RUN pip install PyMuPDF

# Set the working directory
WORKDIR /pymupdf

# Copy the current directory contents into the container at /pymupdf
COPY . /pymupdf

# Run the application
ENTRYPOINT ["python3", "extract.py"]
