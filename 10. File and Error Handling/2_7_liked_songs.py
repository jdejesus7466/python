def write_liked_songs_to_file(liked_songs, file_name):
    file = open(file_name, 'w')

    file.write("Liked Songs\n\n")

    for song, artist in liked_songs.items():
        file.write(f"{song} by {artist}\n")

    file.close()

if __name__ == "__main__":

    liked_songs = {
        'sucker' : 'jonas brothers',
        'nissan altima' : 'doechii',
        'bakamitai' : 'kazuma kiryu',
        'espresso' : 'sabrina carpenter'
    }

    write_liked_songs_to_file(liked_songs, "filename.txt")