from app import app

@app.route("/ola")
def ola():
    return "ola mundo em Flask!!"
