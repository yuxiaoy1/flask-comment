"""
    flask_comment
    ~~~~~~~~~~~~~~
    Create comment component in Jinja2 template.

    :author: Yuxiaoy <withyuxiaoy@gmail.com>
    :copyright: (c) 2021 by Yuxiaoy.
    :license: MIT, see LICENSE for more details.
"""
from setuptools import setup

setup(
    name='Flask-Comment',
    install_requires=['flask'],
    extras_require={
        'dev': [
            'coverage',
            'flake8',
            'tox',
        ],
    },
)
