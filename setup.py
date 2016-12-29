from setuptools import setup, find_packages
setup(
    name="NorTV4",
    version="0.1",
    packages=['nortv4', 'nortv4.plugins'],
    install_requires=['asyncio-irc'],
)