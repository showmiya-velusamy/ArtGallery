INSERT INTO Artist (ArtistID, Name, Biography, BirthDate, Nationality, Website, ContactInformation) VALUES
(1, 'Leonardo da Vinci', 'Italian polymath of the Renaissance whose areas of interest included invention, painting, sculpting, architecture, science, music, mathematics, engineering, literature, anatomy, geology, astronomy, botany, paleontology, and cartography.', '1452-04-15', 'Italian', 'https://leonardodavinci.net/', 'contact@leonardodavinci.net'),
(2, 'Vincent van Gogh', 'Dutch post-impressionist painter who is among the most famous and influential figures in the history of Western art.', '1853-03-30', 'Dutch', 'https://www.vangoghmuseum.nl/', 'contact@vangogh.com'),
(3, 'Pablo Picasso', 'Spanish painter, sculptor, printmaker, ceramicist, and stage designer who is widely regarded as one of the most influential artists of the 20th century.', '1881-10-25', 'Spanish', 'https://www.picasso.fr/', 'contact@picasso.es'),
(4, 'Michelangelo', 'Italian sculptor, painter, architect, and poet of the High Renaissance who exerted an unparalleled influence on the development of Western art.', '1475-03-06', 'Italian', 'https://michelangelo.org/', 'contact@michelangelo.it'),
(5, 'Georgia O''Keeffe', 'American artist known for her paintings of enlarged flowers, New York skyscrapers, and New Mexico landscapes.', '1887-11-15', 'American', 'https://www.okeeffemuseum.org/', 'contact@okeeffe.org');

INSERT INTO Artwork (ArtworkID, Title, Description, CreationDate, Medium, ImageURL, ArtistID) VALUES
(1, 'Mona Lisa', 'Famous portrait painting by Leonardo da Vinci', '1503-01-01', 'Oil on panel', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/687px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg', 1),
(2, 'The Starry Night', 'Iconic painting by Vincent van Gogh', '1889-06-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/687px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg', 2),
(3, 'Les Demoiselles d''Avignon', 'Landmark painting by Pablo Picasso', '1907-07-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Les_Demoiselles_d%27Avignon.jpg/450px-Les_Demoiselles_d%27Avignon.jpg', 3),
(4, 'David', 'Renowned sculpture by Michelangelo', '1504-01-01', 'Marble', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Michelangelo%27s_David_%28hi-res%29.jpg/520px-Michelangelo%27s_David_%28hi-res%29.jpg', 4),
(5, 'Jimson Weed/White Flower No. 1', 'Famous painting by Georgia O''Keeffe', '1932-01-01', 'Oil on canvas', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/Jimson_Weed_White_Flower_No_1.jpg/600px-Jimson_Weed_White_Flower_No_1.jpg', 5);

INSERT INTO [User] (UserID, Username, Password, Email, FirstName, LastName, DateOfBirth, ProfilePicture, FavoriteArtworks) VALUES
(1, 'artlover123', 'hashedpassword123', 'artlover@example.com', 'John', 'Doe', '1990-05-15', 'https://example.com/profile_picture.jpg', '1,3,5'),
(2, 'artcollector456', 'hashedpassword456', 'collector@example.com', 'Jane', 'Smith', '1985-09-20', 'https://example.com/profile_picture.jpg', '2,4'),
(3, 'galleryowner789', 'hashedpassword789', 'owner@example.com', 'Robert', 'Johnson', '1978-03-10', 'https://example.com/profile_picture.jpg', '1,2,3'),
(4, 'artstudent101', 'hashedpassword101', 'student@example.com', 'Emily', 'Brown', '2000-12-05', 'https://example.com/profile_picture.jpg', '4,5'),
(5, 'artenthusiast222', 'hashedpassword222', 'enthusiast@example.com', 'David', 'Wilson', '1995-08-30', 'https://example.com/profile_picture.jpg', '1,4');

INSERT INTO Gallery (GalleryID, Name, Description, Location, Curator, OpeningHours, ArtistID) VALUES
(1, 'Artistic Creations Gallery', 'A gallery showcasing various forms of contemporary art.', '123 Main Street, Cityville', 2, 'Mon-Sat: 10am-6pm', 2),
(2, 'Modern Art Museum', 'Museum featuring modern and abstract art pieces.', '456 Elm Street, Townsville', 3, 'Tue-Sun: 11am-7pm', 3),
(3, 'Classic Arts Center', 'Dedicated to preserving and exhibiting classic artworks.', '789 Oak Avenue, Villageton', 4, 'Wed-Mon: 9am-5pm', 4),
(4, 'Local Artists Collective', 'Showcasing works by local emerging artists.', '101 Pine Road, Hamletville', 1, 'Thu-Fri: 12pm-8pm, Sat-Sun: 10am-6pm', 1),
(5, 'Nature-Inspired Gallery', 'Featuring artworks inspired by the beauty of nature.', '234 Maple Lane, Countryside', 5, 'Sat-Sun: 9am-4pm', 5);

INSERT INTO user_Favourite_Artwork (ArtworkID, UserID) VALUES
(1, 1),
(3, 1),
(2, 2),
(4, 3),
(5, 4);

INSERT INTO Artwork_Gallery (ArtworkID, GalleryID) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);