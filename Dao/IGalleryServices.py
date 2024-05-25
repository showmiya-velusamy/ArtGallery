from Util.DBConn import DBConnection
from abc import ABC,abstractmethod



class I_GalleryService(ABC):
    @abstractmethod
    def readGallery(self):
        pass
    @abstractmethod
    def addGallery(self,new_artist):
        pass
    @abstractmethod
    def removeGallery(self,artistId):
        pass
    @abstractmethod
    def updateGallery(self,galleryId,name, description, location, curator, openingHours, artistID):
        pass
class GalleryService(I_GalleryService,DBConnection):
    def readGallery(self):
        try:
            self.cursor.execute("select * from gallery")
            galleries=self.cursor.fetchall()
            for gallery in galleries:
                 print(gallery)
            return True
        except Exception as e:
            print(e)


    def addGallery(self,galleryId,name, description, location, curator, openingHours, artistId):
        try:
            self.cursor.execute("insert INTO gallery (galleryId,name, description, location, curator, openingHours, artistID)  VALUES(?,?,?,?,?,?)",
                                (galleryId,name, description, location, curator, openingHours, artistId))
            
            new_gallery_id = self.cursor.fetchone()
            self.conn.commit() 
        except Exception as e:
            print(e)

       
    def removeGallery(self,galleryId):
        try:
                self.cursor.execute("Delete from artwork_gallery where galleryId=?",(galleryId))
                self.cursor.execute("Delete FROM gallery WHERE galleryId=?",(galleryId))                                   
                
                self.conn.commit()

        except Exception as e:
            print(e)
       

    def updateGallery(self,galleryId,name, description, location, curator, openingHours, artistID):
        try:
            self.cursor.execute("Update gallery SET galleryId,name, description, location, curator, openingHours, artistID WHERE galleryId= ?",
                        (galleryId,name, description, location, curator, openingHours, artistID,galleryId)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)

