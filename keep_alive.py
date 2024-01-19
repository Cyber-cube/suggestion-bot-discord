from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0', port=os.getenv("PORT", default=5000))

def keep_alive():
    t = Thread(target=run)
    t.start()