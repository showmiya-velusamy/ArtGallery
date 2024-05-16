from Dao.ArtGalleryProcessor import ArtGalleryProcessor
from Entity.Artwork import Artwork
from Entity.User import User
from Exception import UserNotFound, ArtworkNotFound
class ArtManagement:
    def __init__(self):
        self.ArtGalleryProcessor = ArtGalleryProcessor()
    
    def display_menu(self):
        print("\n Welcome to Virtual Art Gallery")
        print("1. Add Artwork")
        print("2. Update Artwork")
        print("3. Remove Artwork")
        print("4. Get Artwork by ID")
        print("5. Search Artwork")
        print("6. Add artwork to favorite")
        print("7. Remove artwork from favorite")
        print("8. Get user favorite artworks")
        print("9. Exit ❗")
