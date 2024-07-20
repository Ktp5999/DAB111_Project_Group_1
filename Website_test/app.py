from flask import Flask
from routes.home import home_bp
from routes.about import about_bp
from routes.data import data_bp

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(data_bp)

if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)
