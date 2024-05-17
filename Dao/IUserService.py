from abc import ABC, abstractmethod
from Util.DBConnUtil import DBConnUtil

class IUserService(ABC):
    @abstractmethod
    def add_User(self, User):
        pass
    
    @abstractmethod
    def update_User(self, User):
        pass
    
    @abstractmethod
    def delete_User(self, UserID):
        pass
    
    @abstractmethod
    def read_User(self, UserID):
        pass    



class UserService(DBConnUtil):
    def read_user(self):
        try:
            self.cursor.execute("select * from User")
            users=self.cursor.fetchall()
            for customer in users:
                print(customer)
 
        except Exception as e:
            print(e)

    def add_user(self,UserId,username, password, email, firstName, lastName, dateOfBirth,profilePicture,favouriteArtworks):
        try:
            self.cursor.execute("insert INTO User (UserId,username, password, email, firstName, lastName, dateOfBirth,favouriteArtworks) VALUES(?,?,?,?,?,?,?,?)",
                                (UserId,username, password, email, firstName, lastName, dateOfBirth,profilePicture,favouriteArtworks))
            
            self.conn.commit() 
        except Exception as e:
            print(e)
       
    def delete_user(self,UserId):
        try:
            self.cursor.execute("Delete FROM User WHERE UserId=?",(UserId))                                   
            
            self.conn.commit()
        except Exception as e:
            print(e)
       

    def update_user(self,UserId,username, password, email, firstName, lastName, dateOfBirth,profilePicture,favouriteArtworks):
        try:
            self.cursor.execute("Update User SET username = ?, password = ?, email = ?, firstName = ?, lastName = ?, dateOfBirth=?,profilePicture=?,favouriteArtworks WHERE UserId= ?",
                        (username, password, email, firstName, lastName, dateOfBirth,profilePicture,favouriteArtworks,UserId)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)