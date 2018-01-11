def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    return album_dict

album = make_album('kiss', 'love gun')
print(album)

album = make_album('bob seger', 'understanding')
print(album)

album = make_album('peter criss', 'beth')
print(album)

