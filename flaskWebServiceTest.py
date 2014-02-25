from flask import Flask, url_for, Response, jsonify

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/test') #sending XML response
def test():
    xml = "<Person name='Foo McBar'><age>42</age></Person>"
    return Response(xml, mimetype='text/xml')

@app.route('/test1') #sending JSON response
def test1():
    temp = [
        {
            'name': u'Shayan',
            'Age': 26
        },
        {
            'name': u'Sinha',
            'Age': 26
        }
    ]
    return jsonify({'persons': temp})

if __name__ == '__main__':
    app.run()