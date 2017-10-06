from routes import *
import pymongo
from pymongo import MongoClient
import requests
import json
import MySQLdb


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
        stock_name = self.get_argument("vote_name")
        
        
        #write to Mlab
        self.mongo_write(req)
        
        #write to sql
        self.sql_write(req['Meta Data'])
        
        self.write(stock_mess)
        #self.render("chart.html")
            
            
            
class signup(tornado.web.RequestHandler):
        self.write("Signup called")
#        self.render("signup.html")
        
class login(tornado.web.RequestHandler):
        self.write("login caled")
#        self.write("login.html")
    
    
class index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")