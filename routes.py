import tornado.ioloop
import tornado.web
import redis
from vote_api import *
import json

r = redis.StrictRedis(host='localhost', db=4)
r.set('vote',json.dumps({'ctr':0,'rnd_no':0,'global_bit_id':0, 'count_no':0, 'pipe_ctr':0}))
r.set('block',json.dumps({'1':{'temp':'temp'}}))
r.set('pipeline',json.dumps({}))
r.set('vote_data',json.dumps({'vote_cnt':[0,0,0], 'vote_pre_cnt':[]}))
#r.set('hash_data',json.dumps('0':[],'1':[],'2':[]))
r.set('hash_data',json.dumps({}))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        kk = json.loads(r.get('vote_data'))
        vote = json.loads(r.get('vote'))['pipe_ctr']
        hash_datas = json.loads(r.get('hash_data')).values()
#        if vote%3 ==0:
#            dat0 = []     
#            self.render("dashboard.html",vote_cnt = kk['vote_cnt'], data0=dat0)
#        else:
#            self.render("dashboard.html",vote_cnt = kk['vote_cnt'])
        print hash_datas
        self.render("dashboard.html",vote_cnt = kk['vote_cnt'], hash_datas=hash_datas)

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