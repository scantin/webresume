import tornado.ioloop
import tornado.web
import os



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")   

settings = {
"static_path": os.path.join(os.path.dirname(__file__), "static") 
}

application = tornado.web.Application([
    (r"/", MainHandler),],**settings
)

if __name__ == "__main__":
    application.listen(9000)
    tornado.ioloop.IOLoop.current().start()
