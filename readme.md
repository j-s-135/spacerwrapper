# SPACER WRAPPER

### Container for the Spacer application.

# INSTRUCTIONS

For Linux or Mac.

Start the docker engine.
- On Mac, find it in the applications directory.
- On Linux, type service docker start.

Cd into the directory containing Dockerfile, then run the following lines.

```
docker build -t spacer -f Dockerfile .

docker run --name spacer -p 8000:8000 spacer
```

Open your browser to localhost:8000.

To change the url that the program runs on, change the configuration.py file in the spacerwrapper subdirectory.

Also change the setting in the Dockerfile.

Then run docker with the port number that you specified.