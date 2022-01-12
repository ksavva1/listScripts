#tests
import requests, zipfile, io 

j = 123
requestURL = 'http://api.brain-map.org/grid_data/download/' + j
r = requests.get(requestURL, stream=True)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall(/Users/katiesavva/Downloads)