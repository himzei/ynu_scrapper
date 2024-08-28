from flask import Flask, render_template, request, redirect, send_file
from scrapper import search_incruit, search_jobkorea
from file import save_to_csv

app = Flask(__name__)

page = 1
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

# db = {
#     "파이썬": [1, 2, 3, 4, .... 500], 
#     "간호사" : [1, 2, 3, ... 500] 
# }
# db["파이썬"]

@app.route("/export")
def export(): 
    keyword = request.args.get("keyword")
    
    if keyword == "": 
        return redirect("/")

    if keyword not in db:
        return redirect("/")
    
    save_to_csv(db[keyword])

    return send_file("./to_save.csv", as_attachment=True)


if __name__ == '__main__':
    app.run()