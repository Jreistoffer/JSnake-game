
# score.py
import pygame  # Make sure to import pygame

class Score:
    def __init__(self, best=0):
        self.points = 0
        self.best = best

    def increase(self):
        self.points += 1

    def get_score(self):
        return self.points

    def update_best(self):
        if self.points>self.best:
            self.best = self.points

    def display(self, screen, width):
        font = pygame.font.SysFont("comicsansms", 35)
        score_text = font.render("Score: " + str(self.points), True, (255, 255, 255))  # White color
        best_text = font.render((" Best: " + str(self.best)), True, (255, 255, 255))
        screen.blit(score_text, [width / 2 - 60, 0])  # Change the position to display above the game board
        screen.blit(best_text, [width - 150,0])
