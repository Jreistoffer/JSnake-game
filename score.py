
# score.py
import pygame
import json
import os

BEST_SCORE_FILE = "best_score.json"

class Score:
    def __init__(self):
        self.points = 0
        self.best = self._load_best()

    def _load_best(self):
        #No file yet (first time running)
        if not os.path.exists(BEST_SCORE_FILE):
            return 0
        try:
            with open(BEST_SCORE_FILE, "r") as f:
                data = json.load(f)

            #file exist but is missing the key or has a bad value
            best = data.get("best", 0)
            if not isinstance(best, int) or best < 0:
                print("Warning: best_score.json had invalid data, resetting at 0.")
                return 0
            return best
        except(json.JSONDecodeError, ValueError):
            #file is corrupted / not valid JSON
            print("Warning: best_score.json is currupted, resetting to 0.")
            return 0

    def _save_best(self):
        try:
            with open(BEST_SCORE_FILE, "w") as f:
                json.dump({"best":self.best}, f)
        except OSError as e:
            print(f"Warning: could not save best score: {e}")

    def increase(self):
        self.points += 1

    def get_score(self):
        return self.points

    def update_best(self):
        if self.points>self.best:
            self.best = self.points
            self._save_best() #indented so it only works for when it is actually set.

    def display(self, screen, width):
        font = pygame.font.SysFont("comicsansms", 35)
        
        score_text = font.render("Score: " + str(self.points), True, (255, 255, 255))  # White color
        score_rect = score_text.get_rect(center=(width / 2, 25))
        screen.blit(score_text, score_rect)  

        
        best_text = font.render((" Best: " + str(self.best)), True, (255, 255, 255))
        best_rect = best_text.get_rect(right=width - 10, top=0)
        screen.blit(best_text, best_rect)
