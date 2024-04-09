#!/usr/bin/python3
"""
    script distributes archive to web servers
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
        archive_file = archive_path.split('/')[-1][:-4]
        uncomp_fname = "/data/web_static/releases/" + archive_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(uncomp_fname))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            archive_file, uncomp_fname))
        run("sudo rm {}".format(archive_path))
        run("sudo rm -rf /data/web_static/current")
        run('sudo mv {}/web_static/* {}/'.format(uncomp_fname, uncomp_fname))
        run('rm -rf {}/web_static'.format(uncomp_fname))
        run("sudo ln -sf {} /data/web_static/current".format(uncomp_fname))
        return True
    return False
