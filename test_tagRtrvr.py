'''
	Tests for module tagRtrvr.py
	
	Author: Jose M. Perez-Macias
	Data: 29.05.2014

'''

import unittest
from tagRtrvr import *
import os, os.path # To count the number of files


#The following is the class in which all functions will be ran by the unittest
class AsignmentTest(unittest.TestCase):
	
	# The function "setUp" will always be ran in order to setup the test environment before all the test have run.
	def setUp(self):
		'''Verify environment is setup properly''' # Printed if test fails
		pass
		
	# The function "tearDown" will always be ran in order to cleanup the test environment after all the tests have run.
	def tearDown(self):
		'''Verify environment is tore down properly''' # Printed if test tails
		pass
		
	def test_get_html(self):
		'''Verify that the url is valid''' #Printed if test fails
		self.assertEqual(get_html('http://www.w3.org/')[1], 200)
		self.assertEqual(get_html('http://www.google.com')[1], 200)
		
	def test_get_html_exc(self):
		# assertRaises(excClass, callableObj) protoype
		self.assertRaises(TypeError, get_html('http://www.w3.org/'))
		
	def test_get_xml_tags(self):
		get_xml_tags(get_html('http://www.w3.org/')[0],'img')
		
	def test_download_img(self):
		download_img('http://www.google.com/images/srpr/logo11w.png')
	
	def test_save_img(self):
		folder = '_test_output/'
		img_url = 'http://www.google.com/images/srpr/logo11w.png'
		save_img(1,img_url,folder)
		
	def test_save_img_array(self):
		
		tag ='img'
		url = 'http://www.w3.org/'
		xhtml, cod = get_html(url)
		folder_name = tag +'/' + str(strftime("%Y_%m_%d_%H_%M_%S", gmtime())) + '/'
		img_list = get_xml_tags(xhtml,tag)
		save_img_array(img_list,url,folder_name)


	def test_found_and_download(self):
		# Test if the number of images downloaded and expected are the same
		
		# check number of img
		tag ='img'
		url = 'http://www.w3.org/'
		xhtml, cod = get_html(url)
		folder_name = tag +'/' + str(strftime("%Y_%m_%d_%H_%M_%S", gmtime())) + '/'
		img_list = get_xml_tags(xhtml,tag)
		number_expected=len(img_list)

		# check number of downloaded images
		save_img_array(img_list,url,folder_name)
		number_found = len([item for item in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, item))])
		self.assertEqual(number_expected, number_found)
		
if __name__ == '__main__':
	unittest.main()