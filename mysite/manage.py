#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    debug = True

    if debug:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ahead.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ahead.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
