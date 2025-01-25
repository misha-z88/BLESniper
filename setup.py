from setuptools import setup, find_packages

setup(
    name='blestrike', 
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pybluez==0.22',  
        'pyserial>=3.5'
    ],
    author='Your Name',
    description='Bluetooth Security Toolkit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/misha-z88/BLEStrike',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7+'
    ]
)
