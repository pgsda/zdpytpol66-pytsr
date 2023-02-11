import pickle

from game_state import GameState

moja_gra = GameState(100, 2, ['axe'])

with open('../zapis.gry', 'wb') as f:
    pickle.dump(moja_gra, f)
