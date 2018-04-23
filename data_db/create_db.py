from sqlalchemy import (create_engine, String, Integer, Column)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from data_db import db_info
from contextlib import contextmanager
Base = declarative_base()  # 创建一个基础类
# 创建连接数据库引擎 （适配器采用mysql-connector-python）
engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(db_info.info["username"],
                                                                       db_info.info["password"],
                                                                       db_info.info["ip"],
                                                                       db_info.info["database"]))


@contextmanager
def session_scope():
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class Language(Base):
    """语言类型"""

    __tablename__ = "language"

    id = Column(Integer, primary_key=True)
    text = Column(String(120))

    def __repr__(self):
        return "<Language(text='%s')>" % self.text


if __name__ == '__main__':
    Base.metadata.create_all(engine)

