FROM python:3.6
RUN mkdir /server
WORKDIR /server
ADD ./server /server/
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt \