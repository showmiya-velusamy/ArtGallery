class ArtWorkNotFoundException(Exception):
    def __init__(self, artwork_id):
        super().__init__(f"Artwork with ID {artwork_id} not found.")