FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /src

# Django entrypoint
COPY ./docker/web/start.sh /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

# Packages dependencies
RUN pip install pipenv
#    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev\
#    && apk add postgresql-dev \
#    && apk add postgresql-client \

# Packages
COPY Pipfile ./
RUN pipenv lock && pipenv install --system --dev
