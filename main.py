import pygame
import sys
from button import Button
import random
import json
import time

# Funktion zum speichern der Optionen
def save_options(options):
    with open('options.json', 'w') as file:
        json.dump(options, file)
# Funktion zum Speicher und beenden des Spieles
def quit_game():
    save_options(options)
    pygame.quit()
    sys.exit()
# Funktion zum Aufrufen der Optionen
def load_options():
    with open('options.json', 'r') as file:
        options = json.load(file)
    return options
# Funktion zum laden der Schrift
def get_font(size):
    return pygame.font.Font('assets\\font.ttf', size)
# Countdown
def counter(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        
        SCREEN.fill(BLACK)
        
        displaytimer = get_font(40).render(timeformat, True, WHITE)
        texttimer = displaytimer
        texttimer_rect = texttimer.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        SCREEN.blit(texttimer, texttimer_rect)
        pygame.display.flip()
        #print(timeformat, end='/r')
        time.sleep(1)
        t -= 1
# Funktion zu Spielen
def save_score(ballchanges):
    HIGHSCOREVAR_EASY = options['HIGHSCOREVAR_EASY']
    HIGHSCOREVAR_MID = options['HIGHSCOREVAR_MID']
    HIGHSCOREVAR_HARD = options['HIGHSCOREVAR_HARD']
    
    if difficulty == "EASY":
        if ballchanges > HIGHSCOREVAR_EASY:
            HIGHSCOREVAR_EASY = ballchanges
            options['HIGHSCOREVAR_EASY'] = HIGHSCOREVAR_EASY
            return HIGHSCOREVAR_EASY
        elif ballchanges < HIGHSCOREVAR_EASY:
            pass
    if difficulty == "MID":
        if ballchanges > HIGHSCOREVAR_MID:
            HIGHSCOREVAR_MID = ballchanges
            options['HIGHSCOREVAR_MID'] = HIGHSCOREVAR_MID
            return HIGHSCOREVAR_MID
        elif ballchanges < HIGHSCOREVAR_MID:
            pass
    if difficulty == "HARD":
        if ballchanges > HIGHSCOREVAR_HARD:
            HIGHSCOREVAR_HARD = ballchanges
            options['HIGHSCOREVAR_HARD'] = HIGHSCOREVAR_HARD
            return HIGHSCOREVAR_HARD
        elif ballchanges < HIGHSCOREVAR_HARD:
            pass

def play():
    global ballchanges
    # options = load_options()
    t = options["COUNTDOWN"]
    counter(t)
    # Caption oben links
    pygame.display.set_caption("Ping Pong!")
    # Definieren der Variablen
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    SCALE_FACTOR_X = SCREEN_WIDTH / 640
    SCALE_FACTOR_Y = SCREEN_HEIGHT / 480

    ball_diameter = int(20 * SCALE_FACTOR_X)
    ballpos_x = 1280 / 2
    ballpos_y = 720 / 2

    player_1_x = 20#int(20 * SCALE_FACTOR_X) #40
    player_1_y = 300 #int(20 * SCALE_FACTOR_Y) #30
    player_1_movement = 0

    player_2_x = 1220#int(SCREEN_WIDTH - (2 * 20 * SCALE_FACTOR_X))
    player_2_y = 300#int(20 * SCALE_FACTOR_Y)
    player_2_movement = 0
    # Umschreiben der Variablen
    if difficulty == "EASY":
        movement_x = options['EASY']['movement_x']
        movement_y = options['EASY']['movement_y']
        racket_height = options['EASY']['racket_height']
        movement_racket = options['EASY']['movement_racket']
        movement_racket = options['EASY']['movement_racket']
        t = options['COUNTDOWN']
    
    elif difficulty == "MID":
        movement_x = options['MID']['movement_x']
        movement_y = options['MID']['movement_y']
        racket_height = options['MID']['racket_height']
        movement_racket = options['MID']['movement_racket']
        movement_racket = options['MID']['movement_racket']
        t = options['COUNTDOWN']
    
    elif difficulty == "HARD":
        movement_x = options['HARD']['movement_x']
        movement_y = options['HARD']['movement_y']
        racket_height = options['HARD']['racket_height']
        movement_racket = options['HARD']['movement_racket']
        movement_racket = options['HARD']['movement_racket']
        t = options['COUNTDOWN']
    play_sounds = options['play_sounds']
    HIGHSCOREVAR_EASY = options['HIGHSCOREVAR_EASY']
    HIGHSCOREVAR_MID = options['HIGHSCOREVAR_MID']
    HIGHSCOREVAR_HARD = options['HIGHSCOREVAR_HARD']
    ballchanges = 0  
    
    if play_sounds == True:
        play_ping_or_pong = True
    elif play_sounds == False:
        play_ping_or_pong = False
    
    GAME = 1
    COUNTER = 1
    gamestate = GAME
    # Random Zahl zum definieren der Startrichtung des balles
    one_or2 = random.randint(1, 4)
    # Event Listener
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(ballchanges)
                quit_game()
            # Wenn GAME:
            if gamestate == GAME:

                if event.type == pygame.KEYDOWN:  # Taste gedrückt

                    if event.key == pygame.K_w:
                        player_1_movement = -movement_racket
                    elif event.key == pygame.K_s:
                        player_1_movement = movement_racket
                    elif event.key == pygame.K_UP:
                        player_2_movement = -movement_racket
                    elif event.key == pygame.K_DOWN:
                        player_2_movement = movement_racket
                    elif event.key == pygame.K_ESCAPE:
                        save_score(ballchanges)
                        main_menu()

                if event.type == pygame.KEYUP:  # Taste losgelassen
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        player_1_movement = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_2_movement = 0

        # Spiellogik
        # -- Schläger 1 bewegen
        if player_1_movement != 0: 
            player_1_y += player_1_movement
        # -- Fenster begrenzen
        if player_1_y < int(10 * SCALE_FACTOR_Y):
            player_1_y = int(10 * SCALE_FACTOR_Y)
        if player_1_y > SCREEN_HEIGHT - racket_height - (10 * SCALE_FACTOR_Y):
            player_1_y = int(SCREEN_HEIGHT - racket_height - (10 * SCALE_FACTOR_Y))
        
        # -- Schläger 2 bewegen
        if player_2_movement != 0:
            player_2_y += player_2_movement
        # -- Fenster begrenzen
        if player_2_y < int(10 * SCALE_FACTOR_Y):
            player_2_y = int(10 * SCALE_FACTOR_Y)
        if player_2_y > SCREEN_HEIGHT - racket_height - (10 * SCALE_FACTOR_Y):
            player_2_y = int(SCREEN_HEIGHT - racket_height - (10 * SCALE_FACTOR_Y))
        # Spielfeld löschen
        SCREEN.fill(BLACK)
        #SCREEN.blit(BG, (0, 0))
        # Spielfeld zeichnen
        # -- Ball
        ball = pygame.draw.ellipse(SCREEN, WHITE, [ballpos_x, ballpos_y, ball_diameter, ball_diameter])
        # -- Schläger 1
        player1 = pygame.draw.rect(SCREEN, WHITE,
                                             [player_1_x, player_1_y, 20, racket_height])
        # -- Schläger 2
        player2 = pygame.draw.rect(SCREEN, WHITE,
                                           [player_2_x, player_2_y, 20, racket_height])
        # -- Mittellinie
        middle = pygame.draw.line(SCREEN, WHITE, [SCREEN_WIDTH/2, SCREEN_HEIGHT], [SCREEN_WIDTH/2, 0])



        # Bewegen unseres Kreises
        if one_or2 == 1:
            ballpos_x += movement_x
            ballpos_y += movement_y
        elif one_or2 == 2:
            ballpos_x -= movement_x
            ballpos_y -= movement_y
        elif one_or2 == 3:
            ballpos_x += movement_x
            ballpos_y -= movement_y
        elif one_or2 == 4:
            ballpos_x -= movement_x
            ballpos_y += movement_y

        if ballpos_y > SCREEN_HEIGHT - ball_diameter or ballpos_y < 0:
            movement_y = -movement_y
            if random_sound == 1 and play_ping_or_pong == True:
                ping = pygame.mixer.Sound('assets\ping1.mp3')
                pygame.mixer.Sound(ping).play(0, 0)

        if ballpos_x > SCREEN_WIDTH - ball_diameter:
            save_score(ballchanges)
            # Spiel beenden und zum Menü zurückkehren
            main_menu()
        elif ballpos_x < 0:
            save_score(ballchanges)
            # Spiel beenden und zum Menü zurückkehren
            main_menu()
            
        # Kollidieren
        if player1.colliderect(ball):
            movement_x = movement_x * -1
            ballchanges += 1
            ballpos_x = player_1_x + int(20 * SCALE_FACTOR_X)
            if random_sound == 1 and play_ping_or_pong == True:
                ping = pygame.mixer.Sound('assets\ping1.mp3')
                pygame.mixer.Sound(ping).play(0, 0)
                #pygame.mixer.music.set_volume(.3)
            elif random_sound == 2 and play_ping_or_pong == True:
                pong = pygame.mixer.Sound('assets\pong2.mp3')
                pygame.mixer.Sound(pong).play(0, 0)
                #pygame.mixer.Sound.set_volume(.3)
            else:
                pass
        if player2.colliderect(ball):
            movement_x = movement_x * -1
            ballchanges += 1
            ballpos_x = player_2_x - ball_diameter
            if random_sound == 1 and play_ping_or_pong == True:
                pygame.mixer.music.load('assets\ping1.mp3')
                pygame.mixer.music.play(0,0.0)
                pygame.mixer.music.set_volume(1)
                
            elif random_sound == 2 and play_ping_or_pong == True:
                pygame.mixer.music.load('assets\pong2.mp3')
                pygame.mixer.music.play(0,0.0)
                pygame.mixer.music.set_volume(1)
                
            else:
                pass
        # Score Anzeige
        displaytext = get_font(40).render(f"SCORE {str(ballchanges)}", True, WHITE)
        text = displaytext
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, 80))
        SCREEN.blit(text, text_rect)

        pygame.display.flip()
        # Aktualisierung
        pygame.time.Clock().tick(180)               
