''' Programmed by Jose M. Perez-Macias
	May 29th 2014
	Version 29.05.2014

	Retrieves images and downloads them to a folder with the current timestamp. The images
	are scanned from a URI (XML)

	Imports the module called tagRtrvr

'''

from tagRtrvr import *



####### MAIN ###########

def main():
	

	### SETTINGS
	tag ='img'
	url = 'http://www.w3.org/'
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

	
main()


	# Trash
	#raw_input("Press enter to continue")


