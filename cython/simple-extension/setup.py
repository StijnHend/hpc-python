from distutils.core import setup
from Cython.Build import cythonize

# run file in terminal: python setup.py build_ext --inplace

setup(ext_modules=cythonize("cyt_module.pyx", language_level=3),)
