

class UserNotFoundException(Exception):
    def  __init__(self,userId):
        super().__init__(f"UserID {userId} not found.")