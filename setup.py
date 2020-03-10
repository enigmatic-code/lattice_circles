# this file allows lattice_circles.py to be installed directly from GitHub
#
# using Poetry, add the following in pyproject.toml file:
#
# --
# [tool.poetry.dependencies.lattice_circles]
# git = "https://github.com/enigmatic-code/lattice_circles.git"
# --
#
#
# [[[ Formerly adding this to requirements.txt worked:
# --
# git+https://github.com/enigmatic-code/lattice_circles.git#egg=lattice_circles
# --
# but not any more. ]]]

from setuptools import setup

# minimal setup config
setup(name='lattice_circles', py_modules=['lattice_circles'])
