from app import app

@app.route('/')
def front_page():
    return "Welcome"
