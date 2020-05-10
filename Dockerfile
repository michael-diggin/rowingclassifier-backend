FROM python:3.6

WORKDIR /api
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT [ "uvicorn" ]
CMD ["api.main:app", "--host", "0.0.0.0", "--port", "5000"]
