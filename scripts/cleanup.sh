#!/bin/sh
command -v gh >/dev/null 2>&1 && gh auth logout
rm -rf ~/autonomy_ws