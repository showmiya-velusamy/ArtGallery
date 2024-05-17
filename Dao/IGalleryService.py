from abc import ABC, abstractmethod
from Util.DBConnUtil import DBConnUtil

class IGalleryService(ABC):
    @abstractmethod
    def add_Gallery(self, Gallery):
        pass
    
    @abstractmethod
    def update_Gallery(self, Gallery):
        pass
    
    @abstractmethod
    def delete_Gallery(self, GalleryID):
        pass
    
    @abstractmethod
    def read_Gallery(self, GalleryID):
        pass
    
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
            
    def update_Gallery(self,GalleryID):
        try:
           self.cursor.execute(
            """
            UPDATE Gallery
            SET name = ?,description =?,location = ?, curator=?,openingHours=?, ArtistID=?
            WHERE GalleryId = ?
            """,
            (GalleryService.name,GalleryService.description,GalleryService.location,GalleryService.curator,GalleryService.openingHours,GalleryService.ArtistID,GalleryID),
          )
           self.conn.commit()
        except Exception as e:
            print(e)
            return None

       

