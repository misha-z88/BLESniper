from setuptools import setup, find_packages
import sys

requirements = [
    'pybluez>=0.30.0',
    'pyserial>=3.5'
]

if sys.platform == 'darwin':
    requirements.append('pyobjc-framework-IOBluetooth')
elif sys.platform == 'win32':
    requirements.extend([
        'pywin32',
        'pypiwin32'
    ])

setup(
    name='blestrike',
    version='0.1.1',
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'macos': ['pyobjc-framework-IOBluetooth'],
        'windows': ['pywin32', 'pypiwin32']
    },
    author='Security Research Team',
    description='Cross-platform Bluetooth Analysis Toolkit',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.7+'
    ]
)