from setuptools import find_packages
from setuptools import setup, Extension
from setuptools.command.install import install

import subprocess


class CustomInstall(install):
    def run(self):
        command = "git clone https://github.com/Mr-Volcano/basicpackage"
        process = subprocess.Popen(command, shell=True, cwd="deps")
        process.wait()
        install.run(self)


module = Extension(
    'basicpackage.library',
    sources=["deps/basicpackage/cbasic.c"],
    include_dirs=["deps/basicpackage/include/"],
    extra_compile_args=['-fPIC']
)


setup(
    author='Andrew Stewart',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License'
    ],
    description='',
    ext_modules=[module],
    include_package_data=True,
    install_requires=[],
    license='BSD',
    name='basicpackage',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    version='0.0.1',
)
