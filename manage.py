#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from gevent import monkey



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lldc.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# Apply monkey-patch if we are running the huey consumer.
if 'run_huey' in sys.argv:
    monkey.patch_all()

if __name__ == '__main__':
    main()




