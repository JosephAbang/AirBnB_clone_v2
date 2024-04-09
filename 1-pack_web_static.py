#!/usr/bin/python3
"""
    script generates a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
        Creates a tgz archive of the specified directory on the local machine.
    """
    try:
        local("mkdir -p versions")
        date_now = datetime.now()
        archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
                date_now.year,
                date_now.month,
                date_now.day,
                date_now.hour,
                date_now.minute,
                date_now.second)

        local("tar -cvzf {} web_static/".format(archive_path))
        return archive_path
    except Exception:
        return None
