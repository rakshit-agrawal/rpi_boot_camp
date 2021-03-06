# -*- coding: utf-8 -*-
# BSD license.
# Massimo di Pierro and Luca de Alfaro, 2016.
# Simple web cam app for web2py.


import base64
import json

def index():
    return dict()

PATH = '/ramfs/img.jpg'

def get_image():
    filename = PATH
    with open(filename) as imagefile:
        image = imagefile.read()
        data = {'src':'data:image/jpeg;base64,'+base64.b64encode(image)}
        return json.dumps(data)


