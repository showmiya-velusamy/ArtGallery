import unittest

from DAO.IArtworkServices import ArtworkService
from Entity.Artwork import Artwork



class TestArtworkyServiceModule(unittest.TestCase):
    def setUp(self):
        self.artwork_service = ArtworkService()

    def test_add_artwork(self):
        artworkID=5
        description='A painting by Pablo Picasso.'
        title='Les Demoiselles Avignon'
        creationDate='1907-07-01'
        medium='Oil on canvas'
        imageURL='https://example.com/lesdemoiselles.jpg'
        new_artwork=Artwork(artworkID,description,title,creationDate,medium,imageURL)
        created_artwork_id = self.artwork_service.addArtwork(new_artwork)
        self.assertIsNotNone(created_artwork_id)

    def test_read_artwork(self):
        artworks = self.artwork_service.readArtwork()
        self.assertIsNotNone(artworks)
        self.assertGreater(len(artworks), 0)

    def test_update_artwork(self):
        artworkID=3
        description='A painting by Henri Matisse'
        title='The Dance'
        creationDate='1910-01-01'
        medium='Oil on canvas'
        imageURL='https://example.com/thedance.jpg'
        self.artwork_service.updateArtwork(artworkID,description,title,creationDate,medium,imageURL)


        self.artwork_service.cursor.execute(
            "SELECT * FROM artwork WHERE artworkId=?", (artworkID,) 
        )
        updated_artwork = self.artwork_service.cursor.fetchone()


        self.assertEqual(updated_artwork[1], description)
        self.assertEqual(updated_artwork[2], title)
        self.assertEqual(updated_artwork[3], creationDate)
        self.assertEqual(updated_artwork[4], medium)
        self.assertEqual(updated_artwork[5], imageURL)

    def test_delete_artwork(self):
        self.artworkID=3
        self.artwork_service.removeArtwork(self.artworkID)

        self.artwork_service.cursor.execute(
            "SELECT * FROM artwork WHERE artworkId = ?", (self.artworkID)
        )
        artwork = self.artwork_service.cursor.fetchone()

        self.assertIsNone(artwork)
    



if __name__ == "__main__":
    unittest.main()