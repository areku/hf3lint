from distutils.core import setup

import hf3lint

setup(
    name='hf3lint',
    version=hf3lint.__version__,
    py_modules=['hf3lint'],
    url='http://github.com/areku/hf3lint',
    license='GPL 3',
    author='Alexander Weigl',
    author_email='uiduw@student.kit.edu',
    description='Linter for Hiflow3',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Environment :: Console",
        "Operating System :: Microsoft",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    entry_points = {
        'console_scripts' : [
            "hf3lint = hf3lint:main"
        ]
    }
)


