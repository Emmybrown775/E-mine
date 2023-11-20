from flask import Flask, render_template
from why_chose_data import why_choose_us
from vendors import Vendors, TopEarners

app = Flask(__name__)
app_vendors = Vendors()
app_top_earners = TopEarners()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", why_choose_us=why_choose_us)


@app.route('/vendors')
def buy_coupon():
    vendors = app_vendors.get_vendors()
    return render_template("buy_coupon.html", vendors=vendors)

@app.route('/top-earners')
def top_earners():
    apps_top_earners = app_top_earners.get_top_earners()
    return render_template("top_earners.html", top_earners=apps_top_earners)

@app.route('/about')
def about_us():
    return render_template("about_us.html")

@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')


@app.route('/faq')
def faq():
    return render_template("faq.html")

if __name__ == '__main__':
    app.run()

# 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
