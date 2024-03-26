import random
from Players import Player,Generous,Selfish,RandomPlayer,CopyCat,Grudger,Detective
class Game:
    def __init__(self):
        self.players = [
            CopyCat("CopyCat Player"),
            Selfish("Selfish Player"),
            Generous("Generous Player"),
            Grudger("Grudger Player"),
            Detective("Detective Player"),
            # RandomPlayer("Random Player"),
            
        ]
        self.num_rounds = 10

    def start(self):
        print("Welcome to the Trust of Evolution game!")
        print("Let's start...\n")

        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]


                player1_last_action = "Cooperate"
                player2_last_action = "Cooperate"

                print(f"{player1.name} vs {player2.name}:")
                player1.money = player1.money
                player2.money = player2.money
                print(f"{player1.name} :{player1.money} vs {player2.name}:{player2.money} :")
                for round_number in range(1, self.num_rounds + 1):
                    

                    action1 = player1.perform_action(player2_last_action,round_number)
                    action2 = player2.perform_action(player1_last_action,round_number)

                    if action1 == "Cooperate" and action2 == "Cooperate":
                        player1.money += 2
                        player2.money += 2

                    elif action1 == "Cooperate" and action2 == "Betray":
                        player1.money += -1
                        player2.money += 3

                    elif action1 == "Betray" and action2 == "Cooperate":
                        player1.money += 3
                        player2.money += -1

                    elif action1 == "Betray" and action2 == "Betray":
                        player1.money += 0
                        player2.money += 0

                    player1_last_action = action1  
                    player2_last_action = action2

                print(f"{player1.name} final money: {player1.money}")
                print(f"{player2.name} final money: {player2.money}")
                print()
        print("Game over!")
    def show_result(self):
        print("Final Results:")
        for player in self.players:
            print(f"{player.name}: {player.money}")



def main():
    game = Game()
    game.start()
    game.show_result()
    

if __name__ == "__main__":
    main()
