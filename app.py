from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return """  <h1> Welcome to Resturant yoyo test page </h1>
                <h2> <a href="/delivery"> delivery page </a> </h2>
                <h2> <a href="/pos"> point of sale </a> </h2>
                <h2> <a href="/marketing"> Marketing Interface </a> </h2>
                <h2> <a href="/pos2"> point of sale with layout </a> </h2>"""
                
@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/pos')
def pos():
    return render_template('pos.html')

@app.route('/pos2')
def pos2():
    return render_template('PosWithCss.html')

@app.route('/marketing')
def marketing():
    return render_template('marketing.html')


if __name__ == '__main__':
    app.run(debug=True)                