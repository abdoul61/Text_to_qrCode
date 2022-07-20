
# This code is a helper to download youtube video just with the link and save it into your computer 
# First install pytube with pip3



from pytube import YouTube 



#Prompt the user to send the videa link to be download 
link = input("Enter the link of youtube video you'll like to download : ")

# Next launch the video into browser then stream it and download the first
YouTube(link).streams.first().download()

# Create an instance of that video
yt = YouTube(link)


yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


print("Downloaded", link)





