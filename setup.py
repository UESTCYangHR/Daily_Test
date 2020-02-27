#from distutils.core import setup
from setuptools import setup, find_packages

VERSION = '0.0.1'

tests_require = []

install_requires = []

setup(name='LoveZC', # 模块名称
      url='https://github.com/UESTCYangHR/Daily_Test/blob/master/LoveZC.zip',  # 项目包的地址
      author="Peter Young",  # Pypi用户名称
      author_email='yhr_uestc@163.com',  # Pypi用户的邮箱
      keywords='Love ZC',
      description='May there be years to look back on, and with deep feelings to white head',
      license='MIT',  # 开源许可证类型
      classifiers=[
          'Operating System :: OS Independent',
          'Topic :: Software Development',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: PyPy'
      ],

      version=VERSION, 
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='runtests.runtests',
      extras_require={'test': tests_require},

      entry_points={ 'nose.plugins': [] },
      packages=find_packages(),
)