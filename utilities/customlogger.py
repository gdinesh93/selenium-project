import logging

class Loggen:
    @staticmethod
    def loggen():
        logger=logging.getLogger()
        fhandler=logging.FileHandler(filename='mylog.log',mode='a')
        formatter= logging.Formatter('%(acstime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        return logger
