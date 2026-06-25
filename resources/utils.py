from __future__ import annotations
"""
Utilities for use with the Custom Program (Wordy)
"""

__author__ = "Kasra Asarroodi"

__author__ = "COMP1102 / COMP8702 / ENGR1721"


from dataclasses import dataclass, field
from enum import Enum
import random
MAX_ATTEMPTS: int = 6 # The maximum number of guess attempts.


def display_title():
    """
    Displays the program title.
    """
    print("Welcome to")
    print(" ___ ___ ___ ___ ___")
    print("| W | O | R | D | Y |")
    print("[___|___|___|___|___]")
    print()


def menu(stats: Statistics):
    """
    Displays the program menu and prompts the user for a menu option.
    """
    choice: str = ""
    while choice != "Q":
        print("1. Start a new game")
        print("2. View statistics")
        print("Q. Quit")
        choice = input("Enter your choice: ").upper()
        if choice == "1":
            print("Starting a new game...")
            play_game(new_game(random.choice(get_words()), MAX_ATTEMPTS), stats)
        elif choice == "2":
            print("Viewing statistics...")
            display_statistics(stats)
        elif choice == "Q":
            print("Thanks for playing!")
        else:
            print("Unknown option.")

            
class LetterScore(Enum):
    CORRECT = "+"
    PRESENT = "-"
    ABSENT = "."


@dataclass
class Guess:
    word: str
    scores: list[LetterScore] = field(default_factory=list)
    is_correct: bool = False 


@dataclass
class Game:
    secret_word: str
    guesses: list[Guess] = field(default_factory=list)
    max_attempts: int = 6
    has_won: bool = False   


@dataclass
class Statistics:
    games_played: int = 0
    wins: int = 0
    losses: int = 0
    guesses: int = 0


def new_game(Random: str, attempts: int) -> Game:
    """
    Creates a new game with the specified secret word and number of attempts.
    """
    return Game(secret_word=Random.upper(), max_attempts=attempts) 


def get_guess() -> str:
    """
    Prompts the user to enter a guess and returns it as a string.
    """
    guess = input("Enter your guess: ").upper()
    while len(guess) != 5 or not guess.isalpha():
        print("Invalid guess. Word must be exactly five letters and contain only letters.")
        guess = input("Enter your guess: ").upper()
        if len(guess) == 5 and guess.isalpha():
            return guess.upper()

    return guess


def score_guess(guess: str, secret_word: str) -> Guess:
    """
    Identifies which letters from the guess match the letters in the secret word.
    """
    scores: list[LetterScore] = [LetterScore.ABSENT for _ in range(5)]
    remaining_letters = list(secret_word)
    for i in range(5):
        if guess[i] == secret_word[i]:
            scores[i] = LetterScore.CORRECT
            remaining_letters.remove(guess[i])
    for i in range(5):
        if scores[i] != LetterScore.CORRECT:
            if guess[i] in remaining_letters:
                scores[i] = LetterScore.PRESENT
                remaining_letters.remove(guess[i])

            else:
                scores[i] = LetterScore.ABSENT
    return Guess(word=guess, scores=scores, is_correct=guess == secret_word) 
    # Returns the score of the guess made.


def play_game(game: Game, stats: Statistics):
    """
    Creates a loop which keeps the game runninng until a certain condition is met.
    """
    while len(game.guesses) < game.max_attempts and not game.has_won:
        guess = get_guess()
        scored_guess = score_guess(guess, game.secret_word)
        game.guesses.append(scored_guess)
        stats.guesses += 1
        display_feedback(game)
        if scored_guess.is_correct:
            game.has_won = True
            print("Congratulations! You've guessed the word!")
            print(f"You have won the game in {len(game.guesses)} attempts!")
            stats.wins += 1
        elif len(game.guesses) == game.max_attempts:
            print(f"Game over! The secret word was: {game.secret_word}")
            stats.losses += 1
    stats.games_played += 1  


def display_feedback(game: Game):
    """
    Displays feedback for the player's guesses.
    """
    for guess in game.guesses:
        for i in range(5):
            
            if guess.scores[i] == LetterScore.CORRECT: 
                print(green(guess.word[i]), end="")
                
            elif guess.scores[i] == LetterScore.PRESENT:
                print(yellow(guess.word[i]), end="")
                
            else:
                print(grey(guess.word[i]), end="")    
    print()


def display_statistics(stats: Statistics):
    """
    Displays the player's game statistics.
    """
    print(f"Total Games played: {stats.games_played}")
    print(f"Total Wins: {stats.wins}")
    print(f"Total Losses: {stats.losses}")
    win_percentage = (
        stats.wins / stats.games_played * 100
        if stats.games_played > 0
        else 0
    )  

    print(f"Win percentage: {win_percentage:.2f}%") # Calculates the percentage of games won.
    
    return stats


def green(text: str) -> str:
    """
    Formats the given text to have a green background.
    Uses ANSI terminal colours.
    """
    return f"\033[042m {text} \033[0m "


def yellow(text: str) -> str:
    """
    Formats the given text to have a green background.
    Uses ANSI terminal colours.
    """
    return f"\033[043m {text} \033[0m "


def grey(text: str) -> str:
    """
    Formats the given text to have a green background.
    Uses ANSI terminal colours.
    """
    return f"\033[100m {text} \033[0m "


def get_words() -> list[str]:
    """
    Gets a list of five-letter words for Wordy.
    """
    return [
        "apple", "angry", "aisle", "atlas", "adult",
        "bread", "brush", "beach", "birth", "basic",
        "candy", "crane", "cloud", "clean", "coast",
        "dance", "dream", "daily", "draft", "drink",
        "early", "earth", "eagle", "entry", "error",
        "flame", "field", "fruit", "floor", "fresh",
        "glass", "green", "grape", "ghost", "guide",
        "house", "heart", "heavy", "honey", "habit",
        "image", "index", "irony", "inner", "input",
        "joint", "judge", "juice", "jelly", "joker",
        "knife", "knock", "koala", "kneel", "known",
        "light", "lemon", "logic", "level", "lucky",
        "music", "money", "movie", "metal", "mouth",
        "night", "noise", "north", "novel", "nurse",
        "ocean", "order", "other", "owner", "onion",
        "piano", "pilot", "plant", "power", "price",
        "quick", "quiet", "queen", "query", "quite",
        "radio", "river", "round", "rough", "raise",
        "small", "sound", "space", "sugar", "study",
        "table", "train", "tiger", "topic", "touch",
        "uncle", "urban", "under", "union", "upper",
        "voice", "visit", "video", "value", "vivid",
        "water", "watch", "world", "write", "waste",
        "xenon", "yacht", "young", "youth", "zebra"
    ]
