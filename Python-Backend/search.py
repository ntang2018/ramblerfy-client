import json
import pprint
import re

# returns a the string used for fetching json for a song
# Gets the top search result for a track, artist, album, or playlist
import audio_features


def main(sp, search_string, search_type):
    # returns top result for given song title
    if str(search_type).upper() == "SONG":
        data = sp.search(search_string, limit=5, offset=0, type='track', market='US')
        tracks = data["tracks"]["items"]
        pprint.pprint("Searching for " + search_string + "...")
        # with open(search_string + '.json', 'w') as file_out:
        #     json.dump(tracks, file_out, indent=4, sort_keys=True)
        api_key = tracks[0]["uri"]
        audio_features.main(sp, api_key)
    # returns top 25 tracks for given artist (top results generated by spotify)
    if str(search_type).upper() == "ARTIST":
        data = sp.search(q='artist:' + '"' + search_string + '"', limit=50, offset=0, type='track', market='US')
        tracks = data["tracks"]["items"]
        pprint.pprint("Searching for " + search_string + "...")
        print(json.dumps(tracks, indent=4, sort_keys=True))
        for track in tracks:
            api_key = track["uri"]
            audio_features.main(sp, api_key)
    # returns top 25 tracks for given album (top results generated by spotify)
    if str(search_type).upper() == "ALBUM":
        data = sp.search(q='album:' + '"' + search_string + '"', limit=25, offset=0, type='track', market='US')
        tracks = data["tracks"]["items"]
        pprint.pprint("Searching for " + search_string + "...")
        print(json.dumps(tracks, indent=4, sort_keys=True))
        for track in tracks:
            api_key = track["uri"]
            audio_features.main(sp, api_key)
    if str(search_type).upper() == "PLAYLIST":
        data = sp.search(q='playlist:' + '"' + search_string + '"', limit=50, offset=0, type='track', market='US')
        tracks = data["tracks"]["items"]
        pprint.pprint("Searching for " + search_string + "...")
        print(json.dumps(tracks, indent=4, sort_keys=True))
        for track in tracks:
            api_key = track["uri"]
            audio_features.main(sp, api_key)
