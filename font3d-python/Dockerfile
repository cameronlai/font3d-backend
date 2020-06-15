# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM ubuntu:bionic

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:openscad/releases
RUN apt-get update
RUN apt-get install -y openscad
RUN apt-get install -y python3-pip
RUN pip3 install Flask gunicorn

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
