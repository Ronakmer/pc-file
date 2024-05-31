# # Importing libraries
# import bs4 as bs
# import sys
# import urllib.request
# from PyQt5.QtWebEngineWidgets import QWebEnginePage
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import QUrl
# import pytube # library for downloading youtube videos


# class Page(QWebEnginePage):
# 	def __init__(self, url):
# 		self.app = QApplication(sys.argv)
# 		QWebEnginePage.__init__(self)
# 		self.html = ''
# 		self.loadFinished.connect(self._on_load_finished)
# 		self.load(QUrl(url))
# 		self.app.exec_()

# 	def _on_load_finished(self):
# 		self.html = self.toHtml(self.Callable)
# 		print('Load finished')

# 	def Callable(self, html_str):
# 		self.html = html_str
# 		self.app.quit()


# links = []


# def exact_link(link):
# 	vid_id = link.split('=')
# 	# print(vid_id)
# 	str = ""
# 	for i in vid_id[0:2]:
# 		str += i + "="

# 	str_new = str[0:len(str) - 1]
# 	index = str_new.find("&")

# 	new_link = "https://www.youtube.com" + str_new[0:index]
# 	return new_link


# url = "https://www.youtube.com/watch?v=lcJzw0JGfeE&list=PLqM7alHXFySENpNgw27MzGxLzNJuC_Kdj"
# # Scraping and extracting the video
# # links from the given playlist url
# page = Page(url)
# count = 0

# soup = bs.BeautifulSoup(page.html, 'html.parser')
# for link in soup.find_all('a', id='thumbnail'):

# 	# not using first link because it is
# 	# playlist link not particular video link
# 	if count == 0:
# 		count += 1
# 		continue
# 	else:
# 		try:
# 			# Prevents error for links with no href.
# 			vid_src = link['href']
# 			# print(vid_src)
# 			# keeping the format of link to be
# 			# given to pytube otherwise in some cases
# 			new_link = exact_link(vid_src)

# 			# error might occur due to this
# 			# print(new_link)

# 			# appending the link to the links array
# 			links.append(new_link)
# 		except Exception as exp:
# 			pass # No function necessary for invalid <a> tags.

# # print(links)

# # downloading each video from
# # the link in the links array
# for link in links:
# 	yt = pytube.YouTube(link)

# 	# Downloaded video will be the best quality video
# 	stream = yt.streams.filter(progressive=True,
# 							file_extension='mp4').order_by(
# 		'resolution').desc().first()
# 	try:
# 		stream.download()
# 		# printing the links downloaded
# 		print("Downloaded: ", link)
# 	except:
# 		print('Some error in downloading: ', link)











# import re
# from pytube import Playlist

# YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
# DOWNLOAD_DIR = 'D:\\Users\\Jean-Pierre\\Downloads'

# playlist = Playlist('https://www.youtube.com/watch?v=lcJzw0JGfeE&list=PLqM7alHXFySENpNgw27MzGxLzNJuC_Kdj')

# # this fixes the empty playlist.videos list
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# print(len(playlist.video_urls))

# for url in playlist.video_urls:
#     print(url)

# # physically downloading the audio track
# for video in playlist.videos:
#     audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
#     audioStream.download(output_path=DOWNLOAD_DIR)











# https://www.youtube.com/watch?v=lcJzw0JGfeE&list=PLqM7alHXFySENpNgw27MzGxLzNJuC_Kdj











# from pytube import Playlist, YouTube

# # URL of the YouTube playlist you want to download
# playlist_url = 'https://www.youtube.com/watch?v=lcJzw0JGfeE&list=PLqM7alHXFySENpNgw27MzGxLzNJuC_Kdj'

# # Create a Playlist object
# playlist = Playlist(playlist_url)

# # Loop through each video in the playlist
# for video in playlist.video_urls:
#     try:
#         # Create a YouTube object for each video URL
#         yt = YouTube(video)
        
#         # Download the highest resolution available
#         stream = yt.streams.get_highest_resolution()
        
#         # Download the video
#         stream.download(output_path='YOUR_DOWNLOAD_PATH')
        
#         print(f"Downloaded: {yt.title}")
#     except Exception as e:
#         print(f"Error downloading {video}: {e}")





















from pytube import Playlist, YouTube

def download_video(video_url, output_path, format_choice='mp4', quality='highest'):
    try:
        # Create a YouTube object for the video URL
        yt = YouTube(video_url)
        
        if format_choice == 'mp4':
            if quality == 'highest':
                # Download the highest resolution MP4 stream
                stream = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
            else:
                # Download the selected quality MP4 stream
                stream = yt.streams.filter(file_extension='mp4', res=quality).first()
        elif format_choice == 'mp3':
            # Download the audio stream in MP3 format
            stream = yt.streams.filter(only_audio=True).first()
        else:
            print("Invalid format choice. Please choose 'mp4' or 'mp3'.")
            return
        
        # Download the video/audio
        stream.download(output_path=output_path)
        
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Error downloading {video_url}: {e}")

# URL of the YouTube playlist you want to download
playlist_url = 'https://www.youtube.com/watch?v=lcJzw0JGfeE&list=PLqM7alHXFySENpNgw27MzGxLzNJuC_Kdj'

# Create a Playlist object
playlist = Playlist(playlist_url)

# User input for format choice and quality
format_choice = input("Enter format choice (mp4/mp3): ")
quality = input("Enter quality (highest or specific resolution): ")

# Loop through each video in the playlist
for video in playlist.video_urls:
    download_video(video, 'YOUR_DOWNLOAD_PATH', format_choice, quality)



