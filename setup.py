# Copyright 2016-2020 The Van Valen Lab at the California Institute of
# Technology (Caltech), with support from the Paul Allen Family Foundation,
# Google, & National Institutes of Health (NIH) under Grant U24CA224309-01.
# All rights reserved.
#
# Licensed under a modified Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.github.com/vanvalenlab/deepcell-tf/LICENSE
#
# The Work provided may be used for non-commercial academic purposes only.
# For any other use of the Work, including commercial use, please contact:
# vanvalenlab@gmail.com
#
# Neither the name of Caltech nor the names of its contributors may be used
# to endorse or promote products derived from this software without specific
# prior written permission.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import logging

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


def _parse_requirements(file_path):
    lineiter = (line.strip() for line in open(file_path))
    reqs = []
    for line in lineiter:
        # workaround to ignore keras_maskrcnn requirement
        # which is downloaded directly from github
        if line.startswith('#') or line.startswith('git+'):
            continue
        reqs.append(line)
    return reqs


try:
    install_reqs = _parse_requirements('requirements.txt')
except Exception:
    logging.warning('Failed to load requirements file, using default ones.')
    install_reqs = []

setup(
    name='DeepCell',
    version='0.7.0',
    packages=find_packages(),
    install_requires=install_reqs,
    extras_require={
        'tests': ['pytest',
                  'pytest-cov'],
    },
    license='LICENSE',
    author='David Van Valen',
    author_email='vanvalen@caltech.edu',
    description='Deep learning for single cell image segmentation',
)
