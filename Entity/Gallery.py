class Gallery:
    def __init__(self, artistID=None, name=None, description=None, location=None, curator=None, openingHours=None, artistID=None):
        self.artistID = artistID
        self.name = name
        self.description = description
        self.location = location
        self.curator = curator
        self.openingHours = openingHours
        self.artistID = artistID
        
    def get_galleryID(self):
        return self.galleryID

    def set_galleryID(self, galleryID):
        self.galleryID = galleryID

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_curator(self):
        return self.curator

    def set_curator(self, curator):
        self.curator = curator

    def get_openingHours(self):
        return self.openingHours

    def set_openingHours(self, openingHours):
        self.openingHours = openingHours

    def get_artistID(self):
        return self.artistID

    def set_artistID(self, artistID):
        self.artistID = artistID

