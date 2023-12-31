import requests
import json


def ocr_space_file(filename, overlay=False, api_key='72cec1fa2f88957', language='eng'):

    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
                "OCREngine": 5,
                "FileType": ".Auto",
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api8.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


# def ocr_space_url(url, overlay=False, api_key='helloworld-apikey', language='eng'):
def ocr_space_url(url, overlay=False, api_key='72cec1fa2f88957', language='eng'):

    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': "donotstealthiskey8589",
               'language': language,
               "OCREngine": 5,
               "FileType": ".Auto",
               }
    r = requests.post('https://api8.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()


# Use examples:
test_file = ocr_space_file(filename='Alphabet.png', language='eng')
test_url = ocr_space_url(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUJKeSXf8UEp2iz-KlJXTkGcqfeTuJILA-Gw&usqp=CAU')

print(test_url)
print(20*"*")
json_object = json.loads(test_file)
text = (json_object["ParsedResults"][0]["ParsedText"])
print(text)
