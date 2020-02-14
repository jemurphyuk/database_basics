# Libraries, modules and packages

This repo will explore libraries, modules, packages and python
### Libraries
AKA: python standard libraries (such as datetime)! These come out of the box with python and are maintained by python organisation. Just need to install

### Modules
- A piece of software that delivers useful functionality.
- We have created some of these before, both functional and OOP.
    - A functional OOP calculator
    
### Packages & PIP
- A package manager installs software and it's dependencies
- PIP is a python package manager
- Package Managers - exist for almost every modern coding language. Operating systems have package managers:
    - windows - chocolaty and others
    - ubuntu - apt-get
    - mac-os - brew
### Git branching and work flows

#####1) Ensure master is always up to date
````
    $ git pull origin master
````
#####2) Create a new branch
````buildoutcfg
    $ git checkout -b <name>
````
#####3) add and commit changes

#####4) move between existing branches
````buildoutcfg
    $ git checkout <branch>
````
#####5) push current branch to the remote
````
    $ git push origin <name_of_branch>
````
#####6) merge branch with master on github

#####7) checkout to master and pull latest 

###Important notes
- changes will travel with you if you don't commit them
- must commit all changes before switching branches

### Merging branch with master
- ensure all things have been committed
- pull request on github
- merge pull request to realign with master
- return to master
    - git checkout master
    - git pull origin master to pull master from github to own git-bash

### Resolving conflicts
- look at code and edit, duplicates will be shown for you to edit
- can pull conflict onto your computer to run and test
- mark as resolved
- commit merge and confirm merging branch

## JSON
 - Connect to a server which sends back HTML, CSS, Headers, JavaScript
 - A get request 
    - sending headers (meta information; data about the data such as browser and device of search)
    - parameters (chopped up data to send to site)
    - URL (www.), 
 - A post request
    - all of the above +JSON
    - the json is not visible (by protocols) and will look like a dictionary {}
    - {'name': 'Geoff', 'card': '134352...'}
 - An Application Programming Interface will work with a JSON to work with data sent from a get request
