from Dao.IArtworkService import ArtworkService
from Dao.IArtistService import ArtistService
from Dao.IGalleryService import GalleryService
from Dao.IUserService import UserService
from Dao.IUserFavouriteService import user_FavouriteService
from Entity.Artwork import Artwork
from Entity.User import User
from Entity.Artist import Artist
from Entity.Gallery import Gallery
from Entity.User_Favourite_Artwork import user_Favourite_Artwork

class MainMenu:
    artist_service = ArtistService()
    artwork_service = ArtworkService()
    gallery_service=GalleryService()
    user_service = UserService()
    user_favourite_service= user_FavouriteService

    def artist_menu(self):
        while True:
            print(
                """      
            1. Add Artist
            2. View all Artist
            3. Update an Artist 
            4. Delete Artist
            5. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                name = input("Please enter movie year: ")
                biography = input("Please give the biography: ")
                birthDate = input("Enter the Birth Date (YYYY-MM-DD) : ")
                nationality = input("Give the nationality: ")
                website= input("Enter the website: ")
                contactInformation = input("Enter the phone number: ")
                new_artist = Artist(name,biography,birthDate,nationality,website,contactInformation)
                self.artist_service.add_artist(new_artist)
            elif choice == 2:
                self.artist_service.read_artist()
            if choice == 3:
                ArtistID = int(input("Please enter ArtistID: "))
                name = input("Please enter movie year: ")
                biography = input("Please give the biography: ")
                birthDate = input("Enter the Birth Date (YYYY-MM-DD) : ")
                nationality = input("Give the nationality: ")
                website= input("Enter the website: ")
                contactInformation = input("Enter the phone number: ")
                updated_artist = Artist(ArtistID,name,biography,birthDate,nationality,website,contactInformation)
                self.movie_service.update_movie(updated_artist, ArtistID)
            elif choice == 4:
                ArtistID = int(input("Please tell a artist id to delete: "))
                self.artist_service.delete_artist(ArtistID)
            elif choice == 5:
                break

    def artwork_menu(self):
        while True:
            print(
                """      
            1. Add an Artwork
            2. View all Artworks
            3. Get Artwork details by id
            4. Delete an Artwork
            5. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                title = input("Please enter title: ")
                description = input("Give Artwork description: ")
                creationDate = input("Enter the creation date: ")
                medium = input("Enter through which medium: ")
                imageURL = input("Give the artwork url: ")
                ArtistID = int(input("Enter the artistID: "))
                new_artwork = Artwork(title,description,creationDate,medium,imageURL,ArtistID)
                self.artwork_service.add_artwork(new_artwork)
            elif choice == 2:
                self.artwork_service.read_artwork()
            elif choice == 3:
                ArtworkID = input("Please enter artwork id: ")
                self.artwork_service.get_artwork_by_ID(ArtworkID)
            elif choice == 4:
                ArtworkID = int(input("Please tell an artwor id to delete: "))
                self.artwork_service.delete_artwork(ArtworkID)
            elif choice == 5:
                break

    def gallery_menu(self):
        while True:
            print(
                """      
            1. Add Gallery
            2. View Gallery
            3. Update Gallery 
            4. Delete Gallery
            5. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                name = input("Please enter gallery name: ")
                description= input("Please give the description: ")
                location = input("Enter the location: ")
                curator = input("Give the curator: ")
                openingHours= input("Enter the opening hours: ")
                ArtistID = input("Enter the artistID: ")
                new_gallery = Gallery(name,description,location,curator,openingHours,ArtistID)
                self.gallery_service.add_Gallery(new_gallery)
            elif choice == 2:
                self.gallery_service.read_Gallery()
            if choice == 3:
                GalleryID = input("Enter the galleryID: ")
                name = input("Please enter gallery name: ")
                description= input("Please give the description: ")
                location = input("Enter the location: ")
                curator = input("Give the curator: ")
                openingHours= input("Enter the opening hours: ")
                ArtistID = input("Enter the artistID: ")
                updated_gallery = Gallery(GalleryID,name,description,location,curator,openingHours,ArtistID)
                self.gallery_service.update_gallery(updated_gallery, GalleryID)
            elif choice == 4:
                GalleryID = int(input("Please tell a gallery id to delete: "))
                self.gallery_service.delete_gallery(GalleryID)
            elif choice == 5:
                break

    def userfavourite_menu(self):
        while True:
            print(
                """      
            1. Add Favourite
            2. View Favourite
            3. Update Favourite
            4. Delete Favourite
            5. Back to main menu
                    """
            )
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                ArtworkID = input("Enter the artworkID: ")
                UserID = input("Enter the userID: ")
                new_favourite = user_Favourite_Artwork(ArtworkID,UserID)
                self.user_favourite_service.add_favourite(new_favourite)
            elif choice == 2:
                self.user_favourite_service.read_favourite()
            if choice == 3:
                ArtworkID = input("Enter the artworkID: ")
                UserID= input("Enter the userID: ")
                updated_favourites = user_Favourite_Artwork(ArtworkID,UserID)
                self.user_favourite_service.update_favourite(updated_favourites, ArtworkID)
            elif choice == 4:
                ArtworkID = int(input("Please tell a artwork id to delete: "))
                self.user_favourite_service.delete_favourite(ArtworkID)
            elif choice == 5:
                break



def main():
    main_menu = MainMenu()

    while True:
        print(
            """      
            1. Artist Management
            2. Artwork Management
            3. Gallery Management
            4.User Favourite Management
            4. Exit
                """
        )

        choice = int(input("Please choose from above options: "))

        if choice == 1:
            main_menu.artist_menu()
        elif choice == 2:
            main_menu.artwork_menu()
        elif choice == 3:
            main_menu.gallery_menu()
        elif choice==4:
            main_menu.userfavourite_menu()
        elif choice == 5:
            main_menu.artist_menu.close()  
            main_menu.artwork_menu.close()
            main_menu.gallery_menu.close()
            main_menu.userfavourite_menu.close()  
            break

if __name__ == "__main__":
    print("Welcome to the movies app")
    main()