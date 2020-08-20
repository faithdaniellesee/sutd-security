#!/usr/bin/env python2

from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def email_server():
    arg1 = request.args.get('to', None)
    arg2 = request.args.get('payload', None)

    if arg1 is None or arg2 is None:
        return 'Error: Missing parameters'
    else:
        return 'to=' + arg1 + ', payload=' + arg2

app.run(host='127.0.0.1', port=8000, debug=True)
