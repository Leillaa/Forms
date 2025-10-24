FROM python:3.11-slim


WORKDIR /app

COPY ./ /app

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput

CMD ["gunicorn", "survey_form.wsgi:application", "--bind", "0.0.0.0:8000"]