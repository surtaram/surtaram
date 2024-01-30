# this file use for read common data from config.ini file

# configparser is python in-built module that allow you to read and write configuration files in the ini format and
# RawConfigParser class is one of the classes provided by the configparser module that allow you to work with
# configuration files that are written in the ini format without any interpolation of values

# static method:- we can call directly method without creating any object

import configparser

config = configparser.RawConfigParser()

config.read("/Users/surtaram/PycharmProjects/College_ERP/Configurations/config.ini")


class Readconfig:
    @staticmethod
    def getapplicationurl():
        url = config.get("common info", "Base_URL")

        return url

    @staticmethod
    def getusername():
        username = config.get("common info", "Username")
        return username

    @staticmethod
    def getpassword():
        password = config.get("common info", "Password")
        return password



# Readconfig.getapplicationurl()
#
# Readconfig.getusername()
# Readconfig.getpassword()
