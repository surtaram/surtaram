import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename="/Users/surtaram/PycharmProjects/College_ERP/Logs/"+"automation.log",
                                       mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger

