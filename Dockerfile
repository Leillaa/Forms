FROM python:3.10-slim

WORKDIR /app

COPY ./ /app

RUN pip3 install -r req3.txt --no-cache-dir

CMD ["gunicorn", "survey_form.wsgi:application", "--bind", "0:8000" ]