findivey
========

findivey is a small Python utility that alerts you when your favorite high stakes poker players are playing online.


How frustrating is it to miss an appearance of Tom Dwan ("durrr") or Phil Ivey ("Polarizing") or the prodigy Isildur1 only because you forgot to check the high stakes tables of FullTilt and PokerStars that evening?

With findivey, just save a player's details in a text file (examples are provided) and the program alert you as soon as the player is online! 

findivey works by scanning (every ten minutes) the "online" status of a player as displayed on the player's profile on highstakesdb.com.  Once the player shows up, findivey will alerts you by printing on the command line the player's name and where he is currently playing (FullTilt or PokerStars).

With findivey never miss the big action again !!


To Download the program:

    git clone git@github.com:jule64/findivey.git


To run the program:

    python yourpath/findivey.py

OR

add this line to your .bash/.zsh profile file

	findivey () { python yourpath/findivey }

and just type "findivey" in your command line to run it


Dependencies:

Possible library dependencies include:

	BeautifulSoup ("pip install BeautifulSoup" in your command line to install (unix))


Next steps:

    - play sound when specific player enters online. For example by recording the name of the player and playing that name back when the player is online.
    - add time scan interval option (currently scan every ten minutes)


Here is a little screenshot:

![screenshot](https://raw.github.com/jule64/findivey/master/img/screenshot1.png)



If you would like to contribute please fork this project!


