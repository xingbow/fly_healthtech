#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from server import app
# from gevent.pywsgi import WSGIServer
# # app.config['STATIC_FOLDER'] = './client/assets'

# http_server = WSGIServer(('', 5003), app)
# http_server.serve_forever()

from server import app
# The port number should be the same as the front end
try:
    app.run(host='127.0.0.1', port='5003', use_reloader=False, debug=True)
except:
    print('Something wrong!')

