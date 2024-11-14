import pygame 
import cv2 
import numpy as np 

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the gift box image and scale it to fit the screen
gift_box_image = pygame.image.load(r'D:\.Sana\.Books and Notes(Mine)\CODING\WISE\SHRAVAN\birthday_present.jpg')
gift_box_image = pygame.transform.scale(gift_box_image, (screen_width, screen_height))
gift_box_rect = gift_box_image.get_rect()

# Load and start playing the Happy Birthday song
pygame.mixer.music.load(r'D:\.Sana\.Books and Notes(Mine)\CODING\WISE\SHRAVAN\happy-birthday-song.mp3')
pygame.mixer.music.play(-1)  # Loop the music indefinitely

# Function to play the video
def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    clock = pygame.time.Clock()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (screen_width, screen_height))
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                return

        screen.blit(frame, (0, 0))
        pygame.display.flip()
        clock.tick(30)  # Assuming the video has 30 FPS

    cap.release()

# Main loop
running = True
video_playing = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not video_playing:
            if gift_box_rect.collidepoint(event.pos):
                video_playing = True
                play_video(r'D:\.Sana\.Books and Notes(Mine)\CODING\WISE\SHRAVAN\birthday wishes.mp4')

    if not video_playing:
        screen.fill((255, 255, 255))
        screen.blit(gift_box_image, gift_box_rect)
        pygame.display.flip()

pygame.quit()
