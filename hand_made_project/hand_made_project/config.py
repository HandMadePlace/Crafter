from environs import Env
from dataclasses import dataclass


@dataclass
class DB:
    name_db: str
    user_db: str
    pass_db: str
    host_db: str
    port_db: int


def settings():
    env = Env()
    env.read_env()

    name_db = env.str('NAME_DB')
    user_db = env.str('USER_DB')
    pass_db = env.str('PASS_DB')
    host_db = env.str('HOST_DB')
    port_db = env.int('PORT_DB')

    return DB(
        name_db=name_db,
        user_db=user_db,
        pass_db=pass_db,
        host_db=host_db,
        port_db=port_db
    )


settings = settings()
