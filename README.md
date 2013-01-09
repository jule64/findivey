findivey
========

findivey is a small Python utility that alerts you when your favorite high stakes poker players are playing online.
findivey works by scraping a player's online status info displayed on highstakesdb.com (shhhhh! don't tell them!) and display the player's name and other infos to the command line



!! Download findivey and never miss the big online poker action anymore !!




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


If you would like to contribute please fork this project!



