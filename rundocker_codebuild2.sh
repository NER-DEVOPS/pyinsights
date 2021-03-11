
docker  run \
	--mount type=bind,source="c:/Users/jdupont/.aws/",target=/root/.aws \
	--mount type=bind,source="c:/Users/jdupont/Documents/GitHub/devops/pyinsights/queries/",target=/opt/pyinsights/queries/ \
	-it "pyinsights" pyinsights -c /opt/pyinsights/queries/codebuild-role-mynrgapp-qa-deploy_role2.yml --profile default -r us-east-1 > codebuild_data.json
