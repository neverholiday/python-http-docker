### Command to run

1. to build conatiner
	
	1.1 server
	- cd server
	- docker build . --tag python-http-server && docker image prune -f

	1.2 client
	- cd client
	- docker build . --tag python-http-client && docker image prune -f

2. create network
	- export NETWORK_NAME=python-network
	- docker network create ${NETWORK_NAME}

3. run container
	
	3.1 Server
	- docker run -d --network ${NETWORK_NAME} --name myserver --network-alias myserver.local python-http-server
	
	3.2 client
	- docker run -d --network ${NETWORK_NAME} --name myclient --env SECRET_URL="http://myserver:5000" --env="PYTHONUNBUFFERED=1" python-http-client
	you also change SECRET_URL to http://myserver.local:5000


4. to inspect your network using container from nicolaka/netshoot (ref: https://github.com/nicolaka/netshoot )
	- docker run -it --network python-network nicolaka/netshoot

