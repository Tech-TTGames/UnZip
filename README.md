# UnZip
 A Program for automatic unZipping of password protected zips.

# Editing Settings
 To Change Settings edit the config.json file:
  * passwords - A list of passwords to use with the program please separate them with commas.
  ** Example ["testpassword1","TestPassword2"]
  * monipath - The path to the place where the program searches for zip files to unzip
  * destpath - The path to the place where the unzipped contents of the zips are placed
  * mispwdpop - Whether the program should display a pop-up window when theres a zip file with no working password
  * updatetime - How frequently should the program check for new zips (mins)

# Automatic Startup
To make the program auto-start in background on boot:
  * Copy the program - UnZipMain.py
  * Click Win+R
  * Run shell:startup
  * A Windows Explorer window will open - Use right click and "Paste Shortcut"