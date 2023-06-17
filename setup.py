from setuptools import find_packages, setup

setup(
    name='netbox-netbox_sb_dc_accessdata',
    version='1.0',
    description='SB DC Accessdata',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    author='Marco Krajniak',
    license='All rights reserved',
    keywords=['netbox', 'netbox-plugin', 'datacenter'],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)