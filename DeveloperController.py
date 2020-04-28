class DeveloperController:

    def submit_new_game(self, game):
        if isVerified == False:
            game.status = "Submitted"
