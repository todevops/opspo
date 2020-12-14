#!/usr/bin/env python3
import os
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from libs.google_authenticator import verify_mfa, get_qrcode
from settings import BASE_DIR, secret_key


define("port", help="run on the given port", default="8000", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class MFAHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("username")
        filename = get_qrcode(secret_key, username)
        if filename:
            self.write("GEN SUCCESS")
        else:
            self.write("GEN FAILED")

    def post(self):
        code = self.get_argument("code")
        result = verify_mfa(secret_key, code)
        if result:
            self.write("VERIFY SUCCESS")
        else:
            self.write("VERIFY FAILED")


def make_app():
    return tornado.web.Application(
        handlers=[
            (r"/", IndexHandler),
            (r"/mfa", MFAHandler)
        ],
        template_path=os.path.join(BASE_DIR, "templates"),
        static_path=os.path.join(BASE_DIR, "static"),
    )


if __name__ == "__main__":
    options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
