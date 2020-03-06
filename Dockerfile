FROM python:3.8

RUN pip install bottle
RUN mkdir /code
ADD app /code/app

CMD ["python", "/code/app/server.py"]