# -*- coding: utf-8 -*-

# Scrapy settings for meituan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meituan'

SPIDER_MODULES = ['meituan.spiders']
NEWSPIDER_MODULE = 'meituan.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meituan (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__mta=218019497.1565764895582.1566373645392.1566373925144.14; _lxsdk_cuid=16c8edc21825f-0d2831709596ea-36664c08-1fa400-16c8edc2183c8; _hc.v=830a45c4-443f-e2e9-c4d1-ed8fcb171aa5.1565769197; iuuid=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; _lxsdk=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; _ga=GA1.2.1348654524.1565938623; mtcdn=K; cityname=%E6%B7%B1%E5%9C%B3; webp=1; __utmz=74597006.1566210835.3.3.utmcsr=meishi.meituan.com|utmccn=(referral)|utmcmd=referral|utmcct=/i/; isid=52FD344F5848EC3D3150CCF9FC21EC7D; logintype=normal; ci=30; rvct=30%2C118%2C280%2C277%2C113%2C91%2C281%2C92%2C686%2C20%2C108; client-id=0a40bbc7-1433-4fe8-aac3-21c3339e0517; __utma=74597006.1348654524.1565938623.1566210835.1566368904.4; a2h=4; IJSESSIONID=78jhqc02kupgoa4pnvsui3f0; oops=WCEN-yeleLVOqemGHAzNNiikyNIAAAAA5QgAAKgzJktpa4MpobcC4KwY02edRR1ZVfOqmcmsXl8Eiy-0PZCckDd1_W7T3bnhjmnREw; u=56727782; __utmc=74597006; ci3=1; latlng=22.527887,113.934118,1566370142419; i_extend=Gimthomepagecategory122H__a100265__b4; uuid=6d32a37a57944cf49334.1566370783.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=218019497.1565764895582.1566369259828.1566370784636.9; _lxsdk_s=16cb2b17226-482-632-310%7C%7C79',
    'Host': 'sz.meituan.com',
    'Referer': 'https://sz.meituan.com/jiankangliren/c76/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'meituan.middlewares.MeituanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    'meituan.middlewares.MeituanDownloaderMiddleware': 543,
    'meituan.middlewares.ProxyMiddleware': 101,
    # 'meituan.middlewares.RandomUserAgentMiddleware': 443,
    # 'meituan.middlewares.RandomCookiesMiddleware': 545,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    # 'meituan.middlewares.TooManyRequestsRetryMiddleware': 540,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'meituan.pipelines.MeituanPipeline': 300,
     'meituan.pipelines.MongoPipeline': 300,
     'meituan.pipelines.MysqlPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

REDIRECT_ENABLED = False
# HTTPERROR_ALLOWED_CODES = [403, 302]
HTTPERROR_ALLOWED_CODES = list(range(300, 600))
# RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408, 429]
RETRY_HTTP_CODES = list(range(400, 600))
RETRY_TIMES = 666


MONGO_URI = 'localhost'
MONGO_DB = 'MeiTuan_MongoDB'

MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'meituan'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_PORT = 3306

LOG_LEVEL = 'DEBUG'
LOG_FILE = 'log.txt'
# COMMANDS_MODULE = 'dianping.commands'