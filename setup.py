from distutils.core import setup

setup(
    name='OpenPlatform',
    version='0.0.1',
    author='Mart van de Ven',
    author_email='m@type.hk',
    packages=['openplatform'],
    description='Fabric scripts for Open Platoform Useful towel-related stuff.',
    install_requires=[
        "Fabric = 1.8.3"
    ],
)
