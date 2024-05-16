CREATE TABLE Artist (
    ArtistID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Biography TEXT,
    BirthDate DATE,
    Nationality VARCHAR(100),
    Website VARCHAR(255),
    ContactInformation VARCHAR(255)
);

CREATE TABLE Artwork (
    ArtworkID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    CreationDate DATE,
    Medium VARCHAR(100),
    ImageURL VARCHAR(255) ,-- or any reference to the digital representation
	ArtistID INT,
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE [User] (
    UserID INT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(255) NOT NULL, -- Storing hashed passwords for security
    Email VARCHAR(255) UNIQUE NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    ProfilePicture VARCHAR(255), -- URL or reference to the profile picture
    FavoriteArtworks VARCHAR(255) -- Comma-separated list of references to ArtworkIDs
);

CREATE TABLE Gallery (
    GalleryID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Location VARCHAR(255),
    Curator INT, -- Reference to ArtistID
    OpeningHours VARCHAR(255), -- Assuming opening hours can be represented as a string
	ArtistID INT,
	FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID)
);

CREATE TABLE user_Favourite_Artwork(
    ArtworkID INT,
	UserID INT,
	FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID),
	FOREIGN KEY (userID) REFERENCES [user](userID)
);

CREATE TABLE Artwork_Gallery(
    ArtworkID INT,
	GalleryID INT,
	FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID),
	FOREIGN KEY (GalleryID) REFERENCES Gallery(GalleryID)
);
