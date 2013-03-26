#!/usr/bin/python

from unrar import unrar

archive = unrar('/home/bpross/rar_test/underemployed.s01e01.720p.hdtv.x264-evolve.rar')
archive.list_bare()
