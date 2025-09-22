from datetime import timedelta

class Config:
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/unihub_db'
     JWT_SECRET_KEY = "unihub" 
     JWT_EXPIRATION_DELTA = timedelta(hours=24)
