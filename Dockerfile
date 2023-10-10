# Use an official Python runtime as the parent image
FROM python:3.9

# Set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

ENV ENVIRONMENT="dev"
ENV VERSION="latest"
ENV PROJECT="backend"

WORKDIR /appx

COPY . ./
RUN apt-get update
RUN apt-get install sudo -y

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Specify the command to run on container start
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
