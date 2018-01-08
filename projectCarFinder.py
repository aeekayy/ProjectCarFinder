#!/usr/bin/python

from bs4 import BeautifulSoup # For BeautifulSoup and HTML parser
import re
import urllib2 # for urlopen

# Default stuff for this module
TAG_RE = re.compile('<.*?>')

def main(): 
	print "Project Car Finder"
	testUrl = ""
	print extractFromURL(testUrl)

def remove_tags(text):
	cleantext = TAG_RE.sub('', text)
	return cleantext

def getHTML(url): 
	# Open the url into a variable
	singlePage = urllib2.urlopen(url.strip())
	singleLines = []

	# Iterate through the lines and return the page
	for line in singlePage.readlines():
		singleLines.append(line)
	
	# Return that string
	return '\n'.join(singleLines)

def extractFromURL(url):
	# Return the HTML
	soup = BeautifulSoup(getHTML(url), 'html.parser')
	title_tag = soup.find("span", { "id" : "titletextonly"})
	price_tag = soup.find("span", { "class": "price" })
	body_tag = soup.find("section", { "id": "postingbody"})
	print remove_tags(title_tag)
	print price_tag
	print body_tag
	

# run the main function
main()
