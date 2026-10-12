# Blackjack Game — Vibe Coding Lab

## Overview
A command-line Blackjack game built with Python. The player plays against the dealer using a standard 52-card deck.

## Features
- Shuffled deck of 52 playing cards.
- Correct Blackjack hand scoring, including Aces counting as 1 or 11.
- Player can hit, stand, or quit.
- Dealer draws cards until reaching a total of at least 17.
- Detects Blackjack, busts, wins, losses, and ties.
- Betting system that allows players to wager chips each round.
- Validates wagers to prevent invalid amounts or bets exceeding available chips.
- Displays the player's cards, dealer's visible card, and current chip balance.
- Handles invalid commands and empty-deck errors.

## Requirements
- Python 3.10 or newer recommended.
- No third-party packages required.

## How to Run
1. Open a terminal in the project directory.
2. Run:

   ```bash
   python main.py
   ```

   On Windows, you can also use:

   ```powershell
   py main.py
   ```

## How to Play
- Enter a valid positive whole-number wager.
- Enter `h` to draw another card.
- Enter `s` to stand.
- Enter `q` to quit the current game.
- Choose `y` to play another round or `n` to stop.

## Testing
The hand-scoring function should correctly handle Aces as either 1 or 11. Wager validation should reject non-numeric, zero, negative, and unaffordable wagers.

## Project Files
- `main.py` — starts the game.
- `game.py` — contains game logic, betting, and round outcomes.
- `cards.py` — creates the deck and calculates hand values.