# def greet_me(name):
#    print(f"Hello {name}! This is a greeting from the greet_me function.")
# greet_me("Muhammad Affan")
# def greet_me(name):
#     print("Hello world!")
# greet_me("Muhammad Affan")
# def add_numbers(a, b):
#     return a + b
# result = add_numbers(5, 3)
# print("The sum is:", result)
# import os

# folder_name = "MyStufl;;l;"
# os.mkdir(folder_name)
# print(f"Folder {folder_name} created successfully.")
# currest_directory = os.getcwd()
# print("Current Directory:", currest_directory)
# import math
# number = 16
# square_root = math.sqrt(number)
# print(f"The square root of {number} is {square_root}.")
# area = math.pi * (number ** 2)
# print(f"The area of the circle with radius {number} is {area}.")
# name = "Muhammad Affan"
# while name =="Muhammad Affan":
#     print("Hello, Muhammad Affan!")
# numbers = [1, 2, 3, 4, 5]
# numbers.pop(2)  # Remove the element at index 2 (which is 3)
# print(numbers)  # Output: [1, 2, 4, 5]
# # Remove the element at index 2 and store it in a variable
# removed_item = numbers.pop(2)  # removed_item = 3

# # Insert the removed item back at the original index (2)
# numbers.insert(2, removed_item)

# print(numbers)  # Output: [1, 2, 3, 4, 5]
# file  = open("test.txt", "w")
# file.write("Hello, world!")
# file.close()

# file = open("test.txt", "r")
# content = file.read()
# print(content)
# file.close()

# try:
#     file = open("test.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found. Please check the file path.")
# ...existing code...

# print("\nWelcome to the Minecraft AI! Ask me anything about Minecraft.")

# question = input("What would you like to know? ").lower()

# if "diamond" in question:
#     print("Diamonds are most commonly found at Y-level -59 in the Deep Slate layer (between -64 and 16).")
# elif "nether" in question:
#     print("The Nether is a dangerous dimension with lava, unique mobs, and resources like Nether Quartz and Ancient Debris.")
# elif "end" in question:
#     print("The End is where you fight the Ender Dragon and find End Cities with Elytra.")
# elif "villager" in question:
#     print("Villagers are NPCs that live in villages and can trade items with you.")
# elif "creeper" in question:
#     print("Creepers are silent mobs that explode when close to the player.")
# elif "redstone" in question:
#     print("Redstone is used to create circuits and mechanisms, like doors and traps.")
# elif "iron" in question:
#     print("Iron ore is found between Y-levels -64 and 320, with peaks at Y=15 and Y=232.")
# else:
#     print("Sorry, I don't know the answer to that. Try asking something else about Minecraft!")
# import random
# import time
# import os

# # Characters to use in the Matrix effect
# chars = "0123456789abcdef"

# # Terminal size
# width = os.get_terminal_size().columns
# height = os.get_terminal_size().lines

# # Initial column positions
# columns = [random.randint(0, width - 1) for _ in range(width // 2)]

# while True:
#     os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
#     for i in range(height):
#         line = ""
#         for col in columns:
#             if random.randint(0, 4) == 0:  # Random chance to print character
#                 line += random.choice(chars) + " "
#             else:
#                 line += "  "
#         print(line.center(width))  # Print centered
#     columns = [col if random.randint(0, 6) else random.randint(0, width - 1) for col in columns]
#     time.sleep(0.05)  # Speed of animation
# !/usr/bin/env python3
# import time
# import random
# import sys
# from colorama import Fore, Style, init

# # Initialize colorama for cross-platform colored text
# init(autoreset=True)

# class CyberHacker:
#     def __init__(self):
#         self.target = "CRYPT0-C0R3"
#         self.codes = ["OVERRIDE-9X", "PHANTOM-PROTOCOL", "NIGHTMARE-ROOT", "VENOM-BYPASS"]
#         self.status = ["> BACKDOOR ACTIVE", "> FIREWALL CRACKED", "> ENCRYPTION BROKEN", "> MAINFRAME ACCESSED"]
#         self.weapons = ["NEURAL-DISRUPTOR", "QUANTUM DECRYPTOR", "THERMAL-INJECTOR", "ZERO-DAY EXPLOIT"]
#         self.colors = [Fore.RED, Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.MAGENTA]
    
#     def _typewriter(self, text, speed=0.05, color=Fore.WHITE):
#         """Badass typewriter effect with random color bursts"""
#         for char in text:
#             sys.stdout.write(color + char + Style.RESET_ALL)
#             sys.stdout.flush()
#             if random.random() < 0.1:  # Random color burst
#                 sys.stdout.write(random.choice(self.colors) + '|' + Style.RESET_ALL)
#                 time.sleep(0.1)
#                 sys.stdout.write('\b')
#             time.sleep(speed)
#         print()
    
#     def _matrix_rain(self, duration=3):
#         """Simulate Matrix-style code rain"""
#         chars = "01!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
#         start_time = time.time()
        
#         while time.time() - start_time < duration:
#             line = ''.join(random.choice(chars) for _ in range(80))
#             print(random.choice(self.colors) + line + Style.RESET_ALL, end='\r')
#             time.sleep(0.1)
#         print(' ' * 80, end='\r')
    
#     def _display_cyber_skull(self):
#         """Show a badass cyber skull ASCII art"""
#         skull = [
#             "    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄",
#             "   █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█",
#             "  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█",
#             " █▓▓▓▓▓▀▀▀█▓▓▓▓▓▓▀▀▀█▓▓█",
#             "█▓▓▓▓▓▌   ▐▓▓▓▓▓▌   ▐▓▓▓█",
#             "█▓▓▓▓▓     ▓▓▓▓▓     ▓▓▓█",
#             "█▓▓▓▓▓▄▄▄▄▓▓▓▓▓▄▄▄▄▓▓▓▓█",
#             " █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█",
#             "  █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█",
#             "   ███████████████████"
#         ]
#         print(Fore.GREEN)
#         for line in skull:
#             print(line)
#         print(Style.RESET_ALL)
    
#     def breach_system(self):
#         """Main hacking sequence - pure digital mayhem"""
#         try:
#             # Initialization sequence
#             self._matrix_rain(2)
#             self._typewriter(f"INITIALIZING CYBER WARFARE SUITE...", 0.03, Fore.RED)
#             time.sleep(1)
            
#             # Target acquisition
#             self._typewriter(f"LOCKING TARGET: {self.target}", 0.04, Fore.CYAN)
#             self._matrix_rain(1.5)
            
#             # Weapon selection
#             weapon = random.choice(self.weapons)
#             self._typewriter(f"DEPLOYING: {weapon}", 0.03, Fore.YELLOW)
#             time.sleep(1)
            
#             # Breach sequence
#             print("\n" + "-"*60)
#             self._display_cyber_skull()
#             print(f"{Fore.MAGENTA}> > > TARGET PENETRATED: {self.target} < < <{Style.RESET_ALL}")
#             print("-"*60 + "\n")
            
#             # Access codes
#             for i, code in enumerate(self.codes):
#                 time.sleep(0.7)
#                 self._typewriter(f"INJECTING CODE: {code}", 0.03, self.colors[i % len(self.colors)])
#                 self._typewriter(f"STATUS: {self.status[i]}", 0.01, Fore.GREEN)
#                 if i < len(self.codes) - 1:
#                     self._matrix_rain(0.7)
            
#             # Final takeover
#             time.sleep(1)
#             print("\n")
#             self._typewriter(f"! ! ! {self.target} SYSTEM OWNED ! ! !", 0.05, Fore.RED)
#             self._typewriter("ALL ENCRYPTED DATA DUMPED TO SHADOW DRIVE", 0.03, Fore.CYAN)
#             self._typewriter("COVERING DIGITAL FOOTPRINTS...", 0.04, Fore.YELLOW)
#             time.sleep(1)
#             self._typewriter("MISSION COMPROMISED: ZERO", 0.02, Fore.GREEN)
            
#         except KeyboardInterrupt:
#             self._typewriter("\nABORT MISSION: CYBER GHOST PROTOCOL ACTIVATED", 0.03, Fore.RED)
#             sys.exit(0)

# if __name__ == "__main__":
#     hacker = CyberHacker()
#     hacker.breach_system()
# import asyncio
# import platform
# import pygame
# import numpy as np
# from numba import njit, prange
# import colorsys

# # Constants
# WIDTH = 800
# HEIGHT = 600
# MAX_ITER = 100
# FPS = 120

# # Numba-accelerated Mandelbrot calculation
# @njit
# def mandelbrot(real, imag, max_iter):
#     c_real = real
#     c_imag = imag
#     z_real = 0.0
#     z_imag = 0.0
#     for n in range(max_iter):
#         z_real2 = z_real * z_real
#         z_imag2 = z_imag * z_imag
#         if z_real2 + z_imag2 > 4.0:
#             return n
#         z_imag = 2 * z_real * z_imag + c_imag
#         z_real = z_real2 - z_imag2 + c_real
#     return max_iter

# @njit(parallel=True)
# def generate_mandelbrot(width, height, real_min, real_max, imag_min, imag_max, max_iter):
#     mandelbrot_set = np.empty((height, width), dtype=np.uint8)
#     for i in prange(height):
#         imag = imag_min + (imag_max - imag_min) * i / height
#         for j in range(width):
#             real = real_min + (real_max - real_min) * j / width
#             mandelbrot_set[i, j] = mandelbrot(real, imag, max_iter)
#     return mandelbrot_set

# # Color mapping
# def iteration_to_color(iteration, max_iter):
#     if iteration == max_iter:
#         return (0, 0, 0)  # Black for points in the set
#     else:
#         hue = iteration / max_iter * 360
#         r, g, b = colorsys.hsv_to_rgb(hue / 360, 1.0, 1.0)
#         return (int(r * 255), int(g * 255), int(b * 255))

# def create_color_array(mandelbrot_set, max_iter):
#     color_map = np.array([iteration_to_color(i, max_iter) for i in range(max_iter + 1)], dtype=np.uint8)
#     return color_map[mandelbrot_set]

# # Game state
# screen = None
# real_min = -2.0
# real_max = 1.0
# imag_min = -1.6
# imag_max = 1.5
# dragging = False
# view_changed = True
# surface = None
# start_pos = None
# current_pos = None

# def setup():
#     global screen
#     pygame.init()
#     screen = pygame.display.set_mode((WIDTH, HEIGHT))
#     pygame.display.set_caption("Mandelbrot Set Explorer")

