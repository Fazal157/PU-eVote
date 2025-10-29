#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    import threading, webbrowser, time, socket

    def open_browser():
        while True:
            try:
                # Try to connect to server port
                with socket.create_connection(("127.0.0.1", 8000), timeout=2):
                    break
            except OSError:
                time.sleep(1)
        webbrowser.open("http://127.0.0.1:8000/")

    threading.Thread(target=open_browser).start()
    main()

