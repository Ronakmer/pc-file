
#**************************** text to speeach  ****************************

# from gtts import gTTS

# import os

# mytext = 'Welcome to Welcome to Welcome to Welcome to Welcome to toolssssssss!'

# language = 'en'

# myobj = gTTS(text=mytext, lang=language, slow=False)

# myobj.save("welcome.mp3")

# os.system("mpg321 welcome.mp3")






# #****************************  this is a video + audio #****************************

from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import os


title = input("Enter a title: ")

video_clip = VideoFileClip("de.mp4")
audio_clip = AudioFileClip("welcome.mp3")


final_clip = video_clip.set_audio(audio_clip)




final_clip.write_videofile(title + ".mp4")																			
