#!/usr/bin/python
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

from heat.openstack.common import setup

requires = setup.parse_requirements()
project = 'heat'


setuptools.setup(
    name=project,
    version=setup.get_version(project),
    description='The heat project provides services for provisioning '
                'virtual machines',
    license='Apache License (2.0)',
    author='Heat API Developers',
    author_email='discuss@heat-api.org',
    url='http://heat.openstack.org/',
    cmdclass=setup.get_cmdclass(),
    packages=setuptools.find_packages(exclude=['bin']),
    include_package_data=True,
    install_requires=requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
    ],
    scripts=['bin/heat-cfn',
             'bin/heat-api',
             'bin/heat-api-cfn',
             'bin/heat-api-cloudwatch',
             'bin/heat-boto',
             'bin/heat-engine',
             'bin/heat-watch',
             'bin/heat-db-setup',
             'bin/cinder-keystone-setup',
             'bin/heat-keystone-setup'],
    py_modules=[])
