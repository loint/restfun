from setuptools import setup, find_packages

setup(
   name='rest',
   version='1.0',
   description='',
   author='Loi Nguyen',
   author_email='loinguyentrung@gmail.com',
   packages=find_packages(),
   install_requires=[
       'click'
   ],
   scripts=[
        'rest'
   ]
)