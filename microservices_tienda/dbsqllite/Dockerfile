FROM python:alpine

COPY . .
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]
CMD ["sqllite.py"]
