
from cards import Deck, hand_value


class Blackjack:
    def __init__(self):
        self.chips = 100
        self.wager = 0
        self.round_settled = False

    def show(self, player, dealer, hide=True):
        if hide:
            shown_dealer = [f"{dealer[0][0]}{dealer[0][1]}", "??"]
        else:
            shown_dealer = [f"{r}{s}" for r, s in dealer]

        print("Dealer:", " ".join(shown_dealer))
        print(
            "Player:", " ".join(f"{r}{s}" for r, s in player),
            "=", hand_value(player)
        )

    def get_wager(self):
        while True:
            raw = input(f"Your chips: {self.chips}. Enter wager: ").strip()

            try:
                wager = int(raw)
            except ValueError:
                print("Invalid wager. Enter a whole number.")
                continue

            if wager <= 0:
                print("Wager must be greater than zero.")
            elif wager > self.chips:
                print("You cannot wager more chips than you have.")
            else:
                return wager

    def settle(self, result):
        """Settle a round once. The wager is already reserved."""
        if self.round_settled:
            return

        if result == "win":
            self.chips += 2 * self.wager
            print(f"You win {self.wager} chips!")
        elif result == "loss":
            print(f"You lose your {self.wager}-chip wager.")
        else:
            self.chips += self.wager
            print("Push! Your wager is returned.")

        self.round_settled = True
        print("Current chips:", self.chips)

    def round(self):
        if self.chips <= 0:
            print("You have no chips left.")
            return False

        self.wager = self.get_wager()
        self.chips -= self.wager
        self.round_settled = False

        deck = Deck()

        try:
            player = [deck.draw(), deck.draw()]
            dealer = [deck.draw(), deck.draw()]
        except ValueError:
            self.chips += self.wager
            print("Unable to deal cards. Your wager has been returned.")
            return False

        self.show(player, dealer)

        player_blackjack = len(player) == 2 and hand_value(player) == 21
        dealer_blackjack = len(dealer) == 2 and hand_value(dealer) == 21

        if player_blackjack or dealer_blackjack:
            self.show(player, dealer, hide=False)

            if player_blackjack and dealer_blackjack:
                self.settle("push")
            elif player_blackjack:
                self.settle("win")
            else:
                self.settle("loss")

            return True

        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()

            if key == "q":
                self.chips += self.wager
                print("Round cancelled. Your wager has been returned.")
                return False
            elif key == "s":
                break
            elif key == "h":
                try:
                    player.append(deck.draw())
                except ValueError:
                    self.chips += self.wager
                    print("Deck empty. Your wager has been returned.")
                    return False

                self.show(player, dealer)

                if hand_value(player) > 21:
                    self.show(player, dealer, hide=False)
                    print("Player busts.")
                    self.settle("loss")
                    return True
            else:
                print("Invalid command. Enter h, s, or q.")

        while hand_value(dealer) < 17:
            try:
                dealer.append(deck.draw())
            except ValueError:
                self.chips += self.wager
                print("Deck empty. Your wager has been returned.")
                return False

        self.show(player, dealer, hide=False)

        player_total = hand_value(player)
        dealer_total = hand_value(dealer)

        if dealer_total > 21 or player_total > dealer_total:
            self.settle("win")
        elif player_total < dealer_total:
            self.settle("loss")
        else:
            self.settle("push")

        return True

    def run(self):
        print("Blackjack — starting chips:", self.chips)

        while self.chips > 0:
            if not self.round():
                return

            if self.chips <= 0:
                break

            if input("Play again? [y/n]: ").strip().lower() != "y":
                return

        print("Game over: no chips remaining.")
