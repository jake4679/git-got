# Git-Got
## Synopsis
Git-got is a tool which provides a simple look aside cache feature for git.
This tool is meant to use git as a user would which differs from git-annex.
This allows it to be used without modifying server side implementations for
tools like gitorious.  Currently the supported transports are scp, file, and srr
(a type of multi-part encoded http server).

## Installation

In order to install you need to install a few dependencies first, we provide
`requirements.txt` file which is compatible with pip to install the dependencies
for you. It's recommended you install this into your user environment by
running:

    pip install -r requirements.txt

The whole list may not be complete, we only tested it on OSX 10.11.4 running
Python 2.7.11 provided by **brew**.

Once you have your dependencies installed you need to add `src/git-got` to your
a place available through your `$PATH` environment variable.

## Basic Usage
To start using Git Got place the accompanying script into your path.  Execute
the following steps inside of an initialized repository.

### To initialize a repository for use with git got
This will initialize the repository structure as well as add it to the git
repository.

    git got init scp ssh://yourusername@yourserver.com:your_storage_location

### To add(or change) a file to/in the got repo
This will upload the file to the remote repository as well as adding the
tracking hash file to the repository.  This will also add the file being
tracked to the gitignore file.

    git got add path/bigfile

### To retrieve all files for an existing repository
This will iterate over all .got files in the repository and pull down their
contents.  Currently it does not verify if any local changes have been made.

    git got get

### To check the status of tracked files
This will report which files in the repository have been modified.

    git got status

### To remove a file from the repo
This will remove the current hash file from the repository as well as remove
the entry in the gitignore file.  It will *not* remove the file contents from
the remote.

    git got rm yourfile
