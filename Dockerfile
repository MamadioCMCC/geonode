FROM python:2.7.9

MAINTAINER francois.vanderbiest@camptocamp.com

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# This section is borrowed from the official Django image but adds GDAL and others
RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		postgresql-client libpq-dev \
		sqlite3 \
                python-gdal python-psycopg2 \
                python-imaging python-lxml \
                python-dev libgdal-dev \
                python-ldap \
                libmemcached-dev libsasl2-dev zlib1g-dev \
                python-pylibmc \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*


COPY package/docker/wait-for-postgres.sh /usr/bin/wait-for-postgres
RUN chmod +x /usr/bin/wait-for-postgres

# python-gdal does not seem to work, let's install manually the version that is
# compatible with the provided libgdal-dev
RUN pip install GDAL==1.10 --global-option=build_ext --global-option="-I/usr/include/gdal"


COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --no-deps -e /usr/src/app/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
