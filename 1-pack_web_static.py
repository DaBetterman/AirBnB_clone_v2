#!/usr/bin/python3
# A Fabric script that generates a .tgz archive from the contents of
# the web_static folder of your AirBnB Clone repo, using the function do_pack.

from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """
    Generates a tgz archive
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    do_pack()
