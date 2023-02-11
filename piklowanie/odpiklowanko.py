import pickle

from game_state import GameState

with open('../zapis.gry', 'rb') as f:
    moja_gra = pickle.load(f)

print(moja_gra)
