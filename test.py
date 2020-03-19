# from flask import Flask, escape, url_for, request, redirect, Response
# app = Flask(__name__)

# #Request:
# # POST: 127.0.0.1:5000/
# # Body (JSON)
# # {
#     # "name": "aaa"
# # }

# userInfo = {
#     'aaa':'111',
#     'bbb':'222'
# }

# @app.route('/', methods=["GET","POST"])
# def test_header(): 
#     if ('X-Api-Key' not in request.headers.keys()):
#         return {'message': 'no key'}, 401
#     else:
#         key = request.headers['X-Api-Key']
#         if (key != 'A330ABF1BC1D4178A48088311D025BDD'):
#             return {'message': 'key is not correct'}, 401

#     name = request.json['name']
#     if (name in userInfo.keys()):
#         return userInfo[name]
#     else:
#         return {'message': 'user not found'}, 404


        
