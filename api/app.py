from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pymysql
import json

app = Flask(__name__)
cors = CORS(app)

db = pymysql.connect(host="localhost",user="root",password="root",database="bbsdb")
cursor = db.cursor()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/register',methods=['POST'])
def register():
  if len(request.form)==0:
    return 'failed'
  else:
    sql_query = "SELECT * FROM user WHERE email='%s'" % request.form['email']
    cursor.execute(sql_query)
    user = list(cursor.fetchall())
    if len(user)==0:
      sql_insert = '''
      INSERT INTO user(nickname,email,password,avatar,introduction,sex,level,star_post,star_topic) 
      VALUE('%s','%s','%s','%s','%s','%s','%s','%s','%s')
      ''' % (request.form['nickname'],request.form['email'],request.form['password'],request.form['avatar'],request.form['introduction'],request.form['sex'],request.form['level'],'','')
      cursor.execute(sql_insert)
      db.commit()
      return jsonify({'msg':'注册成功','status':200})
    else:
      return jsonify({'msg':'用户已存在','status':502})

@app.route('/user/login',methods=['POST'])
def login():
  if len(request.form)==0:
    return 'failed'
  else:
    sql_query = "SELECT * FROM user WHERE email='%s'" % request.form['email']
    cursor.execute(sql_query)
    user = list(cursor.fetchall())
    if len(user)==0:
      return jsonify({'msg':'用户不存在','status':502})
    else:
      user = list(user[0])
      user_data = {
        'id': user[0],
        'nickname': user[1],
        'email': user[2],
        'password': user[3],
        'avatar': user[4],
        'introduction': user[5],
        'sex': user[6],
        'level': user[7],
        'star_post': user[8],
        'star_topic': user[9],
      }
      if user_data['password'] == request.form['password']:
        print('登陆成功')
        return jsonify({'msg':'登陆成功','status':200,'data':user_data})
      else:
        print('密码错误')
        return jsonify({'msg':'密码错误','status':202})

@app.route('/post/add_post',methods=['POST'])
def add_post():
  if len(request.form)==0:
    return 'failed'
  else:
    user_id = request.form['user_id']
    sql_query = "SELECT * FROM user WHERE id='%s'" % user_id
    cursor.execute(sql_query)
    user = list(cursor.fetchall())
    if len(user)!=0:
      sql_insert = '''
      INSERT INTO post(content,topic,user_id,star_num,comment_num,share_num,read_num,is_share,share_id,is_digest,hot_val) 
      VALUE('%s','%s','%s','%s','%s','%s','%s','%s','%s')
      ''' % (request.form['content'],request.form['topic'],request.form['user_id'],0,0,0,0,0,'',0,1)
      cursor.execute(sql_insert)
      db.commit()
      return jsonify({'msg':'发布成功','status':200})
    else:
      return jsonify({'msg':'用户不存在','status':502})

@app.route('/post/get_post',methods=['GET'])
def get_post():
  post_id = request.args.get('post_id')
  sql_query = "SELECT * FROM post WHERE id='%s'" % post_id
  cursor.execute(sql_query)
  post = list(cursor.fetchall())
  if len(post)!=0:
    post = list(post[0])
    post_data = {
      'id': post[0],
      'content': post[1],
      'topic_id': post[2],
      'user_id': post[3],
      'star_num': post[4],
      'comment_num': post[5],
      'share_num': post[6],
      'read_num': post[7],
      'is_share': post[8],
      'share_id': post[9],
      'is_digest': post[10],
      'hot_val': post[11],
    }
    return jsonify({'msg':'获取帖子成功','status':200,'data':post_data})
  else:
    return jsonify({'msg':'帖子不存在','status':502})

  
@app.route('/post/edit_post')
def edit_post():
  return 'edit_post'
  
@app.route('/post/del_post')
def del_post():
  return 'del_post'
  
@app.route('/post/star_post')
def star_post():
  return 'star_post'

if __name__ == '__main__':
    app.run(debug=True)

''' 
测试用例
  user
    login
      curl -Uri 'http://127.0.0.1:5000/login' -Body "nickname=test&password=test_pwd&email=test_email" -Method 'POST'
    register
      curl -Uri 'http://127.0.0.1:5000/register' -Body "nickname=a&email=a&password=a&avatar=a&introduction=a&sex=a&level=a&star_post=a&star_topic=a" -Method 'POST'
'''