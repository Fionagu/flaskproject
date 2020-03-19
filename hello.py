# from flask import Flask, escape, url_for, request, redirect, Response
# app = Flask(__name__)

# userInfo = {
#     'aaa':'111',
#     'bbb':'222'
# }

# #==========================================路由
# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello' , methods=['POST'])
# def hello():
#     return 'hello world'

# #==========================================变量规则
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # escape用处?
#     #  input url /user/fiona gu ---> /user/fiona%20gu
#     # with/without escape, print 'fiona gu'
#     return 'User %s' % escape(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     return 'Subpath %s' % escape(subpath)

# #==========================================唯一的URL/重定向行为
# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# #==========================================URL构建
# @app.route('/login')
# def login():
#     return 'login page'

# #profile is used
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))    
#     print(url_for('show_user_profile', username='John Doe'))

# #重定向
# #重定向分为永久性重定向和暂时性重定向，
# # 在页面上体现的操作就是浏览器会从一个页面自动跳转到另外一个页面。
# # 比如用户访问了一个需要权限的页面，
# # 但是该用户当前并没有登录，因此我们应该给他重定向到登录页面
# @app.route('/profile/')
# def profile():
#     if request.args.get('name'):
#         return '个人中心页面'
#     else:
#         return redirect(url_for('login'))

# #用法
# #http://127.0.0.1:5000/profile/?name=a ---> 个人中心页面
# #http://127.0.0.1:5000/profile/ ---> login page

# @app.route('/testheader', methods=["POST"])
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


        
