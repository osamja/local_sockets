### Known Bugs
	* Serving file twice causes 'Address already in use' error. 
	* Uploading nothing results in a 'None' upload which changes the URL address.
	* Closing window causes http.run_forever error.  Non-main thread was closed but expected to keep running. 


### IMPROVEMEMENTS
	* Create more user-friendly GUI. ex. (Less buttons, better colors) 
	* fname_nopath = getFileFromPath()  # Parses path name to be only filename. ex: /music/thriller.mp3 -> thriller.mp3
	* Ability to upload multiple files.  Webpage should list all files that can be downloaded. 
	* Make URL highlightable so it can be copy and pasted. 
	* Ability to share URL (IP:Port) link.  

