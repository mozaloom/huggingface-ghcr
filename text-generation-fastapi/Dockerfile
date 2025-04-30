FROM python:3.11-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT [ "uvicorn" ]

CMD [ "--host", "0.0.0.0", "main:app" ]

