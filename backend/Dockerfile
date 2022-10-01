FROM python3.8-slim-buster

LABEL maintainer="Bubble Bois"

# Copy project dependencies
COPY Pipfile* /app/

# Install project dependencies
RUN pipenv install --system
RUN sudo apt install ffmpeg

# Copy project files
COPY . /app/

ENV SECRET_KEY 'temporary key just to build the docker image'

# Collect static files
RUN python3 /app/manage.py collectstatic --noinput
