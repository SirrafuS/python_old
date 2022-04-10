# API - for 2 programs to interconnect for requests Application Programming Interface
# protocol is agreement on what exactly signals transferred between programs mean.
# requests is meant to get HTTP data from websites but not parse it
# pip install requests
import requests
# to just get that page
r = requests.get('https://xkcd.com/353/')
# to check all the possible attributes and methods for the object use dir
# print(dir(r))
# for more details run with help
# print(help(r))

# to get html source of the website
print(r.text)

# to download the image from webpage first you need to get bytes for that image

image = requests.get('https://imgs.xkcd.com/comics/python.png')
print(image.content)

# open new file in write bytes mode as f:
with open('comic.png', 'wb') as f:  # f is variable name for file with that attributes to work with later
    f.write(image.content)      # to write to the file in same dir as python module

# 200s are success, 300s are redirects, 400s are client error (no permission to view), 500s are server errors
print(r.status_code)
# will return true for anything that is less than 400 response
print(r.ok)

# to get headers for website
print(r.headers)

# testing with httpbin.org - website created for http checks for requests tool
# usually you can pass url parameters directly in url, like ?page=2&count=20
# you can still do it that way but there can be mistakes, so Requests lib generates appropriate url for us using
# dictionaries like this
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)
# if we check url for r we will see full link with parameters passed using params=
print(r.url)

# instead of getting we can post data too
payload = {'username': 'tiko', 'password': 'test'}
r = requests.post('https://httpbin.org/post', data = payload)
print(r.text)
# create variable with dictionary of values of json
r_dict = r.json()
print(r_dict)
# print only form
print(r_dict['form'])

# you can pass credentials to url for authorization using basic http Auth using tuple auth= with credentials
# overall it's a good idea to put timeout parameter in the end of requests to avoid endless requests
r = requests.get('https://httpbin.org//basic-auth/tigran/test', auth=('tigran', 'test'), timeout=5)
print(r.text)
print(r.ok)
print(r.status_code)

# setting wrong credentials will not give the same output and return 401 as response
r = requests.get('https://httpbin.org//basic-auth/tigran/test', auth=('tigra', 'test'))
print(r.ok)
print(r.status_code)