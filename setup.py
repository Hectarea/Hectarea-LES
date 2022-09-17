from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='HectareaPES',
    packages=['HectareaPES'],
    version='4.20.68.99.99',
    description='Hectarea Pizza Encryption Standard',
    author='Héctarea',
    license='MIT',
    install_requires=[],
    author_email = 'gonzalez.craqenll@gmail.com',
    url = 'https://hectarea.netlify.app/',
    keywords = ['Encryption', 'Pizza', 'Hectarea', 'Panera'],
    download_url= 'https://github.com/Hectarea/Hectarea-LES/archive/refs/tags/69.4.19.9.tar.gz',)