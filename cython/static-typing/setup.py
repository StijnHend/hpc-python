from distutils.core import setup, Extension
from Cython.Build import cythonize

# run file in terminal: python setup.py build_ext --inplace
setup(
     ext_modules=cythonize("cyt_module.pyx", annotate=True, language_level=3)
)
