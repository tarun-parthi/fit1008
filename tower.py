import random

from poke_team import Trainer, PokeTeam
from enum import Enum
from data_structures.stack_adt import ArrayStack
from data_structures.queue_adt import CircularQueue
from data_structures.array_sorted_list import ArraySortedList
from data_structures.sorted_list_adt import ListItem
from typing import Tuple

class BattleTower:
    MIN_LIVES = 1
    MAX_LIVES = 3

     def __init__(self) -> None:
        self.player_trainer = None
        self.enemy_trainers = ArrayStack(100)  
        self.total_enemy_lives = 0
        self.battles_fought = 0

 def set_my_trainer(self, trainer: Trainer) -> None:
        self.player_trainer = trainer
        self.player_trainer.get_team().set_team_lives(random.randint(self.MIN_LIVES, self.MAX_LIVES))

def generate_enemy_trainers(self, num_teams: int) -> None:
        for _ in range(num_teams):
            enemy_trainer = Trainer("Enemy")
            enemy_trainer.generate_random_team()
            enemy_trainer.get_team().set_team_lives(random.randint(self.MIN_LIVES, self.MAX_LIVES))
            self.total_enemy_lives += enemy_trainer.get_team().get_lives()
            self.enemy_trainers.push(enemy_trainer)

  

    # Hint: use random.randint() for randomisation
    def set_my_trainer(self, trainer: Trainer) -> None:
        raise NotImplementedError

    def battles_remaining(self) -> bool:
        return self.player_trainer.get_team().get_lives() > 0 and self.total_enemy_lives > 0

    def next_battle(self) -> Tuple[Trainer, Trainer, Trainer, int, int]:
       current_enemy = self.enemy_trainers.peek()
        battle_result = Battle(self.player_trainer, current_enemy).commence_battle()
        if battle_result == "Win":
            current_enemy.get_team().lose_life()
            self.total_enemy_lives -= 1
            self.battles_fought += 1
            if current_enemy.get_team().get_lives() == 0:
                self.enemy_trainers.pop()  
        elif battle_result == "Loss":
            self.player_trainer.get_team().lose_life()
     
        player_lives = self.player_trainer.get_team().get_lives()
        enemy_lives = current_enemy.get_team().get_lives() if current_enemy else 0
        
        return (self.player_trainer, current_enemy, battle_result, player_lives, enemy_lives)


    def enemies_defeated(self) -> int:
        return self.battles_fought
