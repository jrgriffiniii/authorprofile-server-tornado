import tornado.ioloop
import tornado.web

import network

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("AuthorProfile Server dashboard")

class DepthHandler(tornado.web.RequestHandler):

    def post(self):

        author = self.get_argument("author", None)
        depth = self.get_argument("depth", None)

        global_message_buffer.new_messages(['Starting the exploration of the network for ' + author + ' to a depth of ' + depth])

        neighborhood = Neighborhood(author, depth)
        global_message_buffer.new_messages([message])
        pass

class StatusHandler(tornado.web.RequestHandler):

    def on_collection_updates(self, messages):

        if self.request.connection.stream.closed():

            return
        self.finish(dict(messages=messages))

    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
        global_message_buffer.wait_for_messages(self.on_collection_updates,
                                                cursor=cursor)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/depth", DepthHandler),
    (r"/status", StatusHandler)
])

if __name__ == "__main__":

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
