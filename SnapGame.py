import itertools
import random
import typing
import sys


class SnapGame():
    NUMBER_OF_PLAYERS = 0
    NUMBER_OF_DECKS = 1
    SUITS = ['hearts', 'diamonds', 'spades', 'clubs']
    CARD_VALUES = [x for x in range(1, 14)]

    def start_game(self):
        self.get_input()
        players_scores_list = self.run_simulation()
        sorted_scores = sorted(players_scores_list, key=lambda d : d["final_score"], reverse=True)
        print("And your winner is..... player: " + str(sorted_scores[0]["playerId"]) + " !!!!")
        print("With a final score of : "+ str(sorted_scores[0]["final_score"]) + "!!!")

    def run_simulation(self):
        decks = self.make_decks(self.CARD_VALUES, self.SUITS, self.NUMBER_OF_DECKS)
        player_hands = self.get_player_hands(decks, self.NUMBER_OF_DECKS, self.NUMBER_OF_PLAYERS)
        players_scores = []

        cards_in_pile = []
        for card_count in range(0, len(player_hands[0]["cards"])):
            for player in player_hands:
                cards_in_pile.append(player["cards"][card_count])
                if len(cards_in_pile) > 1:
                    if cards_in_pile[-1][0] == cards_in_pile[-2][0]:
                        player_calls_snap = random.randint(1, self.NUMBER_OF_PLAYERS)
                        winning_player = {
                            "playerId": player_calls_snap,
                            "cards": cards_in_pile
                        }
                        players_scores.append(winning_player)
                        cards_in_pile = []

        players_final_scores = []

        for player_id in range(1, self.NUMBER_OF_PLAYERS+1):
            player_final_score = 0
            for item in players_scores:
                if item["playerId"] == player_id:
                    player_final_score += len(item["cards"])

            player_score ={
                "playerId":player_id,
                "final_score":player_final_score
            }
            players_final_scores.append(player_score)

        return players_final_scores

    def make_decks(self, card_values: typing.List[int], suits:typing.List[str], num_of_decks:int) -> typing.List[tuple]:
        decks = []
        for x in range(1, num_of_decks+1):
            deck = list(itertools.product(card_values, suits))
            random.shuffle(deck)
            decks.append(deck)
        cards_in_play = []
        for deck in decks:
            for cards in deck:
                cards_in_play.append(cards)

        return list(cards_in_play)

    def get_player_hands(self, decks, number_of_decks,number_of_players) -> typing.List[typing.Dict]:
        number_of_cards_to_take = int((52 * number_of_decks) / number_of_players)
        amount_to_increase_by = number_of_cards_to_take
        player_hands = []
        counter = 0
        for player in range(1, number_of_players + 1):
            player_cards = decks[counter: number_of_cards_to_take]
            player_item = {
                "playerId": player,
                "cards": player_cards
            }
            counter +=amount_to_increase_by
            number_of_cards_to_take += amount_to_increase_by

            player_hands.append(player_item)

        return player_hands

    def get_input(self):
        print("**********   Welcome to the Snap Game!   **********\n")
        self.NUMBER_OF_PLAYERS = self.check_input_isnumeric("Please enter the number of players: \n")
        self.NUMBER_OF_DECKS = self.check_input_isnumeric("Please enter the number of decks you are playing with: \n")

    @staticmethod
    def check_input_isnumeric(msg) -> int:
        while True:
            try:
                numeric_val = input(msg)
                numeric_val = int(numeric_val)
                return numeric_val
            except:
                print("Please enter an integral number value eg: 4")


if __name__ == "__main__":
    p = SnapGame()
    p.start_game()
    sys.exit(0)