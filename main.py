from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # We'll import routes later once the basic app works
    # from app.routes import main
    # app.register_blueprint(main)
    
    @app.route('/')
    def home():
        return "Hello World!"
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=3000)