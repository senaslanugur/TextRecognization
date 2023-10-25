from flask import Flask, render_template, request
from html import escape
import requests
import json

app = Flask(__name__)

def ocr_space_file(filename, overlay=False, api_key='72cec1fa2f88957', language='eng'):
#helloworld
    payload = {'isOverlayRequired': overlay,
               'apikey': "donotstealthiskey8589",
               'language': language,
                "OCREngine": 5,
                "FileType": ".Auto",
                "detectOrientation": True,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api8.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

    
def ocr_space_url(url, overlay=False, api_key='72cec1fa2f88957', language='eng'):

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               "OCREngine": 5,
               "FileType": ".Auto",

               }
    r = requests.post('https://api8.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        if file:
            filename = file.filename
            text = ocr_space_file(filename=filename)
            # json_object = json.loads(text)
            # text = (json_object["ParsedResults"][0]["ParsedText"])
            success_notification('Image Uploaded and OCR Completed', 'Check the OCR result below.')
            return render_template('result.html', text=text)
            
    elif 'url' in request.form:
        url = request.form['url']
        text = ocr_space_url(url=url)
        success_notification('Image URL Processed', 'View the OCR result below.')
        return render_template('result.html', text=text)
    error_notification('Invalid request', 'Please select a file or provide a valid URL.')
    return render_template('index.html')

def success_notification(title, message):
    """Display a success notification using SweetAlert2."""
    script = '''
    <script>
        Swal.fire({
            title: "{title}",
            html: "{message}",
            icon: "success",
            confirmButtonText: "OK"
        });
    </script>
    '''
    return script

def error_notification(title, message):
    """Display an error notification using SweetAlert2."""
    script = '''
    <script>
        Swal.fire({
            title: "{title}",
            html: "{message}",
            icon: "error",
            confirmButtonText: "OK"
        });
    </script>
    '''
    return script

if __name__ == '__main__':
    app.run(debug=True)