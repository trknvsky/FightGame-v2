from game_constants import *
from parsing_warriors_csv import WARRIORS
from random import randint


class Player():

    def __init__(self, warriors_data, number):
        self.name = warriors_data[number].get('name')
        self.power = warriors_data[number].get('power')
        self.hp = warriors_data[number].get('hp')
        self._damage = 0

    def get_damage(self):
        return self._damage

    def set_damage(self, skill):
        self._damage = self.power * skill

    def __gt__(warrior_1, warrior_2):
        return warrior_1.hp > warrior_2.hp

    def __eq__(warrior_1, warrior_2):
        return warrior_1.hp == warrior_2.hp


class Fight():
    def select_player(self, choose=False):
        if choose:
            warrior = int(input('Select a warrior:\n\t1: strength\n\t 2: agility\n\t 3: intelligence\n\t'))
            player = Player(WARRIORS, warrior - 1)
        else:
            warrior = randint(0, 2)
            player = Player(WARRIORS, warrior)
        return player

    def play(self):
        player = self.select_player(True)
        opponent = self.select_player(False)
        player.set_damage(randint(1, 3))
        opponent.set_damage(randint(1, 3))
        if (player > opponent) is True:
            print('Your hero has bigger hp than opponents hero !')
        elif (player == opponent) is True:
            print('You have identical heroes with opponent !')
        elif (player > opponent) is False:
            print('Opponents hero has bigger hp than your hero !')

        print('Your warrior:\n\t', player.__dict__)
        print('Opponents warrior:\n\t', opponent.__dict__)

        while True:
            print('Your players hp:\t', player.hp)
            print('Opponents players hp:\t', opponent.hp)
            kick = int(input('Select a kick:\n\t1: headkick\n\t2: bodykick\n\t3: lowkick\n'))
            block = int(input('What you want to block?:\n\t1: head\n\t2: body\n\t3: legs\n'))
            opponent_kick = randint(1, 3)
            opponent_blok = randint(1, 3)

            if kick != opponent_blok:
                print('You hit an opponent by {} damage!'.format(player._damage))
                opponent.hp -= player._damage
            else:
                print('Opponent blocked your hit!')
            if block != opponent_kick:
                print('Opponent hit you by {} damage!'.format(opponent._damage))
                player.hp -= opponent._damage
            else:
                print('You blocked opponents hit!')
            if player.hp <= 0:
                print(GAME_OVER)
                break
            if opponent.hp <= 0:
                print(WINNER_MESSAGE)
                break
