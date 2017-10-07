from routes import *
import pymongo
from pymongo import MongoClient
import requests
import json
import MySQLdb
import hashlib
import tornado.ioloop
import tornado.web
import tornado.websocket
import random
import hashlib as hasher
import datetime as date
import redis

r = redis.StrictRedis(host='localhost', db=4)

class vote(tornado.web.RequestHandler):
    
    def set_headers(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        
    def get(self, room_no):
        global_bit_id= json.loads(r.get('vote'))['global_bit_id']
        self.render("vote.html", room_no = room_no, bit_id = global_bit_id)
            
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
            
            

class signup(tornado.web.RequestHandler):
#        self.write("Signup called")
    def get(self):
        self.render("signup.html")
        

#global rnd_no
#global global_bit_id
class login(tornado.web.RequestHandler):
#        self.write("login called")
    def set_headers(self):
        self.set_header('Content-Type', 'application/json')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        
    def get(self):
        kk = json.loads(r.get('vote'))
        kk['ctr'] += 1
        if(kk['ctr']%3 == 0):
            kk['rnd_no'] = random.randint(1,9)
        r.set('vote',json.dumps(kk))
        self.render("login.html")
        
    def post(self):
        self.set_headers()
        kk = json.loads(r.get('vote'))
        kk['global_bit_id'] = self.get_argument("bit_id")
        r.set('vote',json.dumps(kk))
        #save user details
        self.redirect('/vote/' + str(kk['rnd_no']))
        
    
    
class index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        
        


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
  
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + 
                   str(self.timestamp) + 
                   str(self.data) + 
                   str(self.previous_hash))
        return sha.hexdigest()

    
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

clients = []  
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks_to_add = 20



class WebSocketHandler(tornado.websocket.WebSocketHandler):
    
    def add_block(self, vote_id_hash, vote_hash):
        tmp = random.randint(1,3)
        if tmp == 1:
            #write sql
            db = MySQLdb.connect("localhost","root","root","vote" )
            cursor = db.cursor()
            sql = "INSERT INTO `vote`.`block_vote` (`vote_id`, `vote_hash`) VALUES ('%s', '%s')" % (vote_id_hash,vote_hash)
            cursor.execute(sql)
            db.commit()
            db.close()
        elif tmp == 2:
            #write mongo
            connection = MongoClient("ds149954.mlab.com", 49954)
            db = connection['visualizer']
            db.authenticate('temp', 'temp123')
            #db.mynewcollection.insert({ "temp123" : "new_temp_inserter" })
            db.mynewcollection.insert({ vote_id_hash: vote_hash })
        elif tmp ==3 :
            #write redis
            kk = json.loads(r.get('block'))
#            ss = {vote_id_hash: vote_hash}
            ss = kk['1']
            ss[str(vote_id_hash)] = str(vote_hash)
#            kk[str(vote_id_hash)] =kk[str(vote_hash)]
            kk['1'] = ss
            r.set('block', json.dumps(kk))
        print "successfully written somewhere ?: "
        print "Block hash: " + str(vote_hash)
        
    def open(self, *args):
        print("open", "WebSocketChatHandler")     
        clients.append(self)
        print "Active Clients " + str(len(clients))
    

    def on_message(self, message):        
        print message
        mess = json.loads(message)
        pipe = json.loads(r.get('pipeline'))
        pipe[mess['bit_id']] = message
        r.set('pipeline',json.dumps(pipe))
        
        vote_table = json.loads(r.get('vote'))
        vote_table['pipe_ctr'] +=1
        r.set('pipeline',json.dumps(vote_table))
        
        #vote_id_hash
        sha = hasher.sha256()
        sha.update(str(mess['vote_name']) + str(mess['vote_type']))
        vote_id_hash = sha.hexdigest()
        
        #vote_hash
        sha = hasher.sha256()
        sha.update(str(mess['bit_id']))
        vote_hash = sha.hexdigest()
        mess['bit_id'] = vote_hash
        mess['message'] = "voted for:" + str(mess['vote_name'])
        
        self.add_block(str(mess['vote_name']), vote_hash)
        print "Block Added Successfully:  "
        kk =json.loads(r.get('vote'))
        
        if vote_table['pipe_ctr']%3 == 0:
            for client in clients:
                pipe = json.loads(r.get('pipeline'))
                for val in pipe.values():
  		            client.write_message(val)
        
    def on_close(self):
        clients.remove(self)
        print "Active Clients " + str(len(clients))