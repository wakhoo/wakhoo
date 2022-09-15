from flask import render_template, request, jsonify,Blueprint
from combine.static.db import db
moviereview_api = Blueprint('moviereview_api', __name__,
                        template_folder='templates')


import requests
from bs4 import BeautifulSoup

@moviereview_api.route('/movie')
def home2():
   return render_template('index.html')

@moviereview_api.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    image = og_image['content']
    title = og_title['content']
    description = og_description['content']

    doc = {
        'image':image,
        'title':title,
        'desc':description,
        'star':star_receive,
        'comment':comment_receive
    }

    db.movies.insert_one(doc)

    return jsonify({'msg':'POST 연결 완료!'})

@moviereview_api.route("/movie", methods=["GET"])
def movie_get():
    movies_list = list(db.movies.find({},{'_id':False}))
    return jsonify({'movies':movies_list})

@moviereview_api.route("/movie", methods=["GET"])
def find_movie():
    movies_list = list(db.movies.find({},{'_id':False}))
    return jsonify({'movies':movies_list})
