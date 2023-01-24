""" Setup """
from setuptools import setup

setup(
    name="evernote3",
    version="0.1",
    author="Evernote Corporation",
    author_email="api@evernote.com",
    url="http://dev.evernote.com",
    description="Evernote SDK for Python3",
    license="BSD",
    install_requires=["oauth2", "oauthlib", "requests_oauthlib"],
)