# async def update_loop():
#     global real_min, real_max, imag_min, imag_max, dragging, view_changed, surface, start_pos, current_pos

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             return False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:  # Left click
#                 dragging = True
#                 start_pos = event.pos
#         elif event.type == pygame.MOUSEMOTION:
#             if dragging:
#                 current_pos = event.pos
#         elif event.type == pygame.MOUSEBUTTONUP:
#             if event.button == 1 and dragging:
#                 end_pos = event.pos
#                 x1, y1 = start_pos
#                 x2, y2 = end_pos
#                 if x1 > x2:
#                     x1, x2 = x2, x1
#                 if y1 > y2:
#                     y1, y2 = y2, y1
#                 real_selected_min = real_min + (x1 / WIDTH) * (real_max - real_min)
#                 real_selected_max = real_min + (x2 / WIDTH) * (real_max - real_min)
#                 imag_selected_min = imag_min + (y1 / HEIGHT) * (imag_max - imag_min)
#                 imag_selected_max = imag_min + (y2 / HEIGHT) * (imag_max - imag_min)
#                 real_min, real_max = real_selected_min, real_selected_max
#                 imag_min, imag_max = imag_selected_min, imag_selected_max
#                 view_changed = True
#                 dragging = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 shift = 0.1 * (real_max - real_min)
#                 real_min -= shift
#                 real_max -= shift
#                 view_changed = True
#             elif event.key == pygame.K_RIGHT:
#                 shift = 0.1 * (real_max - real_min)
#                 real_min += shift
#                 real_max += shift
#                 view_changed = True
#             elif event.key == pygame.K_UP:
#                 shift = 0.1 * (imag_max - imag_min)
#                 imag_min -= shift
#                 imag_max -= shift
#                 view_changed = True
#             elif event.key == pygame.K_DOWN:
#                 shift = 0.1 * (imag_max - imag_min)
#                 imag_min += shift
#                 imag_max += shift
#                 view_changed = True
#             elif event.key in (pygame.K_PLUS, pygame.K_EQUALS):
#                 center_real = (real_min + real_max) / 2
#                 center_imag = (imag_min + imag_max) / 2
#                 width = (real_max - real_min) / 1.5
#                 height = (imag_max - imag_min) / 1.5
#                 real_min = center_real - width / 2
#                 real_max = center_real + width / 2
#                 imag_min = center_imag - height / 2
#                 imag_max = center_imag + height / 2
#                 view_changed = True
#             elif event.key == pygame.K_MINUS:
#                 center_real = (real_min + real_max) / 2
#                 center_imag = (imag_min + imag_max) / 2
#                 width = (real_max - real_min) * 1.5
#                 height = (imag_max - imag_min) * 1.5
#                 real_min = center_real - width / 2
#                 real_max = center_real + width / 2
#                 imag_min = center_imag - height / 2
#                 imag_max = center_imag + height / 2
#                 view_changed = True
#             elif event.key == pygame.K_r:
#                 real_min, real_max = -2.0, 1.0
#                 imag_min, imag_max = -1.5, 1.5
#                 view_changed = True

#     if view_changed:
#         mandelbrot_set = generate_mandelbrot(WIDTH, HEIGHT, real_min, real_max, imag_min, imag_max, MAX_ITER)
#         color_array = create_color_array(mandelbrot_set, MAX_ITER)
#         color_array_transposed = np.transpose(color_array, (1, 0, 2))
#         surface = pygame.surfarray.make_surface(color_array_transposed)
#         view_changed = False

#     if surface is not None:
#         screen.blit(surface, (0, 0))

#     if dragging and current_pos:
#         rect = pygame.Rect(start_pos[0], start_pos[1], current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
#         pygame.draw.rect(screen, (255, 255, 255), rect, 1)

#     pygame.display.flip()
#     return True

# async def main():
#     setup()
#     running = True
#     while running:
#         running = await update_loop()
#         await asyncio.sleep(1.0 / FPS)

# if platform.system() == "Emscripten":
#     asyncio.ensure_future(main())
# else:
#     if __name__ == "__main__":
#         asyncio.run(main())
import pygame
import random
import math
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Get screen dimensions
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Broken Screen Prank")
pygame.mouse.set_visible(False)  # Hide the mouse cursor

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (30, 30, 30)
LIGHT_GRAY = (180, 180, 180)

# Generate crack lines
def generate_cracks():
    cracks = []
    # Create main impact point
    impact_x = SCREEN_WIDTH // 2 + random.randint(-100, 100)
    impact_y = SCREEN_HEIGHT // 2 + random.randint(-100, 100)
    
    # Create radial cracks from impact point
    for _ in range(8):
        angle = random.uniform(0, 2 * math.pi)
        length = random.randint(300, 500)
        segments = []
        segments.append((impact_x, impact_y))
        
        x, y = impact_x, impact_y
        for _ in range(random.randint(10, 20)):
            # Add some randomness to the crack path
            angle += random.uniform(-0.4, 0.4)
            segment_length = random.randint(10, 50)
            x += math.cos(angle) * segment_length
            y += math.sin(angle) * segment_length
            segments.append((x, y))
        cracks.append(segments)
    
    # Create additional random cracks
    for _ in range(15):
        start_x = random.randint(0, SCREEN_WIDTH)
        start_y = random.randint(0, SCREEN_HEIGHT)
        segments = []
        segments.append((start_x, start_y))
        
        x, y = start_x, start_y
        for _ in range(random.randint(5, 15)):
            angle = random.uniform(0, 2 * math.pi)
            segment_length = random.randint(10, 40)
            x += math.cos(angle) * segment_length
            y += math.sin(angle) * segment_length
            segments.append((x, y))
        cracks.append(segments)
    
    return cracks

