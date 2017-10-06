import tornado.ioloop
import tornado.web

from vote_api import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Blockchain Voting, ")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/signup", signup),
        (r"/login", login),
        (r"/vote", vote),
        (r"/index", index),
    ])

if __name__ == "__main__":
    app = make_app()
    print ('Listening on port: 8888')
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    
#API key = PTJUBNEO2HLMPSQD