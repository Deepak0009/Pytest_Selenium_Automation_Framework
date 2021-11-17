from selenium import webdriver


class Base:
    def __init__(self, driver):
        self.driver = driver

    def verigyTitle(self):
        assert self.driver.title



# git init : create .git directory in project directory

# git clone https://github.com   : clone the repo from remote to local

# git status : displays the state of the working directory and the staging area


#git add : adds your modified files to the queue to be committed later.

#git commit : commits the files that have been added and creates a new revision with a log


#git push : pushes your changes to the remote repository.