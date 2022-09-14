from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='LES',
    packages=['HectareaLES'],
    version='4.20.68',
    description='Hectarea Loop Encryption System ',
    author='Héctarea',
    license='MIT',
    install_requires=[],
    author_email = 'gonzalez.craqenll@gmail.com',
    url = 'https://hectarea.netlify.app/',
    keywords = ['Encryption', 'Dictionary', 'Hectarea', 'Secrets'],
    download_url= 'https://github.com/Hectarea/DictionaryEncryption/archive/refs/tags/4.20.68.2.tar.gz',)