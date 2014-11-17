#GetLyrics
Search lyricwiki and add lyrics to iTunes track metadata

Simple applescript that processes selected tracks in iTunes and searches lyricwiki 
for lyrics. If a match is found, the lyrics are added to the track metadata.

The applescript executes a python package (not written by me) called songtext found here:
https://pypi.python.org/pypi/songtext

The package has been (inelegantly) customized to deal with various unicode issues that arise
when executing through applescript.

Usage:
The repository includes the modified python package and the applescript file. 
Open the applescript file using Script Editor and change the path to the songtext executable. 
This is found at or near line 59.  The default path is ~/bin/getlyrics/songtext/songtext.

The script can be run from the Script Editor by highlighting one or more tracks in iTunes
and clicking the run button.  

The script can also be saved as an Automator workflow so it can be executed from the 
Services menu in iTunes or via keyboard shortcut 

##TODO
* Understand why Unicode errors are raised when called from applescript but not when
run from terminal

##CHANGELOG

###Version 1.2
11/17/2014

* Add bad_char_replace module to address Unicode exceptions caused by umlauts in band
names (Motörhead, Queensrÿche, etc...)

###Version 1.1
10/20/2014

* Add desktop log file and dialog with result summmary counts
* Add try/except block to Lyricwiki.py module to prevent failures due to Unicode errors

###Version 1.0
10/10/2014

* First functional version





