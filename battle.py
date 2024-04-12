from __future__ import annotations
from poke_team import Trainer, PokeTeam
from typing import Tuple
from battle_mode import BattleMode

from queue_adt.py import CircularQueue
from stack_adt.py import ArrayStack
from data_structures.referential_array import ArrayR

class Battle:
    def __init__(self, trainer1, trainer2, battle_mode):
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.battle_mode = battle_mode
        self.pokemon_queue1 = CircularQueue(6)  # Assuming maximum team size of 6
        self.pokemon_queue2 = CircularQueue(6)


 def load_teams(self):
        """ Load teams into the appropriate data structures based on battle mode. """
        if self.battle_mode == 'queue':  
            for pokemon in self.trainer1.team:
                self.pokemon_queue1.append(pokemon)
            for pokemon in self.trainer2.team:
                self.pokemon_queue2.append(pokemon)
        elif self.battle_mode == 'stack':
            self.pokemon_queue1 = ArrayStack(6)  
            self.pokemon_queue2 = ArrayStack(6)
            for pokemon in reversed(self.trainer1.team):  
                self.pokemon_queue1.push(pokemon)
            for pokemon in reversed(self.trainer2.team):
                self.pokemon_queue2.push(pokemon)

    def commence_battle(self) -> Trainer | None:
        raise NotImplementedError

    def _create_teams(self) -> None:
        raise NotImplementedError

    # Note: These are here for your convenience
    # If you prefer you can ignore them
    def set_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def rotate_battle(self) -> PokeTeam | None:
        raise NotImplementedError

    def optimise_battle(self) -> PokeTeam | None:
        raise NotImplementedError
        
  def fight(self):
        """ Commence battle between two trainers. """
        while not self.pokemon_queue1.is_empty() and not self.pokemon_queue2.is_empty():
            pokemon1 = self.pokemon_queue1.serve() if self.battle_mode == 'queue' else self.pokemon_queue1.pop()
            pokemon2 = self.pokemon_queue2.serve() if self.battle_mode == 'queue' else self.pokemon_queue2.pop()

            while pokemon1.is_alive() and pokemon2.is_alive():
                damage_to_pokemon2 = pokemon1.attack()
                pokemon2.defend(damage_to_pokemon2)

                if pokemon2.is_alive():
                    damage_to_pokemon1 = pokemon2.attack()
                    pokemon1.defend(damage_to_pokemon1)

            if pokemon1.is_alive():
                self.pokemon_queue1.append(pokemon1)  
            if pokemon2.is_alive():
                self.pokemon_queue2.append(pokemon2) 

if __name__ == '__main__':
    t1 = Trainer('Ash')
    t2 = Trainer('Gary')
    b = Battle(t1, t2, BattleMode.ROTATE)
    b._create_teams()
    winner = b.commence_battle()

    if winner is None:
        print("Its a draw")
    else:
        print(f"The winner is {winner.get_name()}")

battle = Battle(trainer1, trainer2, 'queue')
battle.load_teams()
battle.fight()
