#!/usr/bin/python3
"""
    creates and distributes an archive to your web servers
"""
import os
from fabric.api import local, put, run
from datetime import datetime


def do_pack():
    """
        Creates a tgz archive of the specified directory on the local machine.
    """
    try:
        local("mkdir -p versions")
        date_now = datetime.now()
        _path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
                date_now.year,
                date_now.month,
                date_now.day,
                date_now.hour,
                date_now.minute,
                date_now.second)

        local("tar -cvzf {} web_static/".format(_path))
        return _path
    except Exception:
        return None


def do_deploy(archive_path):
    """
        Distribute archive to server
    """
    if os.path.exists(archive_path):
        archived_file = os.path.basename(archive_path)
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file_tmp = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format
            (archived_file_tmp, newest_version))
        run("sudo rm {}".format(archived_file_tmp))
        run("sudo mv {}/web_static/* {}".format
            (newest_version, newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))
        return True
    return False


def deploy():
    """
        creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
