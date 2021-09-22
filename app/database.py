from flask import Flask
from flask_appbuilder import SQLA, AppBuilder

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.functions import database_exists, create_database

from config import server_config

engine = create_engine(server_config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db(flask_app: Flask):
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    if not database_exists(server_config.SQLALCHEMY_DATABASE_URI):
        create_database(server_config.SQLALCHEMY_DATABASE_URI)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = server_config.SQLALCHEMY_DATABASE_URI
    flask_app.config['CSRF_ENABLED'] = True
    flask_app.config['SECRET_KEY'] = 'timelineserver'
    db = SQLA(flask_app)
    appbuilder = AppBuilder(flask_app, db.session)
    db.create_all()
    return appbuilder
