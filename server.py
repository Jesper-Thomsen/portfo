from flask import Flask, render_template, request, redirect
from scrape import getlinks, create_custom_hn, make_html_friendly
from weather import make_link_and_data, extract_data

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()

        return redirect("thank_you.html")
    else:
        return 'something went wrong, try again'


@app.route('/scraper.html')
def scraper_page():
    hacker_news = make_html_friendly(create_custom_hn(getlinks(5)[0], getlinks(5)[1]))
    return render_template('scraper.html', hacker_news=hacker_news)

@app.route('/submit_city', methods=['POST', 'GET'])
def submit_city():
    if request.method == 'POST':
        data = request.form.to_dict()
        data=extract_data(make_link_and_data(data['city']))
        return render_template('weather_response.html', weather_data=data)
    else:
        return 'something went wrong, try again'
