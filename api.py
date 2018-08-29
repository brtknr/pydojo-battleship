from flask import Flask
from flask_restplus import Resource, Api
from flask import request

app = Flask(__name__)
api = Api(app)

import main


@api.route('/game')
class HelloWorld(Resource):
    def get(self):
        return {'board': main.game.to_json()}

    def put(self):
        x = int(request.form['x']) % main.n
        y = int(request.form['y']) % main.m
        main.game.board[x][y].hit = True
        print(main.game)
        return str(main.game)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
