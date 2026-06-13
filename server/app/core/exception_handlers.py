from fastapi import (
    FastAPI,
    Request
)

from fastapi.responses import (
    JSONResponse
)

import traceback


def register_exception_handlers(
    app: FastAPI
):

    @app.exception_handler(Exception)
    async def global_exception_handler(

        request: Request,

        exc: Exception
    ):

        print(
            "\n===== UNHANDLED EXCEPTION ====="
        )

        traceback.print_exc()

        print(
            "===============================\n"
        )

        return JSONResponse(

            status_code=500,

            content={
                "detail":
                "Internal server error"
            }
        )
