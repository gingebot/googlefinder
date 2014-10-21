from distutils.core import setup
setup(
    name = 'googlefinder',
    packages = ['googlefinder'], # this must be the same as the name above
    version = '0.1',
    description = 'Google finder returns google search results against a list of search parameters. Results consist of a 2 part tuple of url and result description',
    author = 'gingebot',
    author_email = 'gingebot@gmail.com',
    url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
    download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
    keywords = ['google', 'search'], # arbitrary keywords
    classifiers = [],
    install_requires=['requests>=2.4.3', 'beautifulsoup4>=4.3.2'],
)
