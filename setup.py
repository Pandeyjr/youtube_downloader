# setup.py
from setuptools import setup, find_packages

setup(
    name="youtube_downloader",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'youtube-download=youtube_downloader:main',
        ],
    },
    install_requires=[
        'yt-dlp',
    ],
    description="A simple Python YouTube downloader",
    author="Kiran Pandey",
    author_email="kp842586@gmail.com",
    url="https://github.com/Pandeyjr/youtube_downloader",  # Link to your repo if you plan to publish this
    long_description=open('README.md').read(),
)
