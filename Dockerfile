FROM python:3.9-slim

WORKDIR /root

ENV PYTHONUNBUFFERED=1

COPY ./manage.py /root/manage.py
COPY ./requirements.txt /root/requirements.txt
COPY ./spacerwrapper /root/spacerwrapper
COPY ./static /root/static
COPY ./tree /root/tree
COPY ./welcome /root/welcome

RUN pip3 install --upgrade pip && pip3 install -r /root/requirements.txt && python3 /root/manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "spacerwrapper.wsgi"]
#CMD ["python3", "/root/manage.py", "runserver", "0.0.0.0:8000"]

