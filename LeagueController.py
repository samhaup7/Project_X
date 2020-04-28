class LeagueController:
    
    # parameter - tournament is an object of Tournament class
    def get_tournament_ID(self, tournament):
        return tournament.ID

    # parameter - MatchResult is an object of MatchResult class
    def announce_winner(self, MatchResult):
        print("The winner is " + MatchResult.winnerID)


    # parameter - tournament is an object of Tournament class
    def get_num_player(self, tournament):
        return len(tournament.players)
