create schema beers_db;
REVOKE ALL ON DATABASE beers_db FROM public;  -- shut out the general public
GRANT CONNECT ON DATABASE beers_db TO dbuser;  -- since we revoked from public

GRANT USAGE ON SCHEMA public TO dbuser;

GRANT ALL ON ALL TABLES IN SCHEMA public TO dbuser;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO dbuser; -- don't forget those

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA beers_db TO dbuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA beers_db TO dbuser;