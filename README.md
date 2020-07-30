## tnea 2019 cut off - Anna university 2019 cut off - Python Dash App

## Running app locally

   ## 1) Install python requirements (Make sure you have Python 3.6 and above)
   
   ```sh
   $ git clone https://github.com/anandhakumarpalanisamy/tnea_2019_cut_off_marks.git
   $ cd tnea_2019_cut_off_marks
   $ pip install -r requirements.txt
   ```
   ## Start jupyter notebook

   Open **"tnea_app.ipynb"** in jupyter notebook and run

   **App will be running in port 9007 :** http://127.0.0.1:9007/


## Dockerisation

### Build Docker Image

```sh
$ git clone https://github.com/anandhakumarpalanisamy/tnea_2019_cut_off_marks.git
$ cd tnea_2019_cut_off_marks
$ docker build --tag tnea-app .
```

### Run as a docker container

```sh
$ docker run -d --name tnea-app -p 9007:9007 tnea-app
```

## Run as a docker service with replicas

```sh
$ docker service create --name tnea-service --replicas 3 -p 9007:9007 tnea-app:latest
```
