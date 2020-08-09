#!/usr/bin/env python
from livereload import Server, shell

server = Server()
# -t defines the theme location while generating pelican content
server.watch('themes/', shell('pelican content -s pelicanconf.py -t ./themes/basic', cwd='.'))
server.serve(root='output')
