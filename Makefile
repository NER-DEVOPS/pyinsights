build:
	docker build . -t pyinsights

test2:
	bash -x ./rundocker.sh
