from pokemon import *
import random
from typing import List
from battle_mode import BattleMode

class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = ArrayR(self.TEAM_LIMIT) # change None value if necessary
        self.team_count = 0

    def choose_manually(self):
        print("Please choose your Pokemon (Enter the name): ")
        chosen = 0
        while chosen < self.TEAM_LIMIT:
            for index, poke in enumerate(self.POKE_LIST, 1):
                print(f"{index}. {poke}")
            choice = input("Choose a Pokemon by number (or 'done' to finish): ")
            if choice.lower() == 'done' and chosen > 0:
                break
            try:
                poke_choice = self.POKE_LIST[int(choice) - 1]
                self.team[chosen] = poke_choice()  
                chosen += 1
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

        self.team_count = chosen

    def choose_randomly(self) -> None:
         self.team = ArrayR([random.choice(self.POKE_LIST)() for _ in range(self.TEAM_LIMIT)])
        self.team_count = self.TEAM_LIMIT
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for i in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team[i] = all_pokemon[rand_int]()
            self.team_count += 1

    def regenerate_team(self, battle_mode: BattleMode, criterion: str = None) -> None:
        raise NotImplementedError

    def assign_team(self, criterion: str = None) -> None:
        raise NotImplementedError

    def assemble_team(self, battle_mode: BattleMode) -> None:
        raise NotImplementedError

    def special(self, battle_mode: BattleMode) -> None:
        raise NotImplementedError

    def __getitem__(self, index: int):
       if 0 <= index < self.team_count:
            return self.team[index]
        else:
            raise IndexError("Team index out of range")


    def __len__(self):
        return self.team_count

    def __str__(self):
        team_str = "Team:\n"
        for i in range(self.team_count):
            team_str += f"{i+1}. {str(self.team[i])}\n"  # Assuming each Pokemon has a __str__ method.
        return team_str

class Trainer:

    def __init__(self, name) -> None:
        raise NotImplementedError

    def pick_team(self, method: str) -> None:
        raise NotImplementedError

    def get_team(self) -> PokeTeam:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def register_pokemon(self, pokemon: Pokemon) -> None:
        raise NotImplementedError

    def get_pokedex_completion(self) -> float:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())
