class Artwork:
    def __init__(self, artworkID=None, title=None, description=None, creationDate=None, medium=None, imageURL=None, artistID=None):
        self.artworkID = artworkID
        self.title = title
        self.description = description
        self.creationDate = creationDate
        self.medium = medium
        self.imageURL = imageURL
        self.artistID = artistID

    def get_artworkID(self):
        return self.artworkID

    def set_artworkID(self, artworkID):
        self.artworkID = artworkID

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_creationDate(self):
        return self.creationDate

    def set_creationDate(self, creationDate):
        self.creationDate = creationDate

    def get_medium(self):
        return self.medium

    def set_medium(self, medium):
        self.medium = medium

    def get_imageURL(self):
        return self.imageURL

    def set_imageURL(self, imageURL):
        self.imageURL = imageURL

    def get_artistID(self):
        return self.artistID

    def set_artistID(self, artistID):
        self.artistID = artistID

