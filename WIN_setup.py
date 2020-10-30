from distutils.core import setup
import py2exe, sys, os

APP = ['src/main.py']
DATA_FILES = []
OPTIONS = {
    'iconfile':'img/rushHour.icns',
}

setup(
    app=APP,
    name="Rush-Hour",
    data_files=DATA_FILES,
    options={'py2exe': OPTIONS},
    setup_requires=['py2exe'],
)

"""
sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    windows = [{'script': "single.py"}],
    zipfile = None,
)
"""