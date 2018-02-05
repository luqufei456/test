import expanddouban
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver


def Movie_url(Lei_xing,Di_qu):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影"
    Xu_qiu_url = url + "," + Lei_xing + "," +Di_qu
    return Xu_qiu_url

class Movie(object):
    def __init__(self,name,Ping_fen,Lei_xing,Di_qu,Ye_mian_link,Hai_bao_link):
        self.name = name
        self.Ping_fen = Ping_fen
        self.Lei_xing = Lei_xing
        self.Di_qu = Di_qu
        self.Ye_mian_link = Ye_mian_link
        self.Hai_bao_link = Hai_bao_link
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.name, self.Ping_fen, self.Lei_xing, self.Di_qu, self.Ye_mian_link, self.Hai_bao_link)