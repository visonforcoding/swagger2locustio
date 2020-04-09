import logging.config

API_OPERATIONS = ("get", "post", "put", "patch", "delete", "head", "options", "trace")
LOGGING_LEVELS = ("info", "debug", "warning", "error")


def config_logger(loglevel: str):
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
                },
            },
            "handlers": {
                "default": {
                    "level": loglevel,
                    "formatter": "standard",
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",  # Default is stderr
                },
            },
            "loggers": {
                '': {  # root logger
                    "handlers": ["default"],
                    "level": loglevel,
                    "propagate": False
                },
            }
        }
    )
