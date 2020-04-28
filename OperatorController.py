class OperatorController:

    def reject_new_game(self, game):
        if game.isVerified == False:
            if game.isAccepted == False:
                game.isRejected = True
                game.isVerified = True
                game.status = "Rejected"
        else:
            return

    def accept_new_game(self, game):
        if game.isVerified == False:
            if game.isRejected == False:
                game.isAccepted = True
                game.isVerified = True
                game.status = "Accepted"
        else:
            return
