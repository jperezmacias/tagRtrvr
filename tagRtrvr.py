''' Programmed by Jose M. Perez-Macias
	May 29th 2014 
	Version 29.05.2014

	Functions for main_tagRtrvr.py
	------------------------------------

	get_html(url)
	def get_xml_tags(xhtml,tag):
	def download_img(img_url):
	def save_img(prefix,url,folder):
	save_img_array(img_list,url,folder_name):


'''


from xml.dom import minidom
import urllib
import os, os.path
import sys
#import datetime
from time import gmtime, strftime


# This function gets the URL
def get_html(url):

	headers = {'User-Agent' : 'Mozilla 5.10'}
	#response = urllib.urlopen(url,None,headers)
	
	try:
		response = urllib.urlopen(url,None,headers)
	except Exception as e:
		print 'Could not open URL'
		print e
	else:
		# Response code we expect is 200, check RFC's for others
		# http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
		code = response.code
		html = response.read()
		return html, code

# This function gets the tags in an array
def get_xml_tags(xhtml,tag):
	
	#xmldoc = minidom.parse('binary.xml') # This is for files
	try:
		xmldoc = minidom.parseString(xhtml)
	except Exception as e:
		print "Could not retrieve xhtml, are you sure is XHTML?"
		print e
	else:
		itemlist = xmldoc.getElementsByTagName('img')
		return itemlist

# This function downloads the image
# It is called from save
def download_img(img_url):
	img = urllib.urlopen(img_url)
	code = img.code
	data = img.read()
	return data, code
	

# This function	gets the URI of the image and saves it in a folder
# defined by 'folder'. If this folder does not exist, it creates it.
def save_img(prefix,url,folder):

	# I check if the folder exsists and if not I create it
	# http://www.java2s.com/Tutorial/Python/0420__Network/RetrievingImagesfromHTMLDocuments.htm
	if not os.path.exists(folder):
		os.makedirs(folder)
	
	#I download the imgage
	data, code = download_img(url)
	#print " Download image code " + str(code) 

	# Save the image
	splitPath = url.split('/')
	image_name = splitPath.pop()
	#print fName
	# os.getcwd() # To get the base path
	full_path = folder + str(prefix) + '_' + image_name
	
	# Save the imgage in the specificed
	f = open(full_path, 'wb')
	f.write(data)
	f.close()

def save_img_array(img_list,url,folder_name):
	
	for idx, img_tag in enumerate(img_list):
			# i is the image_tag, and idx is the index
			print idx+1
			# Structure of the array is : img_list[0].attributes['name'].value
			#print i.attributes['src'].value
			#print url[:-1] + i.attributes['src'].value # I join, but also have to remove the last slash from the base url
			
			
			img_url = url + img_tag.attributes['src'].value[2:];
			
			# We save the images
			#def save_img(prefix, url,folder):
			save_img(idx,img_url,folder_name)

def download_images_xhtml_url(url):


	### SETTINGS
	tag ='img'
#	url='http://xhtml.com/en/xhtml/reference/base/'

	folder_name = tag +'/' + str(strftime("%Y_%m_%d_%H_%M_%S", gmtime())) + '/'
	
	
	
	# I get the xml file
	# def get_html(url):
	xhtml, cod = get_html(url)
	#print html # Testing if if returns a HTML output
	# Print the response code (It should be 200)
	print 'HTTP response code ' + str(cod)
	
	# We check everything is ok	
	if (get_html(url)[1] == 200 ):
		print "We got a response from the remote server"
	else:
		print "We are in trouble"
	
	# Retrieve the selected tab
	img_list = get_xml_tags(xhtml,tag)
	


	print 'Number of images ' + str(len(img_list))
	save_img_array(img_list,url,folder_name)


