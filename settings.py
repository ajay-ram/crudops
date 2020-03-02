import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# local testing
db_name = "testdb"
db_host = "0.0.0.0"
db_port = "4999"
db_user = "postgres"
user_password = "test@123"

SQLALCHEMY_TRACK_MODIFICATIONS=True
SQLALCHEMY_DATABASE_URI='postgresql://' + db_user + ':' + user_password + '@' + db_host + '/' + db_name
