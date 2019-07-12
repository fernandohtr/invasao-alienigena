class GameStats():
    """Armazena dados estatísticos da Invesão Alienígena."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Inicia a Invasão ALienígena em um estato ativo
        self.game_active = True

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit
