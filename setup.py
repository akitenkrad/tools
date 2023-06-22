import sys

import setuptools

with open("README.md", mode="r") as f:
    long_description = f.read()

version_range_max = max(sys.version_info[1], 10) + 1
python_min_version = (3, 8, 0)

setuptools.setup(
    name="tools",
    version="0.0.1",
    author="akitenkrad",
    author_email="akitenkrad@gmail.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
    ]
    + ["Programming Language :: Python :: 3.{}".format(i) for i in range(python_min_version[1], version_range_max)],
    long_description=long_description,
    install_requires=[
        "click",
        "numpy",
        "pandas",
        "PyYAML",
        "toml",
        "py-cpuinfo",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib",
        "oauth2client",
        "tqdm",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "mypy",
            "flake8",
            "isort",
            "jupyterlab",
            "types-python-dateutil",
            "types-PyYAML",
            "types-requests",
            "typing-extensions",
        ]
    },
    entry_points={
        "console_scripts": [
            "tools = tools.cli:cli",
        ],
    },
)
