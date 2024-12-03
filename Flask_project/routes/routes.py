

from flask import render_template, request
from flask import redirect
from backend.models import Post
from main import app, db

@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/posts')
def get_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        try:
            db.session.delete(post)
            db.session.commit()
            return redirect('/posts')
        except Exception as e:
            return f'Ошибка при удалении записи: {e}'
    else:
        return 'Запись не найдена'

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        date = request.form['date']
        title = request.form['title']
        text = request.form['text']

        post = Post(date=date, title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/create')
        except:
            return 'Ошибка при добавлении записи'
    else:
        return render_template('create.html')