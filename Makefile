
dev_dest:
	DOCKER_HOST=tcp://localhost:2375 \
	docker  run \
	--mount type=bind,source="c:/Users/jdupont/.aws/",target=/root/.aws \
	--mount type=bind,source="c:/Users/jdupont/Documents/GitHub/devops/pyinsights",target=/opt/pyinsights/ \
	-it "pyinsights" pyinsights -c /opt/pyinsights/queries/dev_source_addr.yml --profile default -r us-east-1 > dev_dest.json

build:
	docker build . -t pyinsights

test2:
	bash -x ./rundocker.sh


push :
	DOCKER_HOST=tcp://localhost:2375 docker tag pyinsights 106715121600.dkr.ecr.us-east-1.amazonaws.com/nrg-public:pyinsights
	DOCKER_HOST=tcp://localhost:2375 docker push 106715121600.dkr.ecr.us-east-1.amazonaws.com/nrg-public:pyinsights
