from amazonlinux
#RUN yum install -y python3.9
RUN amazon-linux-extras enable python3.8

RUN amazon-linux-extras install -y python3.8
RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install poetry

ADD . /opt/pyinsights
WORKDIR /opt/pyinsights
RUN poetry update
RUN poetry install 
