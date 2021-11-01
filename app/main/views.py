from ..request import get_news
from . import main
from flask import render_template,request
from ..models import News_Article

#Our views
@main.route('/')
def index():
    business_news = get_news('business')
    entertainment_news = get_news('entertainment')
    science_news = get_news('science')
    title = 'News platform'
    return render_template('index.html',business=business_news, entertainment=entertainment_news,science=science_news)



