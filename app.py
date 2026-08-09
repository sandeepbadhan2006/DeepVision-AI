from flask import Flask, render_template, request,jsonify
from src.pred_pipeline.email_pipeline import predict_email
from src.password.password_strength import check_password
from src.chat.chat import get_ai_response
from src.url.url import analyze_url
from src.cyber_news.news import get_news

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home_page.html")



@app.route("/email", methods=["GET", "POST"])
def email():

    prediction = None
    confidence = None
    risk = None
    email_text = ""

    if request.method == "POST":

        email_text = request.form["email"]

        prediction, confidence, risk = predict_email(email_text)

    return render_template(
        "email.html",
        prediction=prediction,
        confidence=confidence,
        risk=risk,
        email=email_text
    )
    
@app.route("/password_strength", methods=["GET", "POST"])
def password_strength():

    password = ""
    prediction = None
    score = 0
    breakdown = None

    if request.method == "POST":

        password = request.form["password"]

        prediction, score, breakdown = check_password(password)

    return render_template(
        "password_strength.html",
        password=password,
        prediction=prediction,
        score=score,
        breakdown=breakdown
    )
    

@app.route("/chat")
def chat_page():
    return render_template("chat.html")

@app.route("/api/chat", methods=["POST"])
def chat():

    try:
        message = request.json["message"]

        reply = get_ai_response(message)

        return jsonify({
            "reply": reply
        })

    except Exception as e:

        print(e)

        return jsonify({
            "reply": str(e)
        }), 500
        
@app.route("/news")
def cyber_news():

    news = get_news()

    return render_template(
        "news.html",
        news=news
    )
    
@app.route("/url")
def url():
    return render_template("url.html")


@app.route("/url_analyzer", methods=["POST"])
def url_analyzer():

    url = request.form["url"]

    result = analyze_url(url)

    return render_template(
        "url.html",
        url=url,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)