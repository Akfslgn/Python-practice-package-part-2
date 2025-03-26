# do not change the method name
def main():
    # Welcome message and empty playlist
    print("Welcome to Playlist Manager!\n")
    playlist = []
    print(f"Current playlist: {playlist}\n")

    # Adding songs to the playlist
    songs_to_add = [
        ("Bohemian Rhapsody", "Queen"),
        ("Hotel California", "Eagles"),
        ("Sweet Child O'Mine", "Guns N'Roses"),
        ("Billie Jean", "Michael Jackson"),
        ("Stairway to Heaven", "Led Zeppelin")
    ]

    for title, artist in songs_to_add:
        song = f"{title} - {artist}"
        print(f'Adding: "{title}" by {artist}')
        playlist.append(song)
        print(f"Current playlist: {playlist}\n")

    # Display the most recently added songs (last 3 songs)
    print(f"Recently added songs (last 3): {playlist[-3:]}\n")

    # Display the first and last songs in the playlist
    print(f"First song: {playlist[0]}")
    print(f"Last song: {playlist[-1]}\n")

    # Remove "Hotel California" from the playlist
    print('Removing: "Hotel California" by Eagles')
    playlist.remove("Hotel California - Eagles")
    print(f"Current playlist: {playlist}\n")

    # Create a "top songs" list containing the first 2 songs from the updated playlist
    top_songs = playlist[:2]
    print(f"Top songs list: {top_songs}")


# do not change the following lines:
main()
