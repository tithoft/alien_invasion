from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.set_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def set_high_score(self):
        """Sets the current high score that is stored in file."""
        path = Path('high_score.json')
        contents = path.read_text()
        # Checks to see if high score is in file.
        if contents:
            self.high_score = json.loads(contents)
        else:
            self.high_score = 0
