# SPACER WRAPPER

### Container for the Spacer application.

# INSTRUCTIONS

For Linux or Mac.

# VIRTUAL ENVIRONMENT

### Install

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
deactivate
```


### Run

```
source venv/bin/activate
python3 manage.py runserver
```

Open your browser to 127.0.0.1:8000.

### Log out

```
deactivate
```

# DOCKER

Start the docker engine.
- On Mac, find it in the applications directory.
- On Linux, type service docker start.

Obtain root privileges.
Cd into the directory containing Dockerfile, then run the following lines.

```
docker build -t spacer -f Dockerfile .

docker run --name spacer -p 8000:8000 spacer

(if container exists)

docker rm container-id

(then repeat run command)
```

Open your browser to 127.0.0.1:8000.

To change the url that the program runs on, change the configuration.py file in the spacerwrapper subdirectory.

Also change the setting in the Dockerfile.

Then run docker with the port number that you specified.
