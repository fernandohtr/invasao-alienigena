import pygame

from pygame.sprite import Group

from game import game_functions as gf
from game.button import Button
from game.game_stats import GameStats
from game.scoreboard import Scoreboard
from game.settings import Settings
from game.ship import Ship


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width,
        ai_settings.screen_height,
    ))
    pygame.display.set_caption('Alien Invasion')

    # Cria o botão Play
    play_button = Button(ai_settings, screen, 'Play')

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Cria a frota de alienígenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(
            ai_settings,
            screen,
            stats,
            sb,
            play_button,
            ship,
            aliens,
            bullets,
        )

        if stats.game_active:
            ship.update()
            gf.update_bullets(
                ai_settings,
                screen,
                stats,
                sb,
                ship,
                aliens,
                bullets
            )
            gf.update_aliens(
                ai_settings,
                screen,
                stats,
                sb,
                ship,
                aliens,
                bullets
            )

        gf.update_screen(
            ai_settings,
            screen,
            stats,
            sb,
            ship,
            aliens,
            bullets,
            play_button,
        )


run_game()