# setup.py
from setuptools import setup

setup(
  name='ccwc',
  version='1.0.0',
  py_modules=['ccwc'],
  python_requires=">=3.6",
  install_requires=['Click'],
  entry_points={
    'console_scripts': [
      'ccwc=ccwc:main'
    ]
  }
)