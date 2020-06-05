
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np


filename = 'cython_bbox'  # 源文件名
full_filename = 'cython_bbox.pyx'  # 包含后缀的源文件名
# 配置需要cython编译的源文件
setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension(filename, [full_filename])],
    include_dirs = [np.get_include()]
)