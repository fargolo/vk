# README 

Demo protype for cross-platform application developed in the 1st year of my Ph.D. It runs on kivy(Linux, Windows, OS X, Android, iOS).  

This is the vk application for assessment of speech measures. Current text data was taken from TED talks transcripts.  
Current version supports two measures: emanctic coherence (Through LSA) and phoneme similarity([Eric Malmi repo](https://github.com/ekQ/raplysaattori)).

The project is currently on hold.

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies: Python 2.7; kivy 1.9.1; R package LSAfun; raplyzer (available on git;requires eSpeaker)
* Database configuration: download semantic space EN_100k (http://www.lingexp.uni-tuebingen.de/z2/LSAspaces/) to "~/LSASpace/EN_100k.rda"
* Deployment instructions: run "python2.7 main.py"


### Issues
I stopped while solving remote transfering of files from client to server. I might eventually go back to rewrite it with a better server interface (RESTful?). 

### Contact info

* E-mail: felipe.c.argolo () protonmail.com
