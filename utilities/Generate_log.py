import logging


def generate_logs():
    logging.basicConfig(
        filename="Example.log",
        level=logging.INFO,
        format='%(asctime)s -%(levelname)s - %(message)s',
        datefmt='%Y-%m-%d-%H:%H:%S %p'
    )
    return logging.getLogger()

