from app.core.settings import (
    DATABASE_URL,
    SECRET_KEY
)

from app.core.logger import (
    logger
)


def validate_environment():

    missing = []

    if not DATABASE_URL:
        missing.append(
            "DATABASE_URL"
        )

    if not SECRET_KEY:
        missing.append(
            "SECRET_KEY"
        )

    if missing:

        raise RuntimeError(
            f"Missing environment variables: {', '.join(missing)}"
        )

    logger.info(
        "Environment configuration valid"
    )