# Generate shattered glass pieces
def generate_glass_pieces():
    pieces = []
    grid_size = 40
    offset_range = 3
    
    for y in range(0, SCREEN_HEIGHT, grid_size):
        for x in range(0, SCREEN_WIDTH, grid_size):
            # Create a slight offset to make the glass look shattered
            offset_x = random.randint(-offset_range, offset_range)
            offset_y = random.randint(-offset_range, offset_range)
            pieces.append((x + offset_x, y + offset_y, 
                           x + grid_size + offset_x, y + offset_y,
                           x + grid_size + offset_x, y + grid_size + offset_y,
                           x + offset_x, y + grid_size + offset_y))
    return pieces

# Generate the cracked glass effect
crack_lines = generate_cracks()
glass_pieces = generate_glass_pieces()

# Create a surface for the glass effect
glass_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    
    # Get mouse position for parallax effect
    mouse_x, mouse_y = pygame.mouse.get_pos()
    parallax_x = (mouse_x - SCREEN_WIDTH // 2) / 100
    parallax_y = (mouse_y - SCREEN_HEIGHT // 2) / 100
    
    # Fill the background with a dark color to simulate a powered-off screen
    screen.fill(DARK_GRAY)
    
    # Draw glass pieces with parallax effect
    for piece in glass_pieces:
        # Apply parallax effect to each vertex
        piece_vertices = [
            (piece[0] + parallax_x, piece[1] + parallax_y),
            (piece[2] + parallax_x, piece[3] + parallax_y),
            (piece[4] + parallax_x, piece[5] + parallax_y),
            (piece[6] + parallax_x, piece[7] + parallax_y)
        ]
        pygame.draw.polygon(screen, LIGHT_GRAY, piece_vertices, 0)
        pygame.draw.polygon(screen, BLACK, piece_vertices, 1)
    
    # Draw crack lines with parallax effect
    for crack in crack_lines:
        adjusted_crack = []
        for point in crack:
            adjusted_x = point[0] + parallax_x
            adjusted_y = point[1] + parallax_y
            adjusted_crack.append((adjusted_x, adjusted_y))
        pygame.draw.lines(screen, BLACK, False, adjusted_crack, 2)
    
    # Draw impact point
    impact_x = SCREEN_WIDTH // 2 + parallax_x
    impact_y = SCREEN_HEIGHT // 2 + parallax_y
    pygame.draw.circle(screen, BLACK, (int(impact_x), int(impact_y)), 20)
    pygame.draw.circle(screen, DARK_GRAY, (int(impact_x), int(impact_y)), 15)
    
    # Draw some random white pixels to simulate broken pixels
    for _ in range(20):
        x = random.randint(0, SCREEN_WIDTH - 1)
        y = random.randint(0, SCREEN_HEIGHT - 1)
        screen.set_at((x, y), WHITE)
    
    # Draw fake reflection
    pygame.draw.ellipse(screen, (100, 100, 100, 150), 
                       (SCREEN_WIDTH - 200 + parallax_x, 100 + parallax_y, 100, 50), 3)
    
    # Draw exit instructions (hidden in corner)
    font = pygame.font.SysFont(None, 24)
    text = font.render("Press ESC to exit", True, (100, 100, 100))
    screen.blit(text, (10, SCREEN_HEIGHT - 30))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()