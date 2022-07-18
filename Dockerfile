FROM python:3
ENV PYTHONBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN mkdir /app/src/__target__
ENTRYPOINT [ "bash", "/app/entrypoint.sh" ]
