# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

from get_article import get_article

app = Flask(__name__)


@app.route("/")
def home():
    """
    http://127.0.0.1:5000
    で起動する画面。Flaskの動作確認。
    """
    return "Hello, Flask!"


@app.route("/mobility_news/")
def get_top_page():
    """
    http://127.0.0.1:5000/mobility_news/
    で起動する画面。ホーム画面をイメージ。
    """
    # gazoonのニュースを取得
    gazoon_top_news = get_article.gazoon_news('https://gazoo.com/list/news/')
    # techcrunchのニュースを取得する
    techcrunch_mobility_contents = get_article.techcrunch_news(
        'https://jp.techcrunch.com/mobility/')

    return render_template(
        "mobility_toppage.html",
        gazoon_top_news=gazoon_top_news,
        techcrunch_mobility_contents=techcrunch_mobility_contents
    )

if __name__ == '__main__':
    app.run(debug = False)
