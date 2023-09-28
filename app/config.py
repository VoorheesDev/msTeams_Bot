import os


class DefaultConfig:
    """Class to represent a default Bot Configuration."""

    APP_ID = os.environ.get("APP_ID", "")
    APP_PASSWORD = os.environ.get("APP_PASSWORD", "")
