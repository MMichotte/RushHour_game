from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 2, 'compressed': True}},
    windows = [{
        'script': 'src/main.py',
        "icon_resources": [(1, 'img/rushHour.icns')],
        "dest_base" : "Rush-Hour",
        }],
    zipfile = None,
)