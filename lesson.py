import json
import os

data = {
    'name': 'User',
    'surname': 'Govno',
    'lastname': 'Huinya'
}

with open('text.json', 'w') as file:
    json.dump(data, file)

folder = 'data'

print(os.path.dirname(__file__))

print(os.path.join(os.path.dirname(__file__), folder))

