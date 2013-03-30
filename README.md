# Git-Got
## Synopsis
Tool which provides a simple look aside cache feature for git.  This tool is
meant to use git as a user would which differs from git-annex.  This allows
it to be used without modifying server side implementations for tools like
gitorious.  Currently the only transport supported is scp.
## Basic Usage
To strt using Git Got place the accompanyng script into your path.  Execute
the following steps inside of an initialized repository.

### To initialize a repository for use with git got
    git got init yourname@yourserver.com:your_storage_location
### To add a file to the got repo
    git got add path/bigfile
### To check the status of tracked files
    git got status
### To remove a file from the repo
    Not implemented
