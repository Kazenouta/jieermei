from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os, pymysql

APPID = 'wx1d2bd871387bde10'

#------------ 数据库配置 ----------
# MySQL
ENGINE = create_engine(
    'mysql+pymysql://bxz:Bxz13781131889@106.54.20.193:3306/jieermei?charset=utf8mb4', encoding = 'utf8') 
