#!/usr/bin/env python
from setuptools import setup, find_packages
import task.meta as meta

setup(
        name         = meta.name,
        version      = meta.version,
        author       = meta.author,
        author_email = meta.author_email,
        license      = meta.license,
        url          = meta.url,

        packages     = find_packages(),
        )
