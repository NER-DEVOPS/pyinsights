# running 

`poetry run pyinsights`

`poetry run pyinsights -c ./queries/dev_source_addr.yml `

poetry run pyinsights -c ./queries/dev_source_addr.yml  > source_addr.json
poetry run pyinsights -c ./queries/dev_dest_addr.yml > dest_addr.json

poetry run pyinsights --profile prod --region us-east-1 -c ./queries/prod_source_addr.yml  > prod_source_addr.json
poetry run pyinsights --profile prod --region us-east-1 -c ./queries/prod_dest_addr.yml  > prod_dest_addr.json

# transit between source and dest
poetry run pyinsights  --region us-east-1 -c ./queries/dev_transit_addr.yml > dev_transit.json 
poetry run pyinsights --profile prod --region us-east-1 -c ./queries/prod_transit_addr.yml > prod_transit.json 

## merge multiple items together 
jq -s [.[]]  ~/GitHub/devops/pyinsights/prod_transit.json > data/prod_transit.json

poetry run pyinsights --profile prod --region us-east-1 -c ./queries/cloudwatch_details.yml > cloudwatch_details_prod.json
poetry run pyinsights  -c ./queries/cloudwatch_details.yml > cloudwatch_details_dev.json

poetry  run pyinsights  --region us-east-1 --profile prod -c ./queries/cloudwatch_details.yml

jq -r '.[]|.srcAddr' source_addr.json  | sort -u | grep -v null > source_addr.txt
jq -r '.[]|.dstAddr' dest_addr.json  | sort -u | grep -v null  > dest_addr.txt

# example of running in cloud shell


    bash -x ./run_cloudshell.sh  ./queries/events_resources.yml --data-from data/dev_events_new.json


# fork of pyinsights
to build the docker image 
`docker build . -t pyinsights`

to run it in wsl 

```
docker  run \
	--mount type=bind,source="c:/Users/$USER/.aws/",target=/root/.aws \
	--mount type=bind,source="c:/Users/$USER/Documents/GitHub/pyinsights/queries/",target=/opt/pyinsights/queries/ \
	-it "pyinsights" pyinsights -c /opt/pyinsights/queries/codebuild.yml --profile default -r us-east-1 > codebuild_data.json
```


# PyInsights

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyinsights)
![PyPI](https://img.shields.io/pypi/v/pyinsights?color=blue)
![GitHub](https://img.shields.io/github/license/homoluctus/pyinsights)

A CLI tool To query CloudWatch Logs Insights.

![usage1](https://raw.githubusercontent.com/homoluctus/pyinsights/master/images/usage1.png)

![usage2](https://raw.githubusercontent.com/homoluctus/pyinsights/master/images/usage2.png)

## ToC

- [Usage](#Usage)
  - [Write Configuration](#Write%20Configuration)
  - [Execute command](#Execute%20command)
- [Configuration](#Configuration)
- [CLI Options](#CLI%20Options)
- [Environment Variable](#Environment%20Variable)

## Usage

### Write Configuration

Write configuration to `pyinsights.yml` like:

```yaml
version: '1.0'
log_group_name:
  - '/ecs/sample'
query_string: 'field @message | filter @message like /ERROR/'
duration: '30m'
limit: 10
```

I wrote examples, so see [examples folder](https://github.com/homoluctus/pyinsights/tree/master/examples).

### Execute command

```bash
pyinsights -c pyinsights.yml -p aws_profile -r region
```

## Configuration

|Parameter|Type|Required|Description|
|:--:|:--:|:--:|:--|
|version|string|true|Choose configuration version from ['1.0']|
|log_group_name|array|true|Target log group names to query|
|query_string|string|true|Pattern to query|
|duration|string or object|true||
||string||Specify hours, minutes or seconds from now<br>Unit:<br>hours = `h`,<br>minutes = `m`,<br>seconds = `s`,<br>days = `d`,<br>weeks = `w`|
||object||Specify `start_time` and `end_time`<br>Datetime format must be `YYYY-MM-DD HH:MM:SS`|
|limit|integer|false|The number of log to fetch|

## CLI Options

|Option|Required|Description|
|:--:|:--:|:--|
|-c, --config|true|Specify yaml configuration by absolute or relative path|
|-f, --format|false|Choose from json or table|
|-p, --profile|false|AWS profile name|
|-r, --region|false|AWS region|
|-v, --version|false|Show version|

## Environment Variable

If `profile` and `region` options are not specified, AWS Credentials must be set as environment variables.

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

Please see [Environment Variable Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#environment-variable-configuration) for the detail.
