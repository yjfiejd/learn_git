import os

os.system("pip3 install setuptools-39.2.0-py2.py3-none-any.whl --user")
from setuptools import setup, find_packages

print(find_packages())
setup(name = 'tsunagi',
                 version = '2.0',
                 description = 'mapping text to standard concept',
                 author = 'synyi',
                 author_email = 'gu.gen@synyi.com',
       include_package_data=True,
      packages = find_packages()+['tsunagi', 'data/EncryptData','ldk_proxy'],
                 zip_safe=False
)
