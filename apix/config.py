from configparser import RawConfigParser
import random, string

SECRET_KEY_CHARS = f"{string.ascii_letters}{string.digits}{string.punctuation}"

def generate_secret_key():
    return "".join([random.SystemRandom().choice(SECRET_KEY_CHARS) for i in range(50)])

class _CONFIG_WRAPPER:
    CONFIG = None

def load_config(path):
    config_file = RawConfigParser()
    if not path.exists():
        default_config = '\n'.join([
            "[django]",
            f"secret_key = {generate_secret_key()}",
            "debug = YES",
            "time_zone = America/Los_Angeles",
            "allowed_hosts = localhost, 127.0.0.1",
            "db_url = postgres://apix:apix@127.0.0.1/apix",
        ])
        path.write_text(default_config)
    config_file.read(path)
    config = {}
    for x in config_file:
        for y in config_file[x].items():
            config["{}.{}".format(x,y[0])] = y[1]
    _CONFIG_WRAPPER.CONFIG = config
    return config

def config(key, default=None):
    try:
        return _CONFIG_WRAPPER.CONFIG[key]
    except KeyError:
        return default

def config_int(*args, **kwargs):
    return int(config(*args, **kwargs))

def config_bool(*args, **kwargs):
    val = config(*args, **kwargs)
    if val is None:
        return None
    if val.upper() in ['YES','TRUE','YEAH', 'SURE', 'YUP', 'YEP', 'SI', 'OUI', 'JA', 'ON', 'да'.upper(), 'はい', '是', 'हां', 'Ναι'.upper()]:
        return True
    if val.upper() in ['NO','FALSE','NAH', 'MEH', 'NOPE','NON','NEIN', 'OFF', 'нет'.upper(), 'いいえ', '沒有', 'नहीं', 'Όχι'.upper()]:
        return False
    try:
        if int(val) != 0:
            return True
    except:
        pass
    return False

def config_list(*args, **kwargs):
    return [x.strip() for x in config(*args, **kwargs).split(',')]
