import tornado.ioloop
import tornado.web
import redis
from vote_api import *
import json

r = redis.StrictRedis(host='localhost', db=4)
r.set('vote',json.dumps({'ctr':0,'rnd_no':0,'global_bit_id':0, 'count_no':0, 'pipe_ctr':0}))
r.set('block',json.dumps({'1':{'temp':'temp'}}))
r.set('pipeline',json.dumps({}))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Blockchain Voting, ")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/signup", signup),
        (r"/login", login),
        (r"/index", index),
        (r"/vote/([^/])", vote),
        (r"/WebSocketHandler/([^/])", WebSocketHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    print ('Listening on port: 8888')
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
#API key = PTJUBNEO2HLMPSQD