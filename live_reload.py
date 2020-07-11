#!/usr/bin/env python
from livereload import Server, shell

server = Server()
server.watch('themes/', shell('pelican content -s pelicanconf.py -t ./themes/basic', cwd='.'))
server.serve(root='output')
