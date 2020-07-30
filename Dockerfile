FROM python:3.8-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 9007
CMD python ./tnea_app.py
