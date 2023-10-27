#import youtube_dl
import yt_dlp

def run():
    video_url = input("\n please enter youtube video url: ") 
    video_info = yt_dlp.YoutubeDL().extract_info(
        url = video_url,download=True
    )
    filename = f"{video_info['title']}.mp4"
    options={
        'format':'bestvideo/best',
        'keepvideo':True,
        'outtmpl':filename,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("\n Download complete... {} \n".format(filename))

if __name__=='__main__':
    run()