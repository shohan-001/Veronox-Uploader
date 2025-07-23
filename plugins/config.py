# plugins/config.py
import os
import logging
from dotenv import load_dotenv

# ────────────────────────────────────────────────────────
# Load variables from .env (if the file exists)
# ────────────────────────────────────────────────────────
load_dotenv()

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

class Config:
    # ───────── Mandatory Telegram / Pyrogram creds ─────────
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    API_ID    = int(os.getenv("API_ID", 0))
    API_HASH  = os.getenv("API_HASH", "")

    # ───────── Paths & size limits ─────────
    DOWNLOAD_LOCATION       = os.getenv("DOWNLOAD_LOCATION", "./DOWNLOADS")
    MAX_FILE_SIZE           = int(os.getenv("MAX_FILE_SIZE", 2194304000))
    TG_MAX_FILE_SIZE        = int(os.getenv("TG_MAX_FILE_SIZE", 2194304000))
    FREE_USER_MAX_FILE_SIZE = int(os.getenv("FREE_USER_MAX_FILE_SIZE", 2194304000))
    TG_MIN_FILE_SIZE        = int(os.getenv("TG_MIN_FILE_SIZE", 2194304000))
    CHUNK_SIZE              = int(os.getenv("CHUNK_SIZE", 128))

    # ───────── Optional URLs / proxies / watermark ─────────
    DEF_THUMB_NAIL_VID_S = os.getenv("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    HTTP_PROXY           = os.getenv("HTTP_PROXY", "")
    OUO_IO_API_KEY       = os.getenv("OUO_IO_API_KEY", "")
    DEF_WATER_MARK_FILE  = os.getenv("DEF_WATER_MARK_FILE", "@UploaderXNTBot")

    # ───────── Bot behaviour & housekeeping ─────────
    MAX_MESSAGE_LENGTH   = int(os.getenv("MAX_MESSAGE_LENGTH", 4096))
    PROCESS_MAX_TIMEOUT  = int(os.getenv("PROCESS_MAX_TIMEOUT", 3600))
    SESSION_STR          = os.getenv("SESSION_STR", "")
    SESSION_NAME         = "UploaderXNTBot"

    # ───────── Database & logging ─────────
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    LOG_CHANNEL  = int(os.getenv("LOG_CHANNEL", "0") or 0)

    # ───────── Admin & FSUB ─────────
    OWNER_ID       = int(os.getenv("OWNER_ID", "0") or 0)
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "")

    # ───────── Short‑link & verification ─────────
    TRUE_OR_FALSE = os.getenv("TRUE_OR_FALSE", "").lower() == "true"
    SHORT_DOMAIN  = os.getenv("SHORT_DOMAIN", "")
    SHORT_API     = os.getenv("SHORT_API", "")
    VERIFICATION  = os.getenv("VERIFICATION", "")

    # ───────── Misc ─────────
    BOT_USERNAME  = os.getenv("BOT_USERNAME", "")
    BANNED_USERS  = {int(x) for x in os.getenv("BANNED_USERS", "").split()} if os.getenv("BANNED_USERS") else set()

    LOGGER = logging
