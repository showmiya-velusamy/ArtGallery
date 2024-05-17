from abc import ABC, abstractmethod
from Util.DBConn import DBConnection

class IUserFavouriteService(ABC):
    @abstractmethod
    def add_UserFavourite(self, UserID,ArtworkID):
        pass
    
    @abstractmethod
    def update_UserFavourite(self,UserID,ArtworkID):
        pass
    
    @abstractmethod
    def delete_UserFavourite(self, ArtworkID):
        pass
    
    @abstractmethod
    def read_UserFavourite(self):
        pass
    
class user_FavouriteService(IUserFavouriteService,DBConnection):
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
            
    def add_favourite(self,UserId,ArtworkID):
        try:
            self.cursor.execute("insert INTO user_Favourite_Artworks (ArtworkID,UserID) VALUES(?,?)",
                                (ArtworkID,UserId))
            
            self.conn.commit() 
        except Exception as e:
            print(e)