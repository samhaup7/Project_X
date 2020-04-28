class AdvertisementController:

    def _init_(self, AdScheme, AdID advertiser, leagueOwner):
        self.scheme = AdScheme
        self.ID = AdID
        self.advertiser = advertiser
        self.leagueOwner = leagueOwner
        
    def get_LeagueOwner(self):
        return self.leagueOwner

    def get_AdID(self):
        return self.ID

        
    
