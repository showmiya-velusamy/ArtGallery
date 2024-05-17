from abc import ABC, abstractmethod
from Util.DBConn import DBConnection

class IArtworkService(ABC):
    @abstractmethod
    def add_artwork(self, Artwork):
        pass
    
    @abstractmethod
    def update_artwork(self, Artwork):
        pass
    
    @abstractmethod
    def delete_artwork(self, ArtworkID):
        pass
    
    @abstractmethod
    def read_artwork(self, ArtworkID):
        pass
    

class ArtworkService(IArtworkService,DBConnection):
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
    
    def get_artwork_by_ID(self,ArtworkID):
        try:
            self.cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = ? ",ArtworkID)
            artwork=self.cursor.fetchall()
            print(artwork)
            self.conn.commit()
        except Exception as e:
            print(e)
            return None
    
            