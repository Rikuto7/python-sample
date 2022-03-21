from click import echo
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm


engine = sqlalchemy.create_engine(
    'mysql+pymysql:///dbname',
    echo=True
)

Base = sqlalchemy.ext.declarative.declarative_base()
# DB定義
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
# sql実行
