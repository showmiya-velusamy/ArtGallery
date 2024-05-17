import unittest

from Dao.IArtworkService import ArtworkService
from Entity.Artwork import Artwork


class TestArtworkService(unittest.TestCase):
    def setUp(self):
        self.IArtworkService = ArtworkService()
        self.test_artwork = Artwork("Initial Artist")
        self.test_ArtworkID = self.IArtworkService.add_artwork(
            self.test_artwork
        )
        self.assertIsNotNone(self.test_ArtworkID)

    def tearDown(self):
        self.artwork_service.conn.close()

    def test_add_artwork(self):
        artwork_id = self.IArtworkService.add_artwork(
            ArtworkID=1,
            title="Sunset at Sea",
            description="A breathtaking view of the sunset over the ocean waves.",
            creationDate="2023-08-12",
            medium="Oil on canvas",
            imageURL="https://example.com/sunset_at_sea.jpg",
            ArtistID=1
        )
        self.assertIsNotNone(artwork_id, "Artwork should be added successfully")

    def test_read_artwork(self):
        artworks = self.IArtworkService.read_artwork()
        self.assertIsNotNone(artworks, "Artworks should be fetched successfully")

    def test_update_artwork(self):
        updated = self.IArtworkService.update_artwork(
            ArtworkID=2,
            title="Enchanted Forest",
            description="A mystical forest scene with magical creatures and glowing flora.",
            creationDate="2024-03-20",
            medium="Digital painting",
            imageURL="https://example.com/enchanted_forest.jpg",
            ArtistID=2
        )
        self.assertIsNotNone(updated, "Artwork should be updated successfully")

    def test_delete_artwork(self):
        deleted = self.IArtworkService.delete_artwork(ArtworkID=1)
        self.assertIsNotNone(deleted, "Artwork should be deleted successfully")

    def test_get_artwork_by_ID(self):
        artwork = self.IArtworkService.get_artwork_by_ID(ArtworkID=3)
        self.assertIsNotNone(artwork, "Artwork should be fetched successfully")

if __name__ == '__main__':
    unittest.main()
