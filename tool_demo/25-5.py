# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import shutil
# import requests



# PATH = "chromedriver.exe"

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(PATH, options=chrome_options)

# url = 'https://www.instagram.com/reel/url/'
# # Open the YouTube video URL in the browser
# driver.get(url)


    

# find = driver.find_element(by= By.XPATH, value= '/html/head/script[3]')
# text = find.get_attribute('innerText')
# driver.close()

# start = text.index('"contentUrl":"')
# end = text.index('","thumbnailUrl"',start+14)
# print(text)
# new_text = text[start+14:end].replace('\/','/')

# print('--------------')
# print(new_text)
# print('hey')
# response = requests.get(new_text,stream=True)
# with open ('output.mp4','wb') as out_file:
#     shutil.copyfileobj(response.raw,out_file)
# del response


from instascrape import Reel
import time

# session id
SESSIONID = "Paste session Id Here"

# Header with session id
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
	Safari/537.36 Edg/79.0.309.43",
	"cookie": f'sessionid={SESSIONID};'
}

# Passing Instagram reel link as argument in Reel Module
insta_reel = Reel(
	'https://instagram.com/stories/meggi.boy/3109930144927852948?igshid=MTc4MmM1YmI2Ng==')

# Using scrape function and passing the headers
insta_reel.scrape(headers=headers)

# Giving path where we want to download reel to the
# download function
insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")

# printing success Message
print('Downloaded Successfully.')






























