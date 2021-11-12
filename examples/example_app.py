import argparse

import yaml
import psycopg
from munch import munchify
from fs.osfs import OSFS

import config_snacks.assertions as assertions
import config_snacks.placeholder


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = None
    with open(args.config, 'r') as config_fd:
        config = munchify(yaml.safe_load(config_fd))
    assertions.assert_none(config)

    normal_os_filesystem = OSFS("/")
    db_password_filepath = "/path/to/secrets/db_password"
    placeholders = config_snacks.placeholder.get_file_placeholders(normal_os_filesystem, db_password_filepath)

    assertions.assert_str(config.db.dbname)
    assertions.assert_str(config.db.user)
    assertions.assert_str(config.db.password)
    assertions.assert_str(config.db.host)
    assertions.assert_uint(config.db.port)
    connect_kwargs = config_snacks.placeholder.render(config.db.toDict(), placeholders)

    with psycopg.connect(**connect_kwargs) as conn:
        with conn.cursor() as cur:
            cur.execute("select count(*) from foo")
            count, = cur.fetchone()
            print("count: ", count)
