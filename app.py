from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():  # put application's code here
    return render_template('main.html')

@app.route('/minsk')
def minsk():
    return render_template('minsk.html')

@app.route('/vitebsk')
def vitebsk():
    return render_template('vitebsk.html')

@app.route('/mogilev')
def mogilev():
    return render_template('mogilev.html')

@app.route('/gomel')
def gomel():
    return render_template('gomel.html')

@app.route('/brest')
def brest():
    return render_template('brest.html')


@app.route('/grodno')
def grodno():
    return render_template('grodno.html')

@app.route('/1_page')
def one():
    return render_template('one.html')

@app.route('/2_page')
def two():
    return render_template('two.html')

@app.route('/3_page')
def three():
    return render_template('three.html')

@app.route('/4_page')
def four():
    return render_template('four.html')

@app.route('/5_page')
def five():
    return render_template('five.html')

@app.route('/6_page')
def six():
    return render_template('six.html')

@app.route('/7_page')
def seven():
    return render_template('seven.html')

@app.route('/8_page')
def eight():
    return render_template('eight.html')

@app.route('/9_page')
def nine():
    return render_template('nine.html')

@app.route('/10_page')
def ten():
    return render_template('ten.html')


@app.route('/11_page')
def eleven():
    return render_template('eleven.html')


@app.route('/12_page')
def twelve():
    return render_template('twelve.html')


@app.route('/13_page')
def thirteen():
    return render_template('thirteen.html')


@app.route('/14_page')
def fourteen():
    return render_template('fourteen.html')


@app.route('/15_page')
def fivteen():
    return render_template('fivteen.html')


@app.route('/16_page')
def sixteen():
    return render_template('sixteen.html')


@app.route('/17_page')
def seventeen():
    return render_template('seventeen.html')


@app.route('/18_page')
def eighteen():
    return render_template('eighteen.html')


@app.route('/19_page')
def nineteen():
    return render_template('nineteen.html')


@app.route('/20_page')
def twenty():
    return render_template('twenty.html')


@app.route('/21_page')
def twone():
    return render_template('twone.html')

@app.route('/22_page')
def twtwo():
    return render_template('twtwo.html')

@app.route('/23_page')
def twthree():
    return render_template('twthree.html')

@app.route('/24_page')
def twfour():
    return render_template('twfour.html')


@app.route('/25_page')
def twfive():
    return render_template('twfive.html')


@app.route('/26_page')
def twsix():
    return render_template('twsix.html')


@app.route('/27_page')
def twseven():
    return render_template('twseven.html')

@app.route('/28_page')
def tweight():
    return render_template('tweight.html')

@app.route('/29_page')
def twnine():
    return render_template('twnine.html')

@app.route('/30_page')
def thirty():
    return render_template('thirty.html')

@app.route('/31_page')
def trone():
    return render_template('trone.html')

@app.route('/32_page')
def trtwo():
    return render_template('trtwo.html')

@app.route('/33_page')
def trthree():
    return render_template('trthree.html')

@app.route('/34_page')
def trfour():
    return render_template('trfour.html')

@app.route('/35_page')
def trfive():
    return render_template('trfive.html')


if __name__ == '__main__':
    app.run()
