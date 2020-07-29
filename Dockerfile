from 106715121600.dkr.ecr.us-east-1.amazonaws.com/nrg-core:buildsystem-qa-branchcheck-ansible-build

ADD . /opt/pyinsights/

RUN python3 /opt/pyinsights/setup.py install