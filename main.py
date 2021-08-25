#import the package
from pytube import YouTube

url="https://www.youtube.com/watch?v=W-w3WfgpcGg&list=RDW-w3WfgpcGg&start_radio=1"
my_video=YouTube(url)

print("*****************************Video Title************************")
#get video Title
print(my_video.title)

print("***********set up resolution************")
my_video= my_video.streams.get_highest_resolution()
my_video.download()