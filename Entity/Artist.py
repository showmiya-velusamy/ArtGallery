class Artist:
    def __init__(self, artistID=None, name=None, biography=None, birthDate=None, nationality=None, website=None, contactInformation=None):
        self.artistID = artistID
        self.name = name
        self.biography = biography
        self.birthDate = birthDate
        self.nationality = nationality
        self.website = website
        self.contactInformation = contactInformation
        
    def get_artistID(self):
        return self.artistID

    def set_contactInformation(self, artistID):
        self.artistID = artistID

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_biography(self):
        return self.biography

    def set_biography(self, biography):
        self.biography = biography

    def get_birthDate(self):
        return self.birthDate

    def set_birthDate(self, birthDate):
        self.birthDate = birthDate

    def get_nationality(self):
        return self.nationality

    def set_nationality(self, nationality):
        self.nationality = nationality

    def get_website(self):
        return self.website

    def set_website(self, website):
        self.website = website

    def get_contactInformation(self):
        return self.contactInformation

    def set_contactInformation(self, contactInformation):
        self.contactInformation = contactInformation

