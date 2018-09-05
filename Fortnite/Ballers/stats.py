class Stats:

    def __init__(self, stat_id=None, solo_kpg=None, duo_kpg=None, squad_kpg=None, solo_matches=None, duo_matches=None,
                 squad_matches=None, solo_wins=None, duo_wins=None, squad_wins=None, solo_win_percentage=None,
                 duo_win_percentage=None, squad_win_percentage=None, wcpi_score=None, user_id=None, date=None,
                 season=None):
        self.stat_id = float(stat_id)
        self.solo_kpg = float(solo_kpg)
        self.duo_kpg = float(duo_kpg)
        self.squad_kpg = float(squad_kpg)
        self.solo_matches = float(solo_matches)
        self.duo_matches = float(duo_matches)
        self.squad_matches = float(squad_matches)
        self.solo_wins = float(solo_wins)
        self.duo_wins = float(duo_wins)
        self.squad_wins = float(squad_wins)
        self.solo_win_percentage = float(solo_win_percentage)
        self.duo_win_percentage = float(duo_win_percentage)
        self.squad_win_percentage = float(squad_win_percentage)
        self.wcpi_score = float(wcpi_score)
        self.user_id = float(user_id)
        self.date = date
        self.season = float(season)
        self.total_wins = self.solo_wins + self.duo_wins + self.squad_wins
        self.total_matches = self.solo_matches + self.duo_matches + self.squad_matches

    def __repr__(self):
        return '<Stats {}>'.format(self.stat_id)