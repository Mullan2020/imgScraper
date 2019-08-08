#image scraper
#check robots.txt b4 using
#2019.08.08

import urllib
import re
from urllib import request


def search_image(url):

	regex='<img src="(.*?)" />' #you can modify and individualize

	cs=urllib.request.urlopen(url).headers.get_content_charset()

	if cs==None:

		cs='utf-8'

	html=urllib.request.urlopen(url).read().decode(cs)

	#print(html[:100])

	image=re.findall(regex,html)

	for i in range(0,len(image)):

		if 'http' not in image[i]:

			image[i]=url+image[i]



	return image

def download(url):

	try: html=urllib.request.urlopen(url).read()

	except (urllib.error.ContentTooShortError, urllib.error.HTTPError, urllib.error.URLError) as e:

		print(e.reason)

		return None

	return html

def image_scrap(url,username): #insert system's user name that your using, for file creation

	image=search_image(url)

	#print(image)

	for i in range(len(image)):

		html=download(image[i])

		if not (html==None):

			f=open('C:\\Users\\{}\\Desktop\\imagescrap\\image{}.png'.format(username,i),'wb')

			f.write(html)

			f.close()

	print("image scrap finished")


url=input("input url that you want scrap: ")
username=input("insert system's user name that your using, for file creation: ")
print("the result will be saved in file 'C:\\Users\\{}\\Desktop\\imagescrap".format(username))
image_scrap(url,username)
