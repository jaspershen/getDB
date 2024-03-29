from setuptools import setup, find_packages

setup(name='getDB',
      version='0.0.4',
      description="This module can be used to download HMDB and KEGG database.",
      license='MIT',
      author='Xiaotao Shen',
      author_email='shenxt1990@163.com',
      url='https://github.com/jaspershen/getDB',
      long_description_content_type="text/markdown",
      packages=find_packages(),
      install_requires=['requests', 'pandas', 'bs4', 'numpy'],
      classifiers=[
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7'
      ]
      )