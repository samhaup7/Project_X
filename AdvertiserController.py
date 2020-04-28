class AdvertiserController:

    def chooseLeagueSponsorship(self, advertisement):
        advertisement.sponsorshipID = 1   # refer to sponsorship class

    def chooseTournSponsorship(self, advertisement):
        advertisement.sponsorshipID = 2   # refer to sponsorship class

    def cancelAdvertisement(self, advertisement):
        advertisement.ID = None
        advertisement.content = None
