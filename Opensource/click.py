import pygame

pygame.init()

# set
size = [400, 400]
screen = pygame.display.set_mode(size)
running = True
flag_btn = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            flag_btn = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            flag_btn = True
    # display
    if flag_btn == True:
        pygame.mixer.init()
        pygame.mixer.music.load("sound/click.wav")
        pygame.mixer.music.set_volume(1)  # 1 ~ 0.1
        pygame.mixer.music.play()
        pygame.mixer.Sound("sound/click.wav")
