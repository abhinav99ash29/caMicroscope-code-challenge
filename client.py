import requests
import json
import numpy as np
import pickle
import cv2

url = 'http://localhost:30000'

x = requests.post(url, data = 'b')
data = json.loads(x.text)
b = np.array(data['data']).reshape(data['w'],data['h'],1)
b = b.astype(np.uint8)
print('Received blue channel')

x = requests.post(url, data = 'g')
data = json.loads(x.text)
g = np.array(data['data']).reshape(data['w'],data['h'],1)
g = g.astype(np.uint8)
print('Received green channel')

x = requests.post(url, data = 'r')
data = json.loads(x.text)
r = np.array(data['data']).reshape(data['w'],data['h'],1)
r = r.astype(np.uint8)
print('Received red channel')

img = cv2.merge((b,g,r))
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
