import os, json
import sys
sys.path.append(".")
from flaskblog import app, db
from flaskblog.forms import PostForm
from flaskblog.models import Post, User

post = Post()
with open('flaskblog/post.json') as f:
   data = json.load(f)
   for i in data:
      author = User.query.filter_by(id=i['user_id']).first()
      post = Post(title=i['title'], content=i['content'], author=author)
      db.session.add(post)
      db.session.commit()

