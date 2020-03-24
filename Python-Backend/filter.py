import pymongo
import audio_features

client = pymong.MongoClient(
    "mongodb+srv://<username>:<password>@ramblerpy-5rd9x.mongodb.net/test?retryWrites=true&w=majority")
db  = client["mydatabase"]
mycol = mydb['tracks']

#filters out the data(songs) based on certain criteria
#Having trouble getting this portion to function as intended(Nate)



#filters out all tracks that don't have a dancability attribute more than the number .8
danceable_tracks = db.tracks.find({'danceability': {'$gt': .8}})

#prints out the filtered results
print("Here is a filtered list of the most danceable  tracks: ")
for n in danceable_tracks:
        print(n['track_name'])track
        

#filters out all tracks that don't have a loudness attribute greater than the number .5
loud_tracks = db.tracks.find({'loudness': {'$gt': .5}})

#prints out the filtered results
print("Here is a filtered list of loud tracks: ")
for n in loud_tracks:
        print(n['track_name'])track


#filters out all tracks that don't have a tempo attribute greater than the number .7
fast_tracks = db.tracks.find({'tempo': {'$gt': .7}})

#prints out the filtered results
print("Here is a filtered list of high tempo tracks: ")
for n in fast_tracks:
        print(n['track_name'])track


#filters out all tracks that don't have a tempo attribute less than the number .5
chill_tracks = db.tracks.find({'energy': {'$gt': .5}})

#prints out the filtered results
print("Here is a filtered list of low energy tracks: ")
for n in chill_tracks:
        print(n['track_name'])track



    





    

