from python

RUN python3 -m pip install poetry
RUN python3 -m pip install pyinsights
ADD pyproject.toml /opt/pyinsights/pyproject.toml
ADD poetry.lock /opt/pyinsights/poetry.lock
ADD README.md /opt/pyinsights/README.md
ADD pyinsights /opt/pyinsights/pyinsights
WORKDIR /opt/pyinsights/
RUN poetry install 
#RUN poetry update

ADD queries /opt/pyinsights/queries
RUN which pyinsights
#RUN pyinsights -c ./queries/codebuild.yml --profile default -r us-east-1
#RUN python3 -m pyinsights.cli -c ./queries/codebuild.yml --profile default -r us-east-1 > lambda_permissions.json
