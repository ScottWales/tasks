#!/usr/bin/env python
"""
Copyright 2015 ARC Centre of Excellence for Climate Systems Science

author: Scott Wales <scott.wales@unimelb.edu.au>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import yaml

from . import rt

class Session(object):
    """
    Holds a task manager session
    """

    def __init__(self):
        self.servers = {}
    
    def read_config(self, path = None, value = None):
        """
        Reads the config file at `path` and sets up servers

        The config file is in yaml format, looking like::

            ---
            server1:
              kind: rt
              url:  rt.example.com
              user: user
            server2:
              kind: trac
              url:  trac.example.com
        """

        if value is not None:
            config = yaml.safe_load(value)
        else:
            if path is None:
                path = os.path.join(os.environ('HOME'),'.tasks.rc')
            with open(path, 'r') as f:
                config = yaml.safe_load(f)

        for name, c in config.iteritems():
            self.add_server(name, url=c['url'], kind=c['kind'], user=c.get('user'))

    def add_server(self, name, url, kind, user=None):
        """
        Factory function for adding servers
        """
        if   kind == 'rt':
            self.servers[name] = rt.Server(url, user)
        elif kind == 'dummy':
            self.servers[name] = None
        else:
            raise NotImplementedError()
