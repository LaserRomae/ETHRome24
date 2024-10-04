FROM python:3.12-bookworm

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
COPY main.py /main.py

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0"]