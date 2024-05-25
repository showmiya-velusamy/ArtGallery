from Util.DBConn import DBConnection
from abc import ABC,abstractmethod
from myexceptions import ArtworkNotFoundException

class I_ArtworkService(ABC):
    @abstractmethod
    def readArtwork(self):
        pass
    @abstractmethod
    def getArtworkById(self,artworkId):
        pass
    @abstractmethod
    def addArtwork(self,new_artwork):
        pass
    @abstractmethod
    def removeArtwork(self,artworkId):
        pass
    @abstractmethod
    def updateArtwork(self,artworkId,description,title,creationDate,medium,imageURL,artistID):
        pass
class ArtworkService(I_ArtworkService,DBConnection):
    def readArtwork(self):
        try:
            self.cursor.execute("select * from artwork")
            artworks=self.cursor.fetchall()
            for artwork in artworks:
                print(artwork)
            return artwork
        except Exception as e:
            print(e)
            return None
    
    def getArtworkById(self,artworkId):
        try:
            self.cursor.execute("select * from artwork where artworkId=?",(artworkId))
            artwork=self.cursor.fetchone()
            if artwork is None:
                raise ArtworkNotFoundException(artworkId)
            else:
                print(artwork)

        except ArtworkNotFoundException as e:
            print(e)

        except Exception as e:
            print(e)

    def addArtwork(self,new_artwork):
        try:
            self.cursor.execute("insert into Artwork(artworkId,title,description,creationDate,medium,imageURL) VALUES(?,?,?,?,?,?)",
                      (new_artwork.artworkId,new_artwork.title,new_artwork.description,new_artwork.creationDate,new_artwork.medium,new_artwork.imageURL)
                        )
            new_artwork_id = self.cursor.fetchall()
            self.conn.commit() 
            return new_artwork_id
        except Exception as e:
            print("Error!!",e)
        
    def removeArtwork(self,artworkId):
        try:
                self.cursor.execute("Delete FROM User_Favorite_Artwork WHERE artworkId = ?", (artworkId,))
                self.cursor.execute("Delete FROM Artwork_Gallery WHERE artworkId = ?", (artworkId,))
                self.cursor.execute("Delete from artwork where artworkId=?",(artworkId))
                self.conn.commit()
        except Exception as e:
            print(e)
       
    def updateArtwork(self,artworkId,title,description,creationDate,medium,imageURL):
        try:
          
            self.cursor.execute("update artwork SET  artworkId,title, description , creationDate, medium, imageURL WHERE artworkId = ? ",
                        (title,description,creationDate,medium,imageURL,artworkId)
                        )
            self.conn.commit()
            return True

        except Exception as e:
            print(e)
            return False
