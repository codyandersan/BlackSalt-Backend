from pytube import Search
from pprint import pprint
def search_youtube(query):
    s = Search(query)
    return [
        {
            "title": v.title,
            "author": v.author,
            "watch_url": v.watch_url,
            "thumbnail_url": v.thumbnail_url,
            "duration": f"{int(v.length//60):02d}:{int(v.length%60):02d}",

            "views": f"{round(v.views/1000000, 1)}M" if v.views > 999999 else f"{round(v.views/1000, 1)}K" if v.views > 999 else f"{v.views} views",


        }
        for v in s.results
    ]

if __name__ == "__main__":
    pprint(search_youtube(input("Enter query:   ")))
