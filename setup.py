from setuptools import setup, find_packages


setup(
    name='msgWhatsapp',
    version='0.1',
    license='',
    author="J.V.K",
    author_email='jaivkadam@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/hostserver001/msgWhatsapp',
    keywords='whatsapp',
    install_requires=[
          'pyautogui',
          'PyPi-Browser',
          'time',
          'datetime'
      ],

)
