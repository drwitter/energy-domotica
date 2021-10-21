FROM python:3

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ src/
ADD config/ config/

RUN ls

WORKDIR /app
CMD [ "python", "-u", "./src/run-service.py" ]