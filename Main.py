from time import sleep
import requests
from pytube import YouTube


def GetVid(URL):
    #Downloading the video
    print("Getting the video")
    ObjectData = YouTube(URL)
   # VID = input("Would you like to convert the video to an mp3?\n")
   # if VID == 'YES' or 'yes' or "Yes" or "y" or "Y":
       # ObjectData = ObjectData.streams.get_audio_only()
       # ObjectData.download()
    #elif VID == "no" or "NO" or "No" or "n" or "N":
    print("Downloading...")
    if ObjectData.age_restricted == True:
        print("attempting to bypass age restriction")
        sleep(2)
        try:
            print("if bypass fails we will create a HTML file that can be opened within a browser")
            ObjectData.age_restricted = False
            ObjectData.bypass_age_gate()

            
        except:
            print("failed to bypass. :(\n ")
            sleep(15)
            

    ObjectData = ObjectData.streams.get_highest_resolution()
    print(ObjectData.video_codec)
    try:
        ObjectData.download()
    except:
        print("failed to download the video")
    print("Success!"," Saved in   ",ObjectData.get_file_path(),"\n\n\nURL TO RAW VIDEO:\n\n\n ",ObjectData.url)




   # Convert = requests.get(URL)


URL = input("Please enter the URL of the video you want to get\n")
while(URL == ""):
    URL = input("You did not enter a URL please try again.\n")
#while(not URL.startswith("http://") or not URL.startswith("https://")):
   # input("Not a valid URL try again ")
   # exit("Wrong URL")

GetVid(URL)



