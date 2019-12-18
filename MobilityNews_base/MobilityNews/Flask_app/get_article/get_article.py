from bs4 import BeautifulSoup
from time import sleep
import requests
import json

# 解析対象となるurlを直書き
gazoon_url = 'https://gazoo.com/list/news/'
techcrunch_mobility_url = 'https://jp.techcrunch.com/mobility/'

# 社内のプロキシを突破するために設定直書き
proxies = {
    'http': 'http://sassa.takuya@jp.fujitsu.com:9409203122@rep.proxy.nic.fujitsu.com:8080',
    'https': 'http://sassa.takuya@jp.fujitsu.com:9409203122@rep.proxy.nic.fujitsu.com:8080',
}

"""
デモ
"""


def BS_formatter(url):
    """
    BeautifulSoupを使用
    HTMLをpythonで解析することができるライブラリ
    """
    html = requests.get(url, proxies=proxies)
    bsObj = BeautifulSoup(html.content, "html.parser")
    return bsObj


def gazoon_news(gazoon_url):
    """
    gazoonトップページのニュースを取得する
    param@ url
    return@ [[記事タイトル,記事URL,記事画像URL],[記事タイトル,記事URL,記事画像URL]...]
    """
    # 戻り値用のリスト
    gazoon_top_contents = []
    # 解析対象のurl(今回はGazoon)
    url = gazoon_url
    # beautifulsoupで対象urlのwebページを解析
    bs_obj = BS_formatter(url)
    # ニュースサイトが書かれた属性を全て取得
    main_contents = bs_obj.find_all(class_='article-tile article-tile-main')

    # 取得してきた属性のタグを一つずつ解析していく
    for main_content in main_contents:
        # h2タグ内のテキストを取得し、タイトルとして格納
        article_title = main_content.h2.string
        # aタグ内のhref属性を取得し、ニュース記事の書かれたurlとして格納
        article_url = main_content.h2.a['href']
        # imgタグ内の画像のurlを取得し、画像のソースとして格納
        article_img_src = main_content.img['src']
        # 戻り値にそれぞれの情報を格納
        gazoon_top_contents.append(
            [article_title, article_url, article_img_src])

    return gazoon_top_contents


def techcrunch_news(tech_news_url):
    """
    techcrunch Mobilityトップページのニュースを取得する
    param@ url
    return@ [[記事タイトル,記事URL,記事画像URL],[記事タイトル,記事URL,記事画像URL]...]
    """
    techcrunch_mobility_contents = []
    url = tech_news_url
    bs_obj = BS_formatter(url)
    main_contents = bs_obj.find_all(class_='block-content')

    for main_content in main_contents:
        article_title = main_content.h2.string
        article_url = main_content.h2.a['href']
        article_img_src = main_content.img['data-src']
        techcrunch_mobility_contents.append(
            [article_title, article_url, article_img_src])

    return techcrunch_mobility_contents


def main():
    """
    テスト用
    出力の値を確認する
    """
    tech_url = techcrunch_mobility_url
    a = techcrunch_news(tech_url)

    gazo_url = gazoon_url
    b = gazoon_news(gazo_url)


if __name__ == "__main__":
    main()
