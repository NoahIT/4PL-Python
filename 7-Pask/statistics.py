class Statistics:
    def __init__(self):
        self.statistics = {
            "wins": 0,
            "loss": 0,
            "played_in_total": 0,
            "w/l": 0.0
        }

    def info(self):
        print(f"""
        Wins: {self.statistics['wins']}
        Losses: {self.statistics['loss']}
        Play_Count: {self.statistics['played_in_total']}
        Win/Lose: {round(self.statistics['w/l'], 2)}
        """)

    def update_info(self, wins=0, loss=0):
        if wins != 0:
            self.statistics['wins'] = wins
        if loss != 0:
            self.statistics['loss'] = loss
        self.statistics['played_in_total'] = self.statistics['wins'] + self.statistics['loss']
        self.statistics['w/l'] = self.statistics['wins'] / self.statistics['loss']

    def update_win(self):
        print('Win updated')
        self.statistics['wins'] = self.statistics['wins'] + 1
        self.statistics['played_in_total'] = self.statistics['wins'] + self.statistics['loss']

        if self.statistics['wins'] > 0 and self.statistics['loss'] == 0:
            self.statistics['w/l'] = 1
        elif self.statistics['wins'] == 0 and self.statistics['loss'] > 0:
            self.statistics['w/l'] = 0
        else:
            self.statistics['w/l'] = self.statistics['wins'] / self.statistics['loss']
        print(self.statistics['wins'])

    def update_loss(self):
        print('Lose updated')
        self.statistics['loss'] = self.statistics['loss'] + 1
        self.statistics['played_in_total'] = self.statistics['wins'] + self.statistics['loss']
        if self.statistics['wins'] > 0 and self.statistics['loss'] == 0:
            self.statistics['w/l'] = 1
        elif self.statistics['wins'] == 0 and self.statistics['loss'] > 0:
            self.statistics['w/l'] = 0
        else:
            self.statistics['w/l'] = self.statistics['wins'] / self.statistics['loss']
        print(self.statistics['loss'])
