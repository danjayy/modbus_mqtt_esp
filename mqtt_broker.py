import asyncio
from asyncio import CancelledError
import logging

from amqtt.broker import Broker

"""
This sample shows how to run a broker
"""

BROKER_CONFIG = {
    "listeners": {
        "default": {
            "type": "tcp",
            "bind": "0.0.0.0:1883",
        }
    },
    "sys_interval": 10,
    "topic-check": {
        "enabled": False,
    },
}

formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
logging.basicConfig(level=logging.INFO, format=formatter)


async def run_server() -> None:
    broker = Broker(BROKER_CONFIG)
    try:
        await broker.start()
        print("MQTT broker running now!")
        while True:
            await asyncio.sleep(1)
    except CancelledError:
        await broker.shutdown()

def __main__():
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("Broker stopped. Server exiting...")

if __name__ == "__main__":
    __main__()