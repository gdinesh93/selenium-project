import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Readconfig:

    @staticmethod
    def getapplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info', 'username')
        return username


    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
