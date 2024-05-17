import unittest

from Dao.IGalleryService import GalleryService
from Entity.Gallery import Gallery
import unittest


class TestGalleryService(unittest.TestCase):
    def setUp(self):
        self.IGalleryService = GalleryService()
        self.test_gallery = Gallery("Initial Gallery")
        self.test_GalleryID = self.IGalleryService.add_gallery(
            self.test_gallery
        )
        self.assertIsNotNone(self.test_GalleryID)

    def tearDown(self):
        self.IGalleryService.conn.close()

    def test_add_gallery(self):
        self.IGalleryService.add_Gallery(
            GalleryId=1,
            name="Art Gallery XYZ",
            description="A contemporary art gallery showcasing emerging artists.",
            location="123 Main Street, City",
            curator="John Doe",
            openingHours="Mon-Fri: 10am-6pm",
            ArtistId=1
        )

    def test_read_gallery(self):
        self.IGalleryService.read_Gallery()

    def test_remove_gallery(self):
        self.IGalleryService.remove_Gallery(GalleryId=1)

    def test_update_gallery(self):
        self.IGalleryService.update_Gallery(
            GalleryID=1,
            name="City Art Gallery ",
            description="A contemporary art space promoting urban art forms",
            location="789 Park Avenue, City",
            curator="Alice Johnson",
            openingHours="Tue-Sun: 11am-8pm",
            ArtistId=2
        )

if __name__ == '__main__':
    unittest.main()