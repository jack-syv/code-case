from flask import Flask
from apis import api

def main():
    flask_app = Flask(__name__, instance_relative_config=True)
    flask_app.config.from_mapping(SECRET_KEY='dev')

    api.init_app(flask_app)
    flask_app.run()
    
if __name__ == '__main__':
    main()