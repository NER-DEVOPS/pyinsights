docker  run \
	--mount type=bind,source="${HOME}/.aws/",target=/root/.aws \
	--mount type=bind,source="${HOME}/pyinsights/queries/",target=/opt/pyinsights/queries/ \
	--mount type=bind,source="${HOME}/pyinsights/data/",target=/opt/pyinsights/data/ \
	--mount type=bind,source="${HOME}/pyinsights/scripts/",target=/opt/pyinsights/scripts/ \
	-it "pyinsights" /opt/pyinsights/scripts/run_ec2_inside.sh
