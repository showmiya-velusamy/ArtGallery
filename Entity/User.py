class User:
    def __init__(self, userID=None, username=None, password=None, email=None, firstName=None, lastName=None, dateOfBirth=None, dateOfBirth=None, favoriteArtworks=None):
        self.userID = userID
        self.username = username
        self.password = password
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.favoriteArtworks = favoriteArtworks
        
    def get_userID(self):
        return self.userID

    def set_userID(self, userID):
        self.userID = userID

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_firstName(self):
        return self.firstName

    def set_firstName(self, firstName):
        self.firstName = firstName

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def get_dateOfBirth(self):
        return self.dateOfBirth

    def set_dateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
    
    def get_profilePicture(self):
        return self.profilePicture

    def set_profilePicture(self, profilePicture):
        self.profilePicture = profilePicture
        
    def get_favouriteArtworks(self):
        return self.favouriteArtworks

    def set_favouriteArtworks(self, favouriteArtworks):
        self.favoriteArtworks = favouriteArtworks
