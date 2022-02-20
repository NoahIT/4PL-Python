class GameSettings:
    def __init__(self, health, name):
        self.name = name
        self.health = health


class DifficultyRules:
    def __init__(self):
        self.difficulties = [
            GameSettings(name='easy', health=9),
            GameSettings(name='medium', health=6),
            GameSettings(name='hard', health=3)
        ]

    def get_difficulties(self):
        options = ''
        for difficulties in self.difficulties:
            options += f'{difficulties.name}/'
        options = options[:-1:]
        return options

    def get_health(self, search):
        for difficulties in self.difficulties:
            if difficulties.name == search:
                return difficulties.health

    def get_name(self, search):
        for difficulties in self.difficulties:
            if difficulties.name == search:
                return difficulties.name