# Funktion für das Optionsmenu
def option_menu():
    # options = load_options()
    global difficulty, difficulty_disp, play_sounds, HIGHSCOREVAR_EASY,HIGHSCOREVAR_MID,HIGHSCOREVAR_HARD
    # Text
    #print("Main_Menu_play_sound: " + str(play_sounds))
    pygame.display.set_caption("⚙️ Options ⚙️")
    SCREEN.blit(BG, (0, 0))
    OPTIONS_TEXT = get_font(45).render("Difficulty:", True, WHITE)
    OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT) / 2 * 0.3))
    SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
    #print(options['play_sounds'])
    play_sounds = options['play_sounds']
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        # Zurück Button
        OPTIONS_BACK = Button(image=None, pos=(640, 600),
                               text_input="BACK", font=get_font(75), base_color=WHITE, hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        if play_sounds == True:
            sounds_button = Button(image=None, pos=(1100, 600), 
                                text_input="Sound", font=get_font(35), base_color=GREEN, hovering_color=RED)
            sounds_button.changeColor(OPTIONS_MOUSE_POS)
            sounds_button.update(SCREEN)
        elif play_sounds == False:
            sounds_button = Button(image=None, pos=(1100, 600), 
                                text_input="Sound", font=get_font(35), base_color=RED, hovering_color=GREEN)
            sounds_button.changeColor(OPTIONS_MOUSE_POS)
            sounds_button.update(SCREEN)
        # Knöpfe mit Farbe
        if difficulty == "EASY":
            EASY = Button(image=None, pos=(300, SCREEN_HEIGHT / 2),
                            text_input="Easy", font=get_font(35), base_color="Green", hovering_color="Green")
                
            EASY.changeColor(OPTIONS_MOUSE_POS)
            EASY.update(SCREEN)

            MID = Button(image=None, pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                      text_input="Normal", font=get_font(35), base_color=WHITE, hovering_color=BLUE)
        
            MID.changeColor(OPTIONS_MOUSE_POS)
            MID.update(SCREEN)

            HARD = Button(image=None, pos=(960, SCREEN_HEIGHT / 2),
                      text_input="Hard", font=get_font(35), base_color=WHITE, hovering_color=RED)
        
            HARD.changeColor(OPTIONS_MOUSE_POS)
            HARD.update(SCREEN)
        elif difficulty == "MID":
            EASY = Button(image=None, pos=(300, SCREEN_HEIGHT / 2),
                      text_input="Easy", font=get_font(35), base_color=WHITE, hovering_color="Green")
        
            EASY.changeColor(OPTIONS_MOUSE_POS)
            EASY.update(SCREEN)

            MID = Button(image=None, pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                      text_input="Normal", font=get_font(35), base_color=BLUE, hovering_color=BLUE)
        
            MID.changeColor(OPTIONS_MOUSE_POS)
            MID.update(SCREEN)

            HARD = Button(image=None, pos=(960, SCREEN_HEIGHT / 2),
                      text_input="Hard", font=get_font(35), base_color=WHITE, hovering_color=RED)
        
            HARD.changeColor(OPTIONS_MOUSE_POS)
            HARD.update(SCREEN)
        elif difficulty == "HARD":

            EASY = Button(image=None, pos=(300, SCREEN_HEIGHT / 2),
                      text_input="Easy", font=get_font(35), base_color=WHITE, hovering_color="Green")
        
            EASY.changeColor(OPTIONS_MOUSE_POS)
            EASY.update(SCREEN)

            MID = Button(image=None, pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
                      text_input="Normal", font=get_font(35), base_color=WHITE, hovering_color=BLUE)
        
            MID.changeColor(OPTIONS_MOUSE_POS)
            MID.update(SCREEN)
            HARD = Button(image=None, pos=(960, SCREEN_HEIGHT / 2),
                      text_input="Hard", font=get_font(35), base_color=RED, hovering_color=RED)
        
            HARD.changeColor(OPTIONS_MOUSE_POS)
            HARD.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if EASY.checkForInput(OPTIONS_MOUSE_POS):
                    
                    difficulty = "EASY"
                    difficulty_disp = "Easy"
                    options['difficulty'] = "EASY"
                    #main_menu()
                if MID.checkForInput(OPTIONS_MOUSE_POS):
                    
                    difficulty = "MID"
                    difficulty_disp = "Normal"
                    options['difficulty'] = "MID"
                    #main_menu()
                if HARD.checkForInput(OPTIONS_MOUSE_POS):
                    
                    difficulty = "HARD"
                    difficulty_disp = "Hard"
                    options['difficulty'] = "HARD"
                    #main_menu()
                if sounds_button.checkForInput(OPTIONS_MOUSE_POS):

                    play_sounds = not play_sounds
                    options['play_sounds'] = play_sounds
                        
                    #print("Button_clicked: " + str(play_sounds))

        pygame.display.update()
# Funktion für das Hauptmenu
def main_menu():
    HIGHSCOREVAR_EASY = options['HIGHSCOREVAR_EASY']
    HIGHSCOREVAR_MID = options['HIGHSCOREVAR_MID']
    HIGHSCOREVAR_HARD = options['HIGHSCOREVAR_HARD']
    #print(HIGHSCOREVAR)

    if difficulty == "EASY":
        difficulty_disp = "Easy"
    if difficulty == "MID":
        difficulty_disp = "Normal"
    if difficulty == "HARD":
        difficulty_disp = "Hard"

    while True:
        
        SCREEN.blit(BG, (0, 0))
        pygame.display.set_caption("Main Menu")
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


        DIFFICULTY_TEXT = get_font(25).render(f"Mode: {difficulty_disp}", True, "#b68f40")
        DIFFICULTY_RECT = DIFFICULTY_TEXT.get_rect(center=(200, 680))
        SCREEN.blit(DIFFICULTY_TEXT, DIFFICULTY_RECT)

        
        if difficulty == "EASY":
            HIGHSCORE_TEXT = get_font(25).render(f"Highscore: {HIGHSCOREVAR_EASY}", True, "#b68f40")
            HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(1075, 680))
            SCREEN.blit(HIGHSCORE_TEXT, HIGHSCORE_RECT)
        elif difficulty == "MID":
            HIGHSCORE_TEXT = get_font(25).render(f"Highscore: {HIGHSCOREVAR_MID}", True, "#b68f40")
            HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(1075, 680))
            SCREEN.blit(HIGHSCORE_TEXT, HIGHSCORE_RECT)
        elif difficulty == "HARD":
            HIGHSCORE_TEXT = get_font(25).render(f"Highscore: {HIGHSCOREVAR_HARD}", True, "#b68f40")
            HIGHSCORE_RECT = HIGHSCORE_TEXT.get_rect(center=(1075, 680))
            SCREEN.blit(HIGHSCORE_TEXT, HIGHSCORE_RECT)
        

        PLAY_BUTTON = Button(image=None, pos=(640, 250),
        #image = pygame.image.load("'assets/Play Rect.png")
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color=BLUE)
        #image=pygame.image.load("'assets/Options Rect.png")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color=GREEN)
        #image=pygame.image.load("'assets/Quit Rect.png")
        QUIT_BUTTON = Button(image=None, pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color=RED)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    option_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quit_game()

        pygame.display.update()


pygame.init()
# Random zahl für Ping Pong Sound
random_sound = random.randint(1, 2)
# Display Resolution
SCREEN = pygame.display.set_mode((1280, 720))
# Hintergrundbild laden
BG = pygame.image.load('assets\Background.png')
# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (24, 116, 205)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Variablen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCALE_FACTOR_X = SCREEN_WIDTH / 640
SCALE_FACTOR_Y = SCREEN_HEIGHT / 480
# Ballposition und Durchmesser
ball_diameter = int(20 * SCALE_FACTOR_X)
ballpos_x = 1280 / 2
ballpos_y = 720 / 2
# Ballbewegung
movement_x = 0
movement_y = 0
# Schläger Positionen
player_1_x = 20#int(20 * SCALE_FACTOR_X) #40
player_1_y = 300 #int(20 * SCALE_FACTOR_Y) #30
player_1_movement = 0#0
player_2_x = 1220#int(SCREEN_WIDTH - (2 * 20 * SCALE_FACTOR_X))
player_2_y = 300#int(20 * SCALE_FACTOR_Y)
player_2_movement = 0
racket_height = int(100 * SCALE_FACTOR_Y)
# Score
ballchanges = 0

options= load_options()
difficulty = options['difficulty']
play_sounds = options['play_sounds']
menu = main_menu()
menu

# Todo!

# -- Sound wenn Ball den Spielfeldrand berührt
# -- Verloren Screen
# -- Highscore System für die jeweiligen Spielmodi (wenn Spielmodi = easy, soll der easy highscore angezeigt werden.)