import random
import pygame

# Initialize Pygame and set the display dimensions
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

# Create a list of stars with random positions and sizes
stars = []
for i in range(200):
    x = random.uniform(-WIDTH/2, WIDTH/2)
    y = random.uniform(-HEIGHT/2, HEIGHT/2)
    z = random.uniform(0, WIDTH)
    radius = 3 * random.random()
    stars.append({'x': x, 'y': y, 'z': z, 'radius': radius})

# Define the function to draw the starfield
def draw_stars():
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw each star with a gradient based on its distance from the viewer
    for star in stars:
        e = star['z']
        x = star['x'] * (WIDTH / (WIDTH + e)) + WIDTH/2
        y = star['y'] * (HEIGHT / (HEIGHT + e)) + HEIGHT/2
        s = star['radius'] * (WIDTH / (WIDTH + e))
        l = max(0, (WIDTH - e) / WIDTH)
        color = (255 * l, 255 * l, 255 * l)
        pygame.draw.circle(screen, color, (x, y), s)
        star['z'] -= 3
        if star['z'] < 1:
            star['z'] = WIDTH

