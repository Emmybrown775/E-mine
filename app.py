from flask import Flask, render_template
from why_chose_data import why_choose_us
from vendors import Vendors, TopEarners
from forms import LoginForm, RegisterForm, CouponCheckForm
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app_vendors = Vendors()
app_top_earners = TopEarners()
Bootstrap(app)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html", why_choose_us=why_choose_us)

@app.route("/login")
def login():
    loginform = LoginForm()
    return render_template("sign_in.html",form=loginform)

@app.route('/register')
def register():
    register_form = RegisterForm()
    return render_template("sign_up.html", form=register_form)


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

@app.route('/coupon-check')
def coupon_check():
    coupon_check_form = CouponCheckForm()
    return render_template("coupon_checker.html", form=coupon_check_form)

if __name__ == '__main__':
    app.run()

# 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
