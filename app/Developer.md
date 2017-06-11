### Known Bugs
	* Serving file twice causes 'Address already in use' error. 
	* Uploading nothing results in a 'None' upload which changes the URL address.
	* Closing window causes http.run_forever error.  Non-main thread was closed but expected to keep running. 
	* Show URL only when server is running. exit


### IMPROVEMEMENTS
	* Create more user-friendly GUI. ex. (Less buttons, better colors) 
	* fname_nopath = getFileFromPath()  # Parses path name to be only filename. ex: /music/thriller.mp3 -> thriller.mp3
	* Ability to upload multiple files.  Webpage should list all files that can be downloaded.   [HIGH PRIORITy]
	* Make URL highlightable so it can be copy and pasted. 
	* Ability to share URL (IP:Port) link.  
	* portResolver().  This function would find an open port if 8080 is taken.  
	* Add tests (see below).  
	* Create a better landing page when downloading files.  


### Production
	* Insert BSD/MIT license.  
	* Create executable program.  


### Testing
	* traceroute().  Verify that the packet did only one hop.  Helps to ensure privacy.  

### ** IMMEDIATE DELIVERABLES **
	* Allow multi-file uploads.  