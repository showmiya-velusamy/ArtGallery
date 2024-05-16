class user_Favourite_Artwork:
    def __init__(self,ArtworkID,UserID):
        self.ArtworkID=ArtworkID
        self.UserID=UserID
    
    def get_artworkID(self):
        return self.artworkID

    def set_artworkID(self, artworkID):
        self.artworkID = artworkID
    
    def get_userID(self):
        return self.userID

    def set_userID(self, userID):
        self.userID = userID