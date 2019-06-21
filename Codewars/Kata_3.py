str_ing = "AWUBWUBWUBBWUBWUBWUBC"
def song_decoder(song):
    l = song.split("WUB")
    l = list(filter(None, l))
    return ' '.join(l)
#return " ".join(song.replace('WUB', ' ').split())