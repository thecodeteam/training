#some parts of RQ expect this file, but I dont want to include config details here, so I import them from my real config file

from config import Config
cfg = Config(file('private_config.cfg'))
REDIS_HOST=cfg.redis_host
REDIS_DB=cfg.redis_rq_db
REDIS_PASSWORD=cfg.redis_password
REDIS_PASS=cfg.redis_password
