SN_VERSION = "4.0.0"
PROGRESS = 15
ENGINE = 5
LOGGING_VERBOSITY = 1
DEFAULT_ENDPOINT = "https://lishogi.org/shoginet/"
DEFAULT_THREADS = 2
HASH_MIN = 64
HASH_DEFAULT = 256
HASH_MAX = 512
MAX_BACKOFF = 30.0
MAX_FIXED_BACKOFF = 3.0
HTTP_TIMEOUT = 15.0
STAT_INTERVAL = 60.0
DEFAULT_CONFIG = "shoginet.ini"
PROGRESS_REPORT_INTERVAL = 5.0
LVL_SKILL = [-4, 0, 1, 3, 6, 12, 16, 20]
LVL_MOVETIMES = [50, 50, 75, 150, 200, 300, 400, 1000]
LVL_DEPTHS = [1, 1, 1, 2, 3, 6, 10, 22]
LVL_NODES = [1, 1, 5, 10, 15, 0, 0, 0]
DEAD_ENGINE_ERRORS = (EOFError, IOError, BrokenPipeError)