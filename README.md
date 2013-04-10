# Git-Got
## Synopsis
Tool which provides a simple look aside cache feature for git.  This tool is
meant to use git as a user would which differs from git-annex.  This allows
it to be used without modifying server side implementations for tools like
gitorious.  Currently the only transport supported is scp.

## Basic Usage
To start using Git Got place the accompanying script into your path.  Execute
the following steps inside of an initialized repository.

### To initialize a repository for use with git got
This will initialize the repository structure as well as add and commit
it to the git repository.

    git got init yourusername@yourserver.com:your_storage_location

### To add(or change) a file to/in the got repo
This will upload the file to the remote repository as well as adding and
committing the has file to the repository.  This will also add the hash file as
well as the file being tracked to the gitignore file.

    git got add path/bigfile

### To check the status of tracked files
This will report which files in the repository have been modified.

    git got status

### To remove a file from the repo(Not implemented)
This will remove the current hash file from the repository as well as delete the
stored data in the current git repository.

    git got rm yourfile

### To change to a new remote repo
    git got init yourusername@yournewserver.com:your_new_storage_location
