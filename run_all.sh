docker  run \
	--mount type=bind,source="${HOME}/.aws/",target=/root/.aws \
	--mount type=bind,source="${HOME}/pyinsights/queries/",target=/opt/pyinsights/queries/ \
	-it "pyinsights" pyinsights -c /opt/pyinsights/queries/codebuild.yml --profile default -r us-east-1 > codebuild_data.json
