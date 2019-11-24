from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/yogurt')
def yogurt():
    return 'Frozen yogurt my favourite!'

@main.route('/chocolateBrownies')
def chocolateBrownies():
    return render_template('chocolateBrownies.html')

@main.route('/blog')
def blog():
    return render_template('blog.html')