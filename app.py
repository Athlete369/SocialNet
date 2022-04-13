from distutils.log import debug
from json import JSONDecodeError
from  flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    content = db.Column(db.String,nullable=False)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name =  request.form.get('name')
        post =  request.form.get('post')
        
        new_post = Posts(name=name,content = post)
        db.session.add(new_post)
        db.session.commit()

    if request.method == 'GET':
        pass
    posts = Posts.query.all()
    return render_template('index.html',posts=posts)

if __name__ == '__main__':
    app.run(debug=True)