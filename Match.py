class Match:
    match_is_ongoing = False    # match is not started yet
    
    def _init_(self, matchID):
        self.ID = matchID

    def start_match(self, start):
        # if the match already starts
        if self.match_is_ongoing == True:
            return self.match_is_ongoin
        # if the input value is True
        elif start == True:
            self.match_is_ongoing = start
            return self.match_is_ongoing
        # if the game is not started yet, prompt to user
        else:
            print("Match is not started!")
