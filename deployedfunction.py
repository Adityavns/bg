from urllib import request
from rembg.bg import remove
import numpy as np
import io
from PIL import Image
import requests
import urllib.request
import base64
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'base64' in request.args:
        Image.LOAD_TRUNCATED_IMAGES = True
        #decode base64 to image
        img_base64 = request.args.get('base64')
        img_base64 = img_base64.encode('utf-8')
        img_base64 = base64.b64decode(img_base64)
        img = Image.open(io.BytesIO(img_base64))
        #save image to file
        img.save('downloaded.png')
        f = np.fromfile('downloaded.png')
        result = remove(f)
        img_base64 = base64.b64encode(result).decode('utf-8')
        return img_base64 
    
    else:
        return f'Hello World!'



if __name == '__main__':
    app.run(debug=True, host='0.0.0.0:5050')


