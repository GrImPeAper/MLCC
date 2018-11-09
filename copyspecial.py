#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""
def get_special_paths(fromdir):
	all_files=[]
	all_files=os.listdir(fromdir)
	paths=[]
	for name in all_files:
		if re.search(r'__\w+__', name):
			paths.append(os.path.join(os.path.abspath(fromdir),name))
	paths_print='\n'.join(paths)
	print (paths_print)
	return paths

def copy_to(paths,dir):
	new_loc=[]
	print (paths)
	if not os.path.exists(dir):
		os.mkdir(dir)
	for file in paths:
		shutil.move(file,dir)
		print(file + ' moved to ' + dir)
	print('Moving done')
	new_paths=os.listdir(dir)
	print (new_paths)
	for files in new_paths:
		new_loc.append(os.path.join(os.path.abspath(dir),files))
	#print (new_loc)
	#paths=' '.join(new_loc)
	#print (paths)
	
	
def zip_to(paths,zippath):
	paths=copy_to(paths,zippath)
	command='CScript  zip.vbs '+ zippath +'\\' +' '+ zippath +'.zip'
	os.system(command)		
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
	args = sys.argv[1:]
	if not args:
		print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
		sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
	todir = ''
	if args[0] == '--todir':
		todir = args[1]
		del args[0:2]

	tozip = ''
	if args[0] == '--tozip':
		tozip = args[1]
		del args[0:2]

	if len(args) == 0:
		print("error: must specify one or more dirs")
		sys.exit(1)
  
  # +++your code here+++
  # Call your functions
	for direc in args:
		paths=get_special_paths(direc)
	if todir:
		copy_to(paths,todir)
	elif tozip:
		zip_to(paths,tozip)
  
if __name__ == "__main__":
  main()