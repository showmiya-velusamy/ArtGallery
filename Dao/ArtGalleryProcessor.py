from Util.DBConnUtil import DBConnUtil

class ArtistService(DBConnUtil):
    def read_artist(self):
        try:
            self.cursor.execute("SELECT * FROM Artist")
            artists = self.cursor.fetchall()
            for art in artists:
                print(art)
            return ArtistService
        except Exception as e:
            print(e)
            return None

    def add_artist(self,ArtistID, name, biography,birthDate,nationality,website,contactInformation):
        try:
            self.cursor.execute(
                "INSERT INTO Artist (ArtistID, name, biography,birthDate,nationality,website,contactInformation) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (ArtistID, name, biography,birthDate,nationality,website,contactInformation)),
            
            self.conn.commit()
            self.cursor.execute(
                "SELECT @@IDENTITY AS ID"
            )  # For getting last inserted ID in MSSQL
            last_id = self.cursor.fetchone()[0]
            return last_id
        except Exception as e:
            print(e)
            return None

    def update_movie(self,ArtistID):
        try:
           self.cursor.execute(
            """
            UPDATE Artist
            SET name = ?, biography = ?, birthDate = ?, nationality=?,website=?, contactInformation=?
            WHERE artistId = ?
            """,
            (ArtistService.name,ArtistService.biography,ArtistService.birthDate,ArtistService.nationality,ArtistService.website,ArtistService.contactInformation,ArtistID),
            )
           self.conn.commit()
        except Exception as e:
            print(e)
            return None
    def delete_movie(self, artistID):
        try:
           self.cursor.execute("DELETE FROM Artist WHERE ArtistId = ?", artistID)
           self.conn.commit()
        except Exception as e:
            print(e)
            return None
    
class ArtworkService(DBConnUtil):
    def read_artwork(self):
        try:
            self.cursor.execute("SELECT * FROM Artwork")
            Artworks = self.cursor.fetchall()
            for arts in Artworks:
                print(arts)
            return ArtworkService
        except Exception as e:
            print(e)
            return None

    def add_artwork(self,ArtworkID,title,description,creationDate,medium,imageURL,ArtistID):
        try:
            self.cursor.execute(
                "INSERT INTO Artwork (ArtworkID,title,description,creationDate,medium,imageURL,ArtistID) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (ArtworkID,title,description,creationDate,medium,imageURL,ArtistID)),
            
            self.conn.commit()
            self.cursor.execute(
                "SELECT @@IDENTITY AS ID"
            )  # For getting last inserted ID in MSSQL
            last_id = self.cursor.fetchone()[0]
            return last_id
        except Exception as e:
            print(e)
            return None

    def update_artwork(self,ArtworkID):
        try:
           self.cursor.execute(
            """
            UPDATE Artwork
            SET title = ?,description =?,creationDate = ?, medium=?,imageURL=?, ArtistID=?
            WHERE ArtworkId = ?
            """,
            (ArtworkService.title,ArtworkService.description,ArtworkService.creationDate,ArtworkService.medium,ArtworkService.imageURL,ArtworkService.ArtistID,ArtworkID),
          )
           self.conn.commit()
        except Exception as e:
            print(e)
            return None

    def delete_artwork(self, ArtworkID):
        try:
           self.cursor.execute("DELETE FROM Artwork WHERE ArtworkId = ?", ArtworkID)
           self.conn.commit()
        except Exception as e:
            print(e)
            return None
    
class GalleryService(DBConnUtil):
    def read_Gallery(self):
        try:
            self.cursor.execute("select * from Gallery")
            galleries=self.cursor.fetchall()
            for gallery in galleries:
                print(gallery)
 
        except Exception as e:
            print(e)

    def add_Gallery(self,GalleryId,name, description, location, curator, openingHours, ArtistId):
        try:
            self.cursor.execute("insert INTO Gallery (galleryId,name, description, location, curator, openingHours, artistID) VALUES(?,?,?,?,?,?,?)",
                                (GalleryId,name, description, location, curator, openingHours, ArtistId))
            
            self.conn.commit() 
        except Exception as e:
            print(e)
       
    def remove_Gallery(self,GalleryId):
        try:
            self.cursor.execute("Delete FROM Gallery WHERE GalleryId=?",(GalleryId))                                   
            
            self.conn.commit()
        except Exception as e:
            print(e)
       
class UserService(DBConnUtil):
    def read_User(self):
        try:
            self.cursor.execute("select * from User")
            users=self.cursor.fetchall()
            for customer in users:
                print(customer)
 
        except Exception as e:
            print(e)

    def add_User(self,UserId,username, password, email, firstName, lastName, dateOfBirth,profilePicture,favouriteArtworks):
        try:
            self.cursor.execute("insert INTO User (UserId,username, password, email, firstName, lastName, dateOfBirth,favouriteArtworks) VALUES(?,?,?,?,?,?,?,?)",
                                (UserId,username, password, email, firstName, lastName, dateOfBirth,profilePicture,favouriteArtworks))
            
            self.conn.commit() 
        except Exception as e:
            print(e)
       
    def delete_User(self,UserId):
        try:
            self.cursor.execute("Delete FROM User WHERE UserId=?",(UserId))                                   
            
            self.conn.commit()
        except Exception as e:
            print(e)
       

    def update_User(self,UserId,username, password, email, firstName, lastName, dateOfBirth,profilePicture,favouriteArtworks):
        try:
            self.cursor.execute("Update User SET username = ?, password = ?, email = ?, firstName = ?, lastName = ?, dateOfBirth=?,profilePicture=?,favouriteArtworks WHERE UserId= ?",
                        (username, password, email, firstName, lastName, dateOfBirth,profilePicture,favouriteArtworks,UserId)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)


class user_favourite:
    def delete_favourite(self, ArtworkID):
        try:
            self.cursor.execute("DELETE FROM user_Favourite_Artworks WHERE ArtworkId = ?", ArtworkID)
            self.conn.commit()
        except Exception as e:
            print(e)
       
    def update_favourite(self,UserId,ArtworkID):
        try:
            self.cursor.execute("Update user_Favourite_Artwork SET UserID WHERE ArtworkId= ?",
                        (ArtworkID,UserId)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)

    def read_favourite(self):
        try:
            self.cursor.execute("select * from user_favourite_Artworks")
            favourites=self.cursor.fetchall()
            for fav in favourites:
                print(fav)
 
        except Exception as e:
            print(e)
            
    def add_favourites(self,UserId,ArtworkID):
        try:
            self.cursor.execute("insert INTO user_Favourite_Artworks (ArtworkID,UserID) VALUES(?,?)",
                                (ArtworkID,UserId))
            
            self.conn.commit() 
        except Exception as e:
            print(e)