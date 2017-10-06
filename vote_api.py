from routes import *
import pymongo
from pymongo import MongoClient
import requests
import json
import MySQLdb
import hashlib


class vote(tornado.web.RequestHandler):
    def set_headers(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        
    def mongo_write(self,req):
        connection = MongoClient("ds149954.mlab.com", 49954)
        db = connection['visualizer']
        db.authenticate('temp', 'temp123')
        #db.mynewcollection.insert({ "temp123" : "new_temp_inserter" })
        db.mynewcollection.insert({ rand_id: json.dumps(req) })
        print "successfully written to MLab:"
        
        #Retreving data from MLab
        data = db.mynewcollection.find()
        for keys in data:
            print keys['_id']
    
    def sql_write(self,req):
        db = MySQLdb.connect("localhost","root","root","vote" )
        cursor = db.cursor()
        sql = "INSERT INTO `vote`.`collect_vote` (`vote_cat`, `voter_name`) VALUES ('%s', '%s')" % ('temp','temp')
        cursor.execute(sql)
        db.commit()
        db.close()
        print "Successfully written to sql: "
        
        
    def post(self):
        self.set_headers()
        vote_type = self.get_argument("vote_type")
        vote_name = self.get_argument("vote_name")
        block_id = self.get_argument("block_id")
        
        to_hash_str = (block_id + vote_type + vote_name)
        hash_object = hashlib.md5(to_hash_str)
        hash_value = hash_object.hexdigest()
        print hash_value
        
        #write to Mlab
        self.mongo_write(hash_value)
        
        #write to sql
        self.sql_write(req['Meta Data'])
        
        self.write(stock_mess)
        #self.render("chart.html")
            
            
            
class signup(tornado.web.RequestHandler):
#        self.write("Signup called")
    def get(self):
        self.render("signup.html")
        
class login(tornado.web.RequestHandler):
#        self.write("login caled")
    def get(self):
        self.render("login.html")
    
    
class index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        
        
        
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print("WebSocket closed")