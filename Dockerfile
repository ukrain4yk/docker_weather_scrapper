FROM python:3
MAINTAINER Ukrain4yk

ENV PYTHONUNBUFFERED 1
ENV PYTHONUTF8 1

# Update system and install dependencie


# Application coping and running
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./app/ /app

# Run the command on container startup
CMD ["python", "main.py"]