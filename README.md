## tnea 2019 & 2020 cut off - Anna university 2019 & 2020 cut off - Python Dash App

Anna University cut off marks.This tool is intended to help 2021 students to get an overview of the cut off marks in the 2020  and 2019 anna university counselling . 

**UPDATE :**  THE APP IS UPDATED WITH 2020 CUT OFF MARKS FOR 2021 STUDENTS.

**Tags :** Anna university  2020 cut off | Tnea 2020 cut off   | For 2021 students


## Running app locally


   ### 1) Install python requirements (Make sure you have Python 3.6 and above)
   
   ```sh
   $ git clone https://github.com/anandhakumarpalanisamy/tnea_2019_cut_off_marks.git
   $ cd tnea_2019_cut_off_marks
   $ pip install -r requirements.txt
   ```
   ### 2a) Start jupyter notebook and run app

   Open **"tnea_app.ipynb"** in jupyter notebook and run

   **App will be running in port 9007 :** http://127.0.0.1:9007/
   
   ### 2b) Run app through command line

   ```sh
   $ cd tnea_2019_cut_off_marks
   $ python3 tnea_app.py
   ```
   **App will be running in port 9007 :** http://127.0.0.1:9007/





## Dockerisation

### 1) Build Docker Image

```sh
$ git clone https://github.com/anandhakumarpalanisamy/tnea_2019_cut_off_marks.git
$ cd tnea_2019_cut_off_marks
$ docker build --tag tnea-app .
```

### 2a) Run as a docker container

```sh
$ docker run -d --name tnea-app -p 9007:9007 tnea-app
```

### 2b) Run as a docker service with replicas

```sh
$ docker service create --name tnea-service --replicas 3 -p 9007:9007 tnea-app:latest
```
