import pytube

link = input('Enter the video link: ')

yt = pytube.YouTube(link)
videos = yt.streams.all()

s=1
for v in videos:
    print(str(s)+'. '+str(v))
    s+=1

n = int(input("Enter the number of the video: "))
vid = videos[n-1]

destination = input("Enter the destination:   ")
vid.download(destination)

print("Video has been succesfully downloaded!")