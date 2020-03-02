from alpine:latest

RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

#makedir
WORKDIR /app
COPY . /app

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["views.py"]