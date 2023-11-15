from flask import Flask, render_template
from why_chose_data import why_choose_us

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", why_choose_us=why_choose_us)


if __name__ == '__main__':
    app.run()


# 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
