#import requests as rq


imag = """
https://images.squarespace-cdn.com/content/v1/5006ff0084ae2a41e73bc5b6/1362589459111-\
4G1KNIT2VDGYU33CRDBA/ke17ZwdGBToddI8pDm48kPx25wW2-RVvoRgxIT6HShBZw-\
zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-\
7XRK3dMEBRBhUpwGbtSA7WutlFA3XjmDXUDFwmxX_uEhqHOBUlPnU0mYmf1Qvd6diXKmxQIX-\
f1CXeo/underwater_dark07.jpg"""
#respond = rq.get("https://restcountries.eu/data/syc.svg")
#respond = rq.get("https://images.squarespace-cdn.com/content/v1/5006ff0084ae2a41e73bc5b6/1362589459111-4G1KNIT2VDGYU33CRDBA/ke17ZwdGBToddI8pDm48kPx25wW2-RVvoRgxIT6HShBZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpwGbtSA7WutlFA3XjmDXUDFwmxX_uEhqHOBUlPnU0mYmf1Qvd6diXKmxQIX-f1CXeo/underwater_dark07.jpg")
#respond = rq.get(imag)

string_separated = imag.split('/')[-1]
print(string_separated)

#image_name = string_separated[-1]
#image_dir = f"./images/{image_name}"

#print(imag)
#with open(image_dir, 'wb') as im:
#    im.write(respond.content)



