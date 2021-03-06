from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news, get_articles
from ..models import News, Articles


# Views
@main.route('/')  # homepage route
def index():
    message = 'Welcome to your favorite News Channel'
    title = 'Taarifa za Habari'

    current_news = get_news()
    return render_template('index.html', message=message, title=title, current_news=current_news)


@main.route('/news_article/<id>')  # news article route
def news_article(id):

    articles = get_articles(id)
    return render_template('news_article.html', articles=articles)
