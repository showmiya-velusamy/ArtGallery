from myexceptions import UserNotFoundException
from Util.DBConn import DBConnection
from abc import ABC,abstractmethod

class I_UserService(ABC):
    @abstractmethod
    def readUser(self):
        pass
    @abstractmethod
    def addUser(self,new_user):
        pass
    @abstractmethod
    def removeUser(self,userId):
        pass
    @abstractmethod
    def updateUser(self,userId,username,password,email,firstName,lastName,dateOfBirth,picture,favoriteArtworks):
        pass

class UserService(I_UserService,DBConnection):
    def readUser(self):
        try:
            self.cursor.execute("select * from UserTable")
            users=self.cursor.fetchall()
            for user in users:
                print(user)
  
        except Exception as e:
            print(e)

    def readUserById(self,userId):
        try:
            self.cursor.execute("select * from UserTable where userId=?",(userId))
            user=self.cursor.fetchall()
            if user is None:
                raise UserNotFoundException(userId)
            else:
                print(user)
        except UserNotFoundException as e:
            print(e)
        
        except Exception as e:
            print(e)

    def addUser(self,new_user):
        try: 
            self.cursor.execute("Insert INTO userTable (userId,username,password,email,firstName,lastName,dateOfBirth,profilePicture,favoriteArtworks) VALUES(?,?,?,?,?,?,?,?,?)",
                            (new_user.userId,new_user.username,new_user.password,new_user.email,new_user.firstName,new_user.lastName,new_user.dateOfBirth,new_user.profilePicture,new_user.favoriteArtworks)
                            )
                
            self.conn.commit()  
        except Exception as e:
            print(e)
       

    def removeUser(self,UserId):
        try:
                self.cursor.execute("Delete FROM userTable WHERE userId=?",
                            (UserId)
                            )
                self.conn.commit()     
        except Exception as e:
            print(e)
       

    def updateUser(self,userId,username,password,email,firstName,lastName,dateOfBirth,profilePicture,favoriteArtworks):
        try:
            self.cursor.execute("Update UserTable SET userId,username, password, email, firstName, lastName , dateOfBirth , profilePicture , favoriteArtworks  WHERE userId=?",
                        (userId,username,password,email,firstName,lastName,dateOfBirth,profilePicture,favoriteArtworks,userId)
                        )
            self.conn.commit()
        except Exception as e:
            print(e)
            
