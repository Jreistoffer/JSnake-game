# score.py
class Score:
    def __init__(self):
        self.points = 0

    def increase(self):
        self.points += 1

    def get_score(self):
        return self.points

    def display(self, screen):
        font = pygame.font.SysFont("comicsansms", 35)
        score_text = font.render("Score: " + str(self.points), True, (255, 255, 255))  # White color
        screen.blit(score_text, [0, 0])  # Display score at the top left corner
