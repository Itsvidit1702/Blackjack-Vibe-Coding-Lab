
import random


class Deck:
    """A shuffled standard deck of 52 playing cards."""

    def __init__(self):
        suits = ("S", "H", "D", "C")
        ranks = (
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "J", "Q", "K", "A"
        )

        self.cards = [
            (rank, suit)
            for suit in suits
            for rank in ranks
        ]
        random.shuffle(self.cards)

    def draw(self):
        """Draw one card, or raise an error if the deck is empty."""
        if not self.cards:
            raise ValueError("The deck is empty.")
        return self.cards.pop()


def hand_value(hand):
    """Calculate a Blackjack hand's value, handling Aces as 1 or 11."""
    total = 0
    aces = 0

    for rank, suit in hand:
        if rank == "A":
            total += 11
            aces += 1
        elif rank in ("J", "Q", "K"):
            total += 10
        else:
            total += int(rank)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


