import pygame
from pygame.sprite import Sprite
import random

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Choose an alien type and set properties
        self.alien_type = self.choose_alien_type()
        self.set_alien_properties()

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal and vertical positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Set vertical movement direction and speed
        self.vertical_direction = 1
        self.vertical_speed = self.settings.alien_speed / 4

    def choose_alien_type(self):
        """Randomly choose an alien type."""
        return random.choice(["green", "blue", "red"])

    def set_alien_properties(self):
        """Set properties for different alien types."""
        if self.alien_type == "green":
            self.image = pygame.image.load('images/red_alien.png')
            self.speed = self.settings.alien_speed
            self.points = self.settings.green_alien_points
        elif self.alien_type == "blue":
            self.image = pygame.image.load('images/red_alien.png')
            self.speed = self.settings.alien_speed * 1.2
            self.points = self.settings.blue_alien_points
        elif self.alien_type == "red":
            self.image = pygame.image.load('images/red_alien.png')
            self.speed = self.settings.alien_speed * 1.4
            self.points = self.settings.red_alien_points

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left, and slightly up or down."""
        self.x += (self.speed * self.settings.fleet_direction)
        self.rect.x = self.x

        # Move the alien up or down slightly
        self.y += self.vertical_direction * self.vertical_speed
        self.rect.y = self.y

        # Change vertical movement direction if alien reaches a certain limit
        if self.rect.y >= self.y + self.settings.vertical_movement_limit or self.rect.y <= self.y - self.settings.vertical_movement_limit:
            self.vertical_direction *= -1
