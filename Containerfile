FROM python:3.9-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN flask_wpp_api create-db
RUN flask_wpp_api populate-db
RUN flask_wpp_api add-user -u admin -p admin
EXPOSE 5000
CMD ["flask_wpp_api", "run"]
