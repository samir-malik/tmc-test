FROM python:3.13.7-alpine3.21

WORKDIR /tmc

COPY ./requirements.txt /tmc/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmc/requirements.txt

COPY . /tmc/

CMD ["fastapi", "run", "src/app/main.py",  "--proxy-headers", "--port", "80"]