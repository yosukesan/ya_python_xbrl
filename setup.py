import setuptools

with open ("README.rst", "r") as fh:
	rst_description: str = fh.read()

setuptools.setup (name='Distutils',
        version='0.1',  
        description=rst_description,
        author='Yosuke OTSUKI',
        author_email='y.otsuki30@gmail.com',
        url='https://github.com/yosukesan',
	    packages = setuptools.find_packages(exclude=('test')),
)
