import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
name = 'pdfparse',
packages = ['pdfparse'], # this must be the same as the name above
version = '1.3',
description = 'to parse pdf and search for malicious file',
author = 'boddu',
author_email = 'b.manu199@icloud.com',
url = 'https://github.com/boddumanohar/pdfparse', # use the URL to the github repo
download_url = 'https://github.com/boddumanohar/pdfparse/archive/0.1.tar.gz', # I'll explain this in a second
keywords = ['viruspdf', 'malicious', 'pdfparse'], # arbitrary keywords
classifiers = [],
include_package_data = True,
entry_points={
		'console_scripts': [
			'pdfparse = pdfparse.pdfparse:run',
		],
	}
)
