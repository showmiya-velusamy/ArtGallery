class ArtworkNotFound(Exception):
    def __init__(self, message="Artwork not found."):
        self.message = message
        super().__init__(self.message)