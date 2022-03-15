import sys

import yaml
from src.oems.liebherr_lidat import LiebherrLidat
from src.oems.takeuchi_tfm import TakeuchiTFM
from src.oems.volvo_caretrack import VolvoCaretrack
from src.oems.wacker_neuson_kramer_equipcare import WackerNeusonKramerEquipcare


def main(config):
    if config["NAME"] == "wacker-neuson-kramer-equipcare":
        WackerNeusonKramerEquipcare(
            data_url=config["DATA_URL"],
            adapter_name=config["NAME"],
            token_url=config["TOKEN_URL"],
            username=config["USERNAME"],
            password=config["PASSWORD"],
            client_id=config["CLIENT_ID"],
            client_secret=config["CLIENT_SECRET"],
        )()
    elif config["NAME"] == "volvo-caretrack":
        VolvoCaretrack(
            data_url=config["DATA_URL"],
            adapter_name=config["NAME"],
            username=config["USERNAME"],
            password=config["PASSWORD"],
        )()
    elif config["NAME"] == "liebherr-lidat":
        LiebherrLidat(
            data_url=config["DATA_URL"],
            adapter_name=config["NAME"],
            username=config["USERNAME"],
            password=config["PASSWORD"],
        )()
    elif config["NAME"] == "takeuchi-tfm":
        TakeuchiTFM(
            data_url=config["DATA_URL"],
            adapter_name=config["NAME"],
            token_url=config["TOKEN_URL"],
            client_id=config["CLIENT_ID"],
            client_secret=config["CLIENT_SECRET"],
        )()
    else:
        raise Exception("The adapter {} is not currently supported")
    return


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        config_normal = f.read()
    config = yaml.safe_load(f"{config_normal}")
    main(config)
