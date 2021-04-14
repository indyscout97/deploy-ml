import requests
import json
#r = requests.get('http://127.0.0.1:5000/help')
#print(r.text)

# Loading data
with open('newdata.json', 'r') as f:
  testdata = json.load(f)

# Using request package to send POST to flask server
r = requests.post('http://127.0.0.1:5000/predict', json={'newdata' : testdata})
data = r.json()
prediction = data['prediction']

# This prints the predictions with pretty formatting
counter = 0
for i in prediction:
    counter += 1
    print('Good day to you. The probability of phishing for URL', counter,'is:', i)
