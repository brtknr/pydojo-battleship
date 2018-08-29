from flask import Flask
from flask_restplus import Resource, Api
from flask import request

app = Flask(__name__)
api = Api(app)

import battleship as bs

@api.route('/game')
class HelloWorld(Resource):
    def get(self):
        x = request.args.get('x',False)
        y = request.args.get('y',False)
        if x and y:
            bs.game.board[int(x)%bs.n][int(y)%bs.m].hit = True
        print(bs.game)
        return {'board': bs.game.to_json()}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
