#!/usr/bin/env python
#coding:utf-8

class Config:
    SECRET_KEY = "dfahiu2jf"
    SALT = "jack"

class DevelopmentConfig(Config):
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWD = "123456"
    DB_NAME = "reboot"
    DB_POOL_MAX = 10
    DB_POOL_MIN = 1

class ProductionConfig(Config):
    DB_HOST = "localhost"
    DB_USER = "root"
    DB_PASSWD = "123456"
    DB_NAME = "reboot"
    DB_POOL_MAX = 10
    DB_POOL_MIN = 1

config = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig,
    'default': DevelopmentConfig
}