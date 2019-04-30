'''
    The RESTful style api server
'''

from server import app
from server import dataService

from flask import render_template
from flask import Flask, request, redirect, jsonify, send_from_directory
from pymongo import MongoClient
from functools import wraps
import hashlib
import random
import time
import datetime
import os
import json
import requests
import subprocess

_currentDir = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return json.dumps('/')
    # return render_template('index.html')

@app.route('/test')
def _test():
    return json.dumps('test')


@app.route('/initialization/<videoId>')
def _initialization(videoId):
    result = dataService.initialization(videoId)
    return json.dumps(result)


@app.route('/videoData/<videoId>')
def _videoData(videoId):
    result = dataService.getVideoData(videoId)
    return json.dumps(result)


if __name__ == '__main__':
    pass



'''
Fast test:
/api/auth/login
curl -l -H "Content-type: application/json" -X POST -d '{"userName":"test@viv.co.jp","password":"test1243"}' localhost:5003/api/auth/login
curl -l -H "Content-type: application/json" -X POST -d '{"userName":"amami@viv.co.jp","password":"amami1243"}' localhost:5003/api/auth/login



/api/auth/register
curl -l -H "Content-type: application/json" -X POST -d '{"userName":"test@viv.co.jp","password":"test1243","kindergarten":"test"}' localhost:5003/api/auth/register

/api/info/user/<userId>/profile
curl -l -H "Content-type: application/json" -X POST -d '{"userName":"test@viv.co.jp","password":"test","kindergarten":"test123"}' localhost:5003/api/info/user/test@viv.co.jp/profile?token=tc5486dfc976bd97810f99dfe02a251ae292f47b4a9d91f744083ebd9

/api/remove/user/<userId>
curl -l localhost:5003/api/remove/user/test@viv.co.jp?token=tc5486dfc976bd97810f99dfe02a251ae292f47b4a9d91f744083ebd9

/api/info/user/<userId>/video/<videoId>
curl -l localhost:5003/api/info/user/amami@viv.co.jp/video/IMG_7378?token=tca4a7735d17145fdd3a0798461130a1512927ac75717d495c5c869a2

/api/fileinfo/user/<userId>/video/<videoId>
curl -l -H "Content-type: application/json" -X POST -d '{"title":"test title"}' localhost:5003/api/fileinfo/user/amami@viv.co.jp/video/IMG_7378?token=tc5486dfc976bd97810f99dfe02a251ae292f47b4a9d91f744083ebd9

/api/file/user/<userId>/video/
curl -F "file=@/Users/lizhen/Downloads/1.mp4;type=application/octet-stream" "localhost:5003/api/file/user/amami@viv.co.jp/video/?token=t76e6e12b36c700190ae9e055b01c0c729baff0ace678100ddc4e4ecd"

'''

