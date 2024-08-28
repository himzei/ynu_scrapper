from flask import Flask, render_template, request
from scrapper import search_incruit, search_jobkorea

app = Flask(__name__)

page = 10
db = {}

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/search")
def search(): 
    keyword = request.args.get("keyword")

    if keyword in db: 
        jobs = db[keyword]
    else: 
        jobs_incruit = search_incruit(keyword, page)
        jobs_jobkorea = search_jobkorea(keyword, page)
        jobs = jobs_incruit + jobs_jobkorea
        db[keyword] = jobs

           
    return render_template(
        "search.html", 
        keyword=keyword, 
        jobs=enumerate(jobs), 
        counts=len(jobs)
        )

if __name__ == '__main__':
    app.run(debug=True)