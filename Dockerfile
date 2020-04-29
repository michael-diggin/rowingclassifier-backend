FROM python:3.6

WORKDIR /api
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN ls
RUN export FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]
