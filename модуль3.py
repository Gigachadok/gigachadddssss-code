import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.xp = 0
        self.level =  1
    def show_stats(self):
        print(f"\n---{self.name} (Ур. {self.level}) | HP: {self.hp} | XP: {self.xp}/50 ---")
def start_game():

    print('Добро пожаловать в бурмалду!!!')     
    print('Введите имя своего персонажа:')
    name = input()
    player = Player(name)

    print(f"\n{player.name} спускается в сырые подземелья...")
    while player.hp > 0:
        player.show_stats()
        print("Что делаешь бра мой? \n1. Идти дальше во тьму \n2. Отдохнуть у костра (+30HP) \n3. Сбежать")
        choice = input("выбор 1/2/3 : ")
        
        if choice == "1":
            print("\n Ты пошел по темному коридору...")
            time.sleep(1)

            event = random.choice(["Монстр"] ["Пустота"])
            if event == "монстр":
                enemy_hp = random.randint(25, 45)
                print(f" охх, на тебя вылез чубака! (HP : {enemy_hp})")

                while enemy_hp > 0 and player.hp > 0:
                    player_damage = random.randint(12, 25)
                    enemy_damage = random.randint(6, 15)

                    enemy_hp -= player_damage
                    player.hp -= enemy_damage

                    print(f"ты шлепнул его на {player_damage} урона. У него хп осталось {max(0, enemy_hp)}")
                    print(f"он шлепнул тебя на {enemy_damage} урона. У него хп осталось {max(0, player.hp)}")
                    time.sleep(1.2)
start_game()


