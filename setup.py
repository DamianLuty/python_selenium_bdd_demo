# from distutils.core import setup
from setuptools import setup

setup(name='PythonBDDFramework',
      version='1.0',
      packages=[
          'src',
          'src.common',
          'src.common.common_configs',
          'src.common.common_functionalities',
          'src.pages',
          'test'
      ],
      )
