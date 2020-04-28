class Advertisement:

    """
    0 - stands for no sponsorship style picked
    1 - League Sponsorship
    2 - Tournament Sponsorship            
    """
    sponsorshipID = 0
        
    def _init_(self, AdID, contents):
        self.ID = AdID
        self.content = contents
