#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE ROLE geonode WITH SUPERUSER CREATEROLE CREATEDB REPLICATION LOGIN PASSWORD 'E4UCBqXO';
    CREATE DATABASE labs_geonode_metadata OWNER geonode;
    CREATE DATABASE labs_geonode_data OWNER geonode;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "labs_geonode_data" <<-EOSQL
    CREATE EXTENSION postgis;
    CREATE EXTENSION postgis_topology;
    GRANT ALL ON geometry_columns TO PUBLIC;
    GRANT ALL ON spatial_ref_sys TO PUBLIC;
EOSQL

##Example
#psql -U geonode -d labs_geonode_metadata < /backup/labs_geonode_metadata.sql

#Restoring backup
pg_restore -U geonode -d labs_geonode_metadata  /backup/labs_geonode_metadata.dump
pg_restore -U geonode -d labs_geonode_data  /backup/labs_geonode_data.dump