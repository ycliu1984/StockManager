# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib.parse
import datetime
###############################################################################
#                       股票機器人 Python基礎教學 【pymongo教學】                      #
###############################################################################

# Authentication Database認證資料庫
Authdb='stockmanager'

##### 資料庫連接 #####
def constructor():
    client = MongoClient('mongodb://alan:730309al@ac-duzjfef-shard-00-00.mmtqtsm.mongodb.net:27017,ac-duzjfef-shard-00-01.mmtqtsm.mongodb.net:27017,ac-duzjfef-shard-00-02.mmtqtsm.mongodb.net:27017/?ssl=true&replicaSet=atlas-11svnq-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client[Authdb]
    return db
   
#----------------------------儲存使用者的股票--------------------------
def write_user_stock_fountion(stock, bs, price):  
    db=constructor()
    collect = db['stockdb']
    collect.insert({"stock": stock,
                    "data": 'care_stock',
                    "bs": bs,
                    "price": float(price),
                    "date_info": datetime.datetime.utcnow()
                    })
    
#----------------------------殺掉使用者的股票--------------------------
def delete_user_stock_fountion(stock):  
    db=constructor()
    collect = db['stockdb']
    collect.remove({"stock": stock})
    
#----------------------------秀出使用者的股票--------------------------
def show_user_stock_fountion():  
    db=constructor()
    collect = db['stockdb']
    cel=list(collect.find({"data": 'care_stock'}))

    return cel



