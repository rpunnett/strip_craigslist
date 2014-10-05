from bs4 import BeautifulSoup
import urllib2

##Filename: strip_cl.py
##Function: Grabs relevant info from a CL post

url = 'https://atlanta.craigslist.org/nat/cto/4607332736.html'#Url to grab
page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page)
title = soup.title
postTitle = soup.body.h2  #Grab the posts title (Page Title)
postingtitle = soup.find('h2', {"class" : "postingtitle"});  #Grab the title of the post
postingbody = soup.find('section', {"id" : "postingbody"});  #Grab the body of the post
postData = soup.find_all('p', {"class" : "postinginfo"}); #Grab assorted post info //To be sectioned out

imgs = [x['src'] for x in soup.findAll('img')] # Grab attached images //To be further formatted and split, regex to large images

fo = open("output.txt", "w")
fo.write('Posting Title: ');
fo.write(str(soup.title.contents[0].strip()));
fo.write('\nPage Header: ');
fo.write(str(postingtitle.contents[2].strip()));
fo.write('\nPost Body: ');
fo.write(str(postingbody.contents[0].strip()));
fo.write('\nImages: ');
for item in imgs:
    fo.write(str(item));
    fo.write('\n '); 
fo.write('\nPost Info: ');
for item in postData:
    fo.write(str(item));
    fo.write('\n ');
fo.close()
#print(soup)

