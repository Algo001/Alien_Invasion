import pygame
from pygame.sprite import Sprite
import random

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.bullet_type = random.choice(["normal", "fast", "large"])
        self.set_bullet_properties()

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as decimal values.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # Make bullets curve left or right randomly
        self.curve_direction = random.choice([-1, 1])
        self.curve_speed = random.uniform(0.2, 0.8)

    def set_bullet_properties(self):
        """Set properties for different bullet types."""
        if self.bullet_type == "normal":
            self.color = self.settings.bullet_color
            self.speed = self.settings.bullet_speed
            self.width = self.settings.bullet_width
            self.height = self.settings.bullet_height
        elif self.bullet_type == "fast":
            self.color = (0, 255, 0)
            self.speed = self.settings.bullet_speed * 1.5
            self.width = self.settings.bullet_width
            self.height = self.settings.bullet_height
        elif self.bullet_type == "large":
            self.color = (255, 0, 0)
            self.speed = self.settings.bullet_speed * 0.8
            self.width = self.settings.bullet_width * 2
            self.height = self.settings.bullet_height * 2

    def update(self):
        """Move the bullet up the screen and curve left or right."""
        # Update the decimal position of the bullet.
        self.y -= self.speed
        self.x += self.curve_direction * self.curve_speed

        # Update the rect position.
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
