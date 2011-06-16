import os
import subprocess
import tempfile
from urllib import urlretrieve
from django.core.management.base import CommandError, NoArgsCommand
import zipfile
import shutil

def grab(src, dest):
    urlretrieve(str(src), str(dest))

def unzip_file(src, dest):
    zip = zipfile.ZipFile(src)
    if not path(dest).exists():
        path(dest).makedirs()
        
    for name in zip.namelist():
        if name.endswith("/"):
            (path(dest) / name).makedirs()
        else:
            parent, file = path(name).splitpath()
            parent = path(dest) / parent
            if parent and not parent.isdir():
                path(parent).makedirs()
            out = open(path(parent) / file, 'wb')
            out.write(zip.read(name))
            out.close()

class Command(NoArgsCommand):
    can_import_settings = True

    def handle_noargs(self, **options):
        """
        Downloads geoserver, geonetwork and geonode-client.zip into a folder called 'downloads'
        in the project root.

        It also unzips the geonode-client.zip in the right directory.
        """
        from django.conf import settings
        PROJECT_HOME = os.path.join(settings.PROJECT_ROOT, '..', '..')
        TOMCAT_HOME = os.path.join(PROJECT_HOME, 'tomcat')
        DOWNLOAD_DIR = os.path.join(PROJECT_HOME, 'downloads')
        MAP_STATIC_DIR = os.path.join(settings.PROJECT_ROOT, 'maps', 'static', 'geonode')

        files = ['geoserver-geonode-dev.war', 'geonetwork.war', 'geonode-client.zip', 'tomcat.zip']
        for file in files:
            url = '%s/%s' % (settings.GEONODE_DEPENDENCIES_URL, file)
            grab(url, os.path.join(DOWNLOAD_DIR, file))
        
        unzip_file(os.path.join(DOWNLOAD_DIR, 'geonode-client.zip'), MAP_STATIC_DIR)
        unzip_file(os.path.join(DOWNLOAD_DIR, 'tomcat.zip'), TOMCAT_HOME)

        for file in ['geoserver-geonode-dev.war', 'geonetwork.war']:
            src = os.path.join(DOWNLOAD_DIR, file)
            dst = os.path.join(TOMCAT_HOME, 'webapps', file)
            shutil.copyfile(src, dst)
