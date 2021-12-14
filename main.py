from rembg.bg import remove
import numpy as np
import io
from PIL import Image
import base64
from flask import Flask,request
import os
app = Flask(__name__)
  
@app.route('/', methods=['POST','GET'])
def hello():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        img_base64 = json['base64']
        img_base64 = img_base64.encode('utf-8')
        img_base64 = base64.b64decode(img_base64)
        img = Image.open(io.BytesIO(img_base64))
        img.save('downloaded.png')
        f = np.fromfile('downloaded.png')
        result = remove(f)
        img_base64 = base64.b64encode(result).decode('utf-8')
        return img_base64 
    else: 
        return "Hello World!"


if __name__ == "__main__":    
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
