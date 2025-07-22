from flask import Flask
from routes.login import login_bp
from routes.main import main_bp
from routes.dashboard import dashboard_bp

app = Flask (__name__)

app.register_blueprint (login_bp)
app.register_blueprint (main_bp)
app.register_blueprint (dashboard_bp)
if __name__ == '__name__':
    app.run(debug=True)