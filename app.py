"""WSGI entry point for deploying the Iris Dashboard (a2.py) on Render."""

from a2 import app, run_app, server

__all__ = ["app", "run_app", "server"]

if __name__ == "__main__":
    run_app()
