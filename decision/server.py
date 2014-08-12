from decision import app

@app.route('/')
def index():
    return "OK"