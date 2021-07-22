from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Where is DB stored
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Create a model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Post id ' + str(self.id)


# Route
@app.route('/')
def index():
    return render_template('index.html')

# return data into html
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        create_post = Post(
            title=title,
            content=content,
            author='wgprtm_'
        )
        db.session.add(create_post)
        db.session.commit()
        return redirect('/posts')

    all_posts = Post.query.order_by(Post.created_at).all()
    return render_template('posts.html', posts=all_posts)

@app.route('/home/<string:name>')
def home(name):
    return "Hello, " + name

@app.route('/method', methods=['GET', 'POST'])
def route_method():
    return "Route with allowed request method"

if __name__ == "__main__":
    app.run(debug=True)