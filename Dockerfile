FROM python:3.10-alpine

WORKDIR /home/flask_api

COPY flask_api .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["gunicorn", "--chdir", "/home/flask_api", "-w", "1", "-b", "0.0.0.0:8001" ,"app:app"]