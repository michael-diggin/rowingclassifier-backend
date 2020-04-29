FROM python:3.6

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN export FLASK_APP=app
CMD ["flask", "run", "--host=0.0.0.0"]
