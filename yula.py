import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle dimensions
paddle_width = 10
paddle_height = 100

# Ball dimensions
ball_size = 10

# Paddle positions
player_x = 50
player_y = (screen_height - paddle_height) // 2
opponent_x = screen_width - 50 - paddle_width
opponent_y = (screen_height - paddle_height) // 2

# Ball position and speed
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_x_change = 3.0 * random.choice((1, -1))  # Increase ball speed
ball_y_change = 3.0 * random.choice((1, -1))  # Increase ball speed

# Player and opponent speed
player_speed = 0
opponent_speed = 2.0  # Increase opponent speed

# Score
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 74)

def show_score():
    player_text = font.render(str(player_score), True, white)
    screen.blit(player_text, (screen_width // 4, 10))
    opponent_text = font.render(str(opponent_score), True, white)
    screen.blit(opponent_text, (screen_width * 3 // 4, 10))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -3.0  # Increase player speed
            if event.key == pygame.K_DOWN:
                player_speed = 3.0  # Increase player speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0
    
    # Move player paddle
    player_y += player_speed
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - paddle_height:
        player_y = screen_height - paddle_height

    # Move opponent paddle
    if opponent_y + paddle_height / 2 < ball_y:
        opponent_y += opponent_speed
    else:
        opponent_y -= opponent_speed
    
    if opponent_y < 0:
        opponent_y = 0
    if opponent_y > screen_height - paddle_height:
        opponent_y = screen_height - paddle_height

    # Move ball
    ball_x += ball_x_change
    ball_y += ball_y_change

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_y_change *= -1

    # Ball collision with paddles
    if (player_x < ball_x < player_x + paddle_width and
        player_y < ball_y < player_y + paddle_height) or (
        opponent_x < ball_x < opponent_x + paddle_width and
        opponent_y < ball_y < opponent_y + paddle_height):
        ball_x_change *= -1
    
    # Ball out of bounds
    if ball_x <= 0:
        opponent_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_x_change *= random.choice((1, -1))
        ball_y_change *= random.choice((1, -1))
    
    if ball_x >= screen_width - ball_size:
        player_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_x_change *= random.choice((1, -1))
        ball_y_change *= random.choice((1, -1))
    
    # Fill screen with black color
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, (player_x, player_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (opponent_x, opponent_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Show score
    show_score()
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()



""" class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage

def main_game():
    player_name = input("Enter your name: ")
    player = Player(player_name)

    print(f"Welcome, {player.name}! You find yourself in a mysterious dungeon.")

    while player.health > 0:
        action = input("What do you want to do? (explore/fight/rest/quit): ").lower()

        if action == "quit":
            print("Game Over. Thanks for playing!")
            break
        elif action == "explore":
            print("You find a treasure chest!")
            player.inventory.append("Treasure")
        elif action == "fight":
            enemy_health = 50
            while enemy_health > 0 and player.health > 0:
                attack = input("Attack the enemy? (yes/no): ").lower()
                if attack == "yes":
                    enemy_health -= 20
                    print(f"You attacked the enemy! Enemy health: {enemy_health}")
                    player.take_damage(10)
                    print(f"Enemy attacks! Player health: {player.health}")
                elif attack == "no":
                    print("You decide not to attack.")
            if enemy_health <= 0:
                print("You defeated the enemy!")
        elif action == "rest":
            player.health += 20
            print("You rest and recover some health.")
            if player.health > 100:
                player.health = 100
            print(f"Player health: {player.health}")
        else:
            print("Invalid command. Try again.")

# Start the game
main_game()
 """
""" import requests
from bs4 import BeautifulSoup

url = 'https://www.geeksforgeeks.org/'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Create an HTML file and write the links to it
with open('output.html', 'w') as file:
    file.write('<html><head><title>Links</title></head><body>')
    file.write('<h1>Links on the page</h1>')
    file.write('<ul>')

    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            file.write(f'<li><a href="{href}">{href}</a></li>')

    file.write('</ul>')
    file.write('</body></html>')
 """