__all__ = "router"

from aiogram import Router
from .start import router as start_router
from .echo import router as echo_router

router = Router(name=__name__)
router.include_routers(
    start_router,
)

# always last include
router.include_router(echo_router)
