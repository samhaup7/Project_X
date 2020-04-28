class Game:

    isVerified = False
    isRejected = False
    isAccepted = False
    rating = None
    status = "Not submitted."
    
    def _init_(self, gameName, gameID):
        self.name = gameName
        self.ID = gameID
