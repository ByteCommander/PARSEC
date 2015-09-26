import setuptools


setuptools.setup(
    name='PARSEC',
    version='0.0.1',
    author='ByteCommander',
    url='https://github.com/ByteCommander/PARSEC',

    packages=['Parsec', 'ChatExchange6'],
    
    install_requires=[
        'beautifulsoup4>=4.3.2',
        'requests>=2.2.1',
        'websocket-client>=0.13.0',
    ]
)
