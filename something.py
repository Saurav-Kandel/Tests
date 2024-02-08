""" Question 1:
You are tasked to help an analytics team understand which tracks are the most talkedabout tracks in a list of online reviews. Write an algorithm that, given a list of N reviews, will
return a list of names of the most talked-about tracks.
The task in this test is purposefully kept simple to allow you to pay special attention to writing
production-ready pythonic code that is fully covered under unit high quality tests.
Method signature
def get_popular_tracks(reviews: List[str], track_names: List[str], num_tracks: int) -> List[str]:
“””
reviews: a list of space-separated words representing the track reviews
track_names: a list of track names to be found in the reviews
num_tracks: the number of track names that should be returned
“””
Output
Return a list of the N most talked about tracks in order of most to least mentioned.
Note
The comparison of strings is not case sensitive.
If the tracks are mentioned an equal amount of times then sort them in reverse alphabetical
order.
Example:
Input
reviews = [“I enjoyed the introduction”, “I liked the vacation track but gratitude was my favourite”,
“my friend recommended the password but I prefer gratitude”]
track_names = [“Gratitude”, “Introduction”, “The Password”, “Vacation”]
num_tracks = 3
Expected output
['Gratitude', 'Vacation', 'The Password']
"""
from typing import List

reviews = ["I enjoyed the introduction", "I liked the vacation track but gratitude was my favourite","my friend recommended the password but I prefer gratitude"]
track_names = ["Gratitude", "Introduction", "The Password", "Vacation"]
num_tracks = 3


def get_popular_tracks(reviews: List[str], track_names: List[str], num_tracks: int) -> List[str]:
    # Method 1
    # dic = {}
    # for track in track_names:
    #     count = 0
    #     for review in reviews:
    #         if track.lower() in review:
    #             count += 1
    #     dic[track] = count

    # Method 2
    dic = {}
    combined_reviews = " ".join([review for review in reviews])
    for track in track_names:
        dic[track] = combined_reviews.lower().count(track.lower())
    

    sorted_tracks = sorted(dic, key=lambda x: (dic[x], x), reverse=True)
    return sorted_tracks[0: num_tracks]


print(get_popular_tracks(reviews, track_names, num_tracks))


