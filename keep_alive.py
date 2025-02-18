from flask import Flask, jsonify, request
from threading import Thread
import os
import sys

app = Flask("")

@app.route("/")
def home():
    return "Le bot est en ligne !"

@app.route("/restart", methods=["POST"])
def restart():
   
    token = request.headers.get("Authorization")
    if token != "YUSEBHSEBHSEBHSEBHSEBHSEBHSEBHVGN14561231": 
        return jsonify({"message": "Non autorisé"}), 403

    
    os.execv(sys.executable, ['python'] + sys.argv)  
    
    return jsonify({"message": "Bot redémarre maintenant."}), 200

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
