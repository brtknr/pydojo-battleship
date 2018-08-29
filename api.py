from flask import Flask
from flask_restplus import Resource, Api
from flask import request

app = Flask(__name__)
api = Api(app)

import battleship as bs

games = dict()

@api.route('/game/<game_id>/')
class HelloWorld(Resource):
    def get(self, game_id):
        print(game_id)
        game = games.get(game_id, False)
        if not game:
            game = bs.Game()
            games[game_id] = game
        x = request.args.get('x',False)
        y = request.args.get('y',False)
        if x and y:
            game.board[int(x)%game.n][int(y)%game.m].hit = True
        print(game)
        return {'board': game.to_json()}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
