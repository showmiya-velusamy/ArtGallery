from abc import ABC, abstractmethod
from Util.DBConn import DBConnection

class IArtistService(ABC):
    @abstractmethod
    def add_artist(self, artist):
        pass
    
    @abstractmethod
    def update_artist(self, artist):
        pass
    
    @abstractmethod
    def delete_artist(self, artistID):
        pass
    
    @abstractmethod
    def read_artist(self):
        pass
    

class ArtistService(IArtistService,DBConnection):
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

    def update_artist(self,ArtistID):
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
    def delete_artist(self, ArtistID):
        try:
           self.cursor.execute("DELETE FROM Artist WHERE ArtistId = ?", ArtistID)
           self.conn.commit()
        except Exception as e:
            print(e)
            return None