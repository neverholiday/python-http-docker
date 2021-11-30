### Command to run

1. to build conatiner
	1.1 server
	- cd server
	- docker build . --tag python-http-server && docker image prune -f

	1.2 client
	- cd client
	- docker build . --tag python-http-client && docker image prune -f

2. create network
	- docker network create ${NETWORK_NAME}

3. run container
	3.1 Server
	- docker run --network ${NETWORK_NAME} --rm --name myserver python-http-server
	3.2 client
	- docker run --rm --network nashay-net --name myclient --env SECRET_URL="http://myserver:5000" --env="PYTHONUNBUFFERED=1" python-http-client