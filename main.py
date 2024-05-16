from Dao.ArtGalleryProcessor import ArtGalleryProcessor
from Entity.Artwork import Artwork
from Entity.User import User

class ArtManagement:
    def __init__(self):
        self.ArtGalleryProcessor = ArtGalleryProcessor()
    def main(self):
        self.display_menu()
    
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

    def add_art(self):
        artworkID= int(input("Enter the artworkID: "))
        title = input("Enter the Title: ")
        description= input("Description: ")
        creationDate= input("Enter a date (YYYY-MM-DD): ")
        medium=input("Medium: ")
        imageURL=input("Enter the image URL: ")
        artistID=int(input("Enter the artistID: "))
        artwork = Artwork(artworkID,title,description,creationDate,medium,imageURL,artistID)
        self.ArtGalleryProcessor.add_artwork(artwork)
        
    def update_art(self):
        artworkID= int(input("Enter the artworkID: "))
        title = input("Enter the Title: ")
        description= input("Description: ")
        creationDate= input("Enter a date (YYYY-MM-DD): ")
        medium=input("Medium: ")
        imageURL=input("Enter the image URL: ")
        artistID=int(input("Enter the artistID: "))
        updated_artwork = Artwork(artworkID,title,description,creationDate,medium,imageURL,artistID)
        self.ArtGalleryProcessor.update_artwork(updated_artwork)
        
    def remove_art(self):
        artworkID =int(input("Enter the ArtworkID to remove: "))
        removed_artwork = Artwork(artworkID)
        self.ArtGalleryProcessor.remove_artwork(removed_artwork)
    
    def get_art_by_ID(self):
        artworkID =int(input("Enter the ArtworkID to view: "))
        read_artwork = Artwork(artworkID)
        self.ArtGalleryProcessor.get_artwork_by_id(read_artwork)
        
    def search_art(Self):
       keyword =input("Enter the keyword to search: ")
       artworks = ArtGalleryProcessor.search_artworks(keyword)
       if artworks:
            print("Matching Artworks: ")
            for artwork in artworks:
                print(artwork)
       else:
            print("No matching artworks found.")
            
    def add_art_to_fav(self):
        userID=int(input("Enter the userID: "))
        artworkID=int(input("Enter the artworkID: "))
        user=User(userID)
        artwork=Artwork(artworkID)
        self.ArtGalleryProcessor.add_artwork_to_favorite(user,artwork)
        
    def remove_art_from_fav(self):
        userID=int(input("Enter the userID: "))
        artworkID=int(input("Enter the artworkID: "))
        user=User(userID)
        artwork=Artwork(artworkID)
        self.ArtGalleryProcessor.remove_artwork_from_favorite(user,artwork)
        
    def get_user_fav_art(self):
        userID=int(input("Enter the userID: "))
        user=User(userID)
        self.ArtGalleryProcessor.get_user_favorite_artworks(user)
    
    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_art()
            elif choice == "2":
                self.update_art()
            elif choice == "3":
                self.remove_art()
            elif choice == "4":
                self.get_art_by_ID()
            elif choice == "5":
                self.search_art()
            elif choice == "6":
                self.add_art_to_fav()
            elif choice=="7":
                self.remove_art_from_fav()
            elif choice=="8":
                self.get_user_fav_art()
            elif choice == "9":
                print("Exited Visit Again🎇")
                break
            else:
                print("Invalid choice❌")
if __name__ == "__main__":
     Art_Management=ArtManagement()        
     Art_Management.main()