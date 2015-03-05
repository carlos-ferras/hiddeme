#!/bin/bash

PREFIX=/usr/share

INSTALLDIR="$PREFIX/hiddeme"
BINDIR="/usr/bin"
PIXMAPSDIR="$PREFIX/pixmaps"
APPDIR="$PREFIX/applications"

# Are we root?
if [[ $EUID -ne 0 ]]; then
    echo "You must be root to run this script." 2>&1
    exit 1
else
    mkdir -p "$INSTALLDIR"
    cp *.{png,py} "$INSTALLDIR/"
	cp "hiddeme.ico" "$PIXMAPSDIR/"
	cp "hiddeme.desktop" "$APPDIR/"
    ln -s "$INSTALLDIR/hiddeme.py" "$BINDIR/hiddeme"
fi
