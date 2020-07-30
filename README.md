## tnea 2019 cut off - Anna university 2019 cut off - Python Dash App


## Install python requirements

Make sure you have Python 3.7

```sh
$ git clone https://github.com/anandhakumarpalanisamy/tnea_2019_cut_off_marks.git
$ cd tnea_2019_cut_off_marks
$ pip install -r requirements.txt
```
## Running app 

- Open **"tnea_app.ipynb"** in jupyter notebook and run

- **App will be running in port 9007 :** http://127.0.0.1:9007/

## Run as a docker container

```sh
$ git clone https://github.com/anandhakumarpalanisamy/tnea_2019_cut_off_marks.git
$ cd tnea_2019_cut_off_marks
$ docker build --tag tnea-app .
$ docker run --name tnea-app -p 9007:9007 tnea-app
```
