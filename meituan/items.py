# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class AreaItem(Item):
    collection = table = 'area'

    id = Field()
    districtId = Field()
    cityId = Field()
    areaId = Field()
    type = Field()
    name = Field()
    slug = Field()
    hot = Field()
    masterId = Field()
    crawl_time = Field()


class CategoryItem(Item):
    collection = table = 'category'

    id = Field()
    name = Field()
    url = Field()
    pinyin = Field()
    crawl_time = Field()


class GoodsItem(Item):
    collection = table = 'goods'

    id = Field()
    title = Field()
    price = Field()
    value = Field()
    sales = Field()
    shopId = Field()
    shopTitle = Field()
    crawl_time = Field()


class GoodsCommentItem(Item):
    collection = table = 'goods_comment'

    id = Field()
    goodsId = Field()
    content = Field()
    picUrls = Field()
    modTime = Field()
    star = Field()
    userName = Field()
    isAnonymous = Field()
    imgUrl = Field()
    shopTitle = Field()
    recordCount = Field()
    startIndex = Field()
    nextStartIndex = Field()
    isEnd = Field()
    crawl_time = Field()


class GoodsTagItem(Item):
    collection = table = 'goods_tag'

    id = Field()
    content = Field()
    count = Field()
    isPositive = Field()
    goodsId = Field()
    crawl_time = Field()


class ShopItem(Item):
    collection = table = 'shop'

    id = Field()
    title = Field()
    address = Field()
    lowestprice = Field()
    avgprice = Field()
    latitude = Field()
    longitude = Field()
    showType = Field()
    avgscore = Field()
    comments = Field()
    historyCouponCount = Field()
    backCateName = Field()
    areaname = Field()
    areaId = Field()
    categoryIdList = Field()
    cateId = Field()
    groupCoupon = Field()
    dangleAbstracts = Field()
    dealsNum = Field()
    hasAds = Field()
    cityId = Field()
    city = Field()
    full = Field()
    crawl_time = Field()


class ShopCommentItem(Item):
    collection = table = 'shop_comment'

    id = Field()
    shopId = Field()
    userName = Field()
    userUrl = Field()
    avgPrice = Field()
    comment = Field()
    merchantComment = Field()
    picUrls = Field()
    commentTime = Field()
    replyCnt = Field()
    zanCnt = Field()
    readCnt = Field()
    userLevel = Field()
    userId = Field()
    uType = Field()
    star = Field()
    quality = Field()
    alreadyZzz = Field()
    reviewId = Field()
    menu = Field()
    did = Field()
    dealEndtime = Field()
    anonymous = Field()
    crawl_time = Field()


class ShopTagItem(Item):
    collection = table = 'shop_tag'

    id = Field()
    tag = Field()
    count = Field()
    shopId = Field()
    crawl_time = Field()