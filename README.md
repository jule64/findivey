findivey 
========

A small Python utility that informs you when your favorite high stakes poker players are playing online. 

**Now includes notifications directly on your screen (see screenshot below)!*** 



A short intro
----
How frustrating is it to miss an appearance of Tom "durrr" Dwan or Viktor "Isildur1" Blom, two of the most exciting players in the game, only because you forgot to log in to your poker software that evening?

With findivey, just save your favorite player's details in a text file (well actually in the script itself in the current version) and the program alerts you as soon as the player appears on the poker tables!

findivey works by scanning every ten minutes a player's online status as displayed on the player's profile on highstakesdb.com.  Once the player shows up findivey prints to the command line the player's name and where he is currently playing (see screenshot at the bottom for an example).


**With findivey never miss the big poker action again !!**


Installation guidelines
----

Command line:

    git clone git@github.com:jule64/findivey.git


To run the program:

    python your/path/to/findivey/findivey.py

or just add this line to your .bash/.zsh profile file

	findivey () { your/path/to/findivey/findivey.py }

and just type "findivey" in your command line to run it


Dependencies
----

- BeautifulSoup: to install type "pip install BeautifulSoup" in your command line

Note: this project includes [netgrowl.py](https://github.com/timc3/netgrowl) which it uses to send update notifications to growl.  This library was developed by Tim Child \([@timc3](https://github.com/timc3)\), full credit to him.


Next steps
----
- play sound when a player enters online. For example by recording the name of the player and playing that name back when the player is online.
- add time scan interval option (currently scan every ten minutes)


Some screenshots
----

**Growl-enabled notifications**

![screenshot](https://raw.github.com/jule64/findivey/master/img/growl1.png)

**Terminal notifications**

![screenshot](https://raw.github.com/jule64/findivey/master/img/screenshot1.png)



If you would like to contribute please fork this project!

Check the official project page [here](http://jule64.github.com/findivey/)


\* This feature needs Growl notifications installed
