from flask import Flask, render_template
import  data
app = Flask(__name__)

@app.route('/')
def index():
    datax = data.get_data()
    return render_template("index.html", len = len(datax), data = datax)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')