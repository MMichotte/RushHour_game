from setuptools import setup

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
