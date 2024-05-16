from .IVirtualArtGallery import IVirtualArtGallery
from Exception.UserNotFound import UserNotFound
from Exception.ArtworkNotFound import ArtworkNotFound
from Util.DBConnUtil import DBConnUtil
from Entity.User import User

class ArtGalleryProcessor(IVirtualArtGallery):
    def add_artwork(self, Artwork):
        try:
            # Insert Artwork data into the database
            self.cursor.execute('''INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL, ArtistID)
                     VALUES (?, ?, ?, ?, ?, ?)'''(Artwork.title, Artwork.description, Artwork.creation_date,
                                      Artwork.medium, Artwork.image_url, Artwork.artist_id))
            self.conn.commit()
            print("Artwork added successfully.")
        except Exception as e:
            # Handle any exceptions that occur during the operation
            print(f"Error occurred while adding Artwork: {e}")
        finally:
            self.conn.close()
    
    def update_artwork(self, Artwork):
        try:
            # Update Artwork data in the database
            self.cursor.execute('''UPDATE Artwork 
                     SET Title = ?, Description = ?, CreationDate = ?, Medium = ?, ImageURL = ?, ArtistID = ?
                     WHERE ArtworkID = ?'''(Artwork.title, Artwork.description, Artwork.creation_date,
                                      Artwork.medium, Artwork.image_url, Artwork.artist_id, Artwork.artwork_id))
            if self.cursor.rowcount == 0:
                raise ArtWorkNotFoundException(Artwork.artwork_id) # type: ignore
            self.conn.commit()
            print("Artwork updated successfully.")
        except ArtWorkNotFoundException as e: # type: ignore
            print(f"Artwork not found: {e}")
        except Exception as e:
            # Handle any other exceptions that occur during the operation
            print(f"Error occurred while updating Artwork: {e}")
        finally:
            self.conn.close()
            
    def remove_artwork(self, ArtworkID):
        try:
            # Delete Artwork data from the database
            self.cursor.execute( '''DELETE FROM Artwork WHERE ArtworkID = ?'''
            (ArtworkID,))
            if self.cursor.rowcount == 0:
                raise ArtWorkNotFoundException(ArtworkID) # type: ignore
            self.conn.commit()
            print("Artwork removed successfully.")
        except ArtWorkNotFoundException as e: # type: ignore
            print(f"Artwork not found: {e}")
        except Exception as e:
            # Handle any other exceptions that occur during the operation
            print(f"Error occurred while removing Artwork: {e}")
        finally:
            self.conn.close()
            
    def get_artwork_by_id(self, ArtworkID):
        try:
            self.cursor.execute("select * from User_Favorite_Artwork where userId=?",(ArtworkID))
            favorite_artwork=self.cursor.fetchall()
            for Artwork in favorite_artwork:
                print(Artwork)
            if favorite_artwork is None:
                raise ArtWorkNotFoundException(ArtworkID) # type: ignore
            # Construct artwork object from fetched data
            artwork = Artwork(favorite_artwork[0], favorite_artwork[1], favorite_artwork[2], favorite_artwork[3], favorite_artwork[4], favorite_artwork[5], favorite_artwork[6])
            return artwork
        except ArtWorkNotFoundException as e: # type: ignore
            print(f"Artwork not found: {e}")
            return None  # Return None if artwork not found
        except Exception as e:
            print(f"Error occurred while getting Artwork by ID: {e}")
        finally:
            self.conn.close()
   
   
    def search_artworks(self, keyword):
        try:
            # Search artworks in the database by keyword
            self.cursor.execute( '''SELECT * FROM Artwork WHERE Title LIKE ? OR Description LIKE ?'''
            ('%'+keyword+'%', '%'+keyword+'%'))
            artworks = []
            for row in self.cursor.fetchall():
                # Construct Artwork objects from fetched data
                Artwork = Artwork(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                artworks.append(Artwork)
            return artworks
        except Exception as e:
            # Handle any exceptions that occur during the operation
            print(f"Error occurred while searching artworks: {e}")
            return []
        finally:
            self.conn.close()
            
    def add_artwork_to_favorite(self, userID, artworkID):
        try:
            # Check if the user exists
            self.cursor.execute("SELECT UserID FROM User WHERE UserID = ?", (userID,))
            user_data = self.cursor.fetchone()
            if user_data is None:
                raise UserNotFoundException(userID) # type: ignore
            # Add artwork to the user's favorite artworks
            self.cursor.execute("INSERT INTO user_Favourite_Artwork (ArtworkID, UserID) VALUES (?, ?)"
            (artworkID, userID))
            self.conn.commit()
            print("Artwork added to favorites successfully.")
        except UserNotFoundException as e: # type: ignore
            print(f"User not found: {e}")
        except Exception as e:
            # Handle any other exceptions that occur during the operation
            print(f"Error occurred while adding artwork to favorites: {e}")
        finally:
            self.conn.close()
            
    def remove_artwork_from_favorite(self, userID, artworkID):
        try:
            # Check if the user exists
            self.cursor.execute("SELECT UserID FROM User WHERE UserID = ?", (userID,))
            user_data = self.cursor.fetchone()
            if user_data is None:
                raise UserNotFoundException(userID) # type: ignore
            # Remove artwork from the user's favorite artworks
            self.cursor.execute("DELETE FROM user_Favourite_Artwork WHERE UserID = ? AND ArtworkID = ?"
            (userID, artworkID))
            self.conn.commit()
            print("Artwork removed from favorites successfully.")
        except UserNotFoundException as e: # type: ignore
            print(f"User not found: {e}")
        except Exception as e:
            # Handle any other exceptions that occur during the operation
            print(f"Error occurred while removing artwork from favorites: {e}")
        finally:
            self.conn.close()
            
    def get_user_favorite_artworks(self, userID):
        try:
            # Check if the user exists
            self.cursor.execute("SELECT UserID FROM User WHERE UserID = ?", (userID,))
            user_data = self.cursor.fetchone()
            if user_data is None:
                raise UserNotFoundException(userID) # type: ignore
            
            # Retrieve the user's favorite artworks
            self.cursor.execute("SELECT ArtworkID FROM user_Favourite_Artwork WHERE UserID = ?"
             (userID,))
            favorite_artworks = [row[0] for row in self.cursor.fetchall()]
            return favorite_artworks
        except UserNotFoundException as e: # type: ignore
            print(f"User not found: {e}")
            return []
        except Exception as e:
            # Handle any other exceptions that occur during the operation
            print(f"Error occurred while getting user's favorite artworks: {e}")
            return []
        finally:
            self.conn.close()
        
            
    