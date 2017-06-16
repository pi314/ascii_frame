import sys
import ascii_frame

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='ascii_frame',
    version=ascii_frame.__version__,
    description='Wrap text with an ASCII frame.',
    url='https://github.com/pi314/ascii_frame',
    author='Cychih',
    author_email='michael66230@gmail.com',
    maintainer='Cychih',
    maintainer_email='michael66230@gmail.com',
    license='WTFPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
    packages=find_packages(exclude=['scripts']),
    scripts=['scripts/ascii_frame'],

    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
