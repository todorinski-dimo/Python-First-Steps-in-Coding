from project.album import Album


class Band:

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        found_album = next((a for a in self.albums if a.name == album_name), None)
        if found_album:
            if found_album.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(found_album)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        return f"Band {self.name}\n" + "\n".join(f"{a.details()}" for a in self.albums)
