from abc import ABC, abstractmethod

class IVirtualArtGallery(ABC):
    @abstractmethod
    def add_artwork(self, artwork):
        pass
    
    @abstractmethod
    def update_artwork(self, artwork):
        pass
    
    @abstractmethod
    def remove_artwork(self, artworkID):
        pass
    
    @abstractmethod
    def get_artwork_by_id(self, artworkID):
        pass
    
    @abstractmethod
    def search_artworks(self, keyword):
        pass
    
    @abstractmethod
    def add_artwork_to_favorite(self, userID, artworkID):
        pass
    
    @abstractmethod
    def remove_artwork_from_favorite(self, userID, artworkID):
        pass
    
    @abstractmethod
    def get_user_favorite_artworks(self, userID):
        pass
