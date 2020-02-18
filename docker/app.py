from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('body.html')


@app.route('/star-gazer')
def render_star_gazer():
    return render_template('body.html', description='THIS IS A DESCRIPTION', img='img', link='https://github.com/s-axford/StarGazer')


@app.route('/chirp-nets')
def render_chirp_nets():
    return render_template('body.html', description='THIS IS A DESCRIPTION', img='img', link='https://github.com/chirpnets/chirp-nets-mobile')


@app.route('/folklore')
def render_folklore():
    return render_template('body.html', description='THIS IS A DESCRIPTION', img='img', link='https://github.com/DelightedWaif/Folklore-Alexa-Skill')


@app.route('/mothership')
def render_mothership():
    return render_template('body.html', description='THIS IS A DESCRIPTION', img='img', link='https://github.com/DelightedWaif/mothership-character-generator')


@app.route('/playground')
def render_playground():
    return render_template('body.html', description='THIS IS A DESCRIPTION', img='img', link='https://github.com/DelightedWaif/learning')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
