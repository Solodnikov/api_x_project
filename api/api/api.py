import requests

payload = {'api-key': 'ZWebJwfoKyKr2YL5pq8HdNGAvoEu12oJ',}
r = requests.get('https://api.nytimes.com/svc/books/v3/lists', params=payload)
r.json
print(r.text)

