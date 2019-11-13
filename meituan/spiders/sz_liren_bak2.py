# -*- coding: utf-8 -*-
import json
import re
from datetime import datetime
from pprint import pprint
import random
from time import sleep

import scrapy
from scrapy import Request
from meituan.items import *
from meituan.share import html_from_uri, calc_md5


class SzLirenSpider(scrapy.Spider):
    name = 'sz_liren2'
    allowed_domains = ['meituan.com']
    start_urls = ['https://sz.meituan.com/jiankangliren/']
    shop_detail_baseurl = 'https://apimobile.meituan.com/group/v4/poi/pcsearch/30?limit=1000&offset=0&cateId={cateId}&areaId={areaId}'
    shop_comment_baseurl = 'https://www.meituan.com/ptapi/poi/getcomment?id={shopid}&offset={offset}&pageSize=10&sortType=0'
    goods_comment_baseurl = 'https://i.meituan.com/general/platform/mttgdetail/mtdealcommentsgn.json?dealid={dealid}&limit=10&offset={offset}&sorttype=1&tag='
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {

            # 'Accept': '*/*',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            # 'Connection': 'keep-alive',
            # 'Cookie': '_lxsdk_cuid=16c8edc21825f-0d2831709596ea-36664c08-1fa400-16c8edc2183c8; _hc.v=830a45c4-443f-e2e9-c4d1-ed8fcb171aa5.1565769197; iuuid=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; _lxsdk=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; _ga=GA1.2.1348654524.1565938623; cityname=%E6%B7%B1%E5%9C%B3; webp=1; __utmz=74597006.1566210835.3.3.utmcsr=meishi.meituan.com|utmccn=(referral)|utmcmd=referral|utmcct=/i/; isid=52FD344F5848EC3D3150CCF9FC21EC7D; logintype=normal; __utma=74597006.1348654524.1565938623.1566210835.1566368904.4; a2h=4; IJSESSIONID=78jhqc02kupgoa4pnvsui3f0; oops=WCEN-yeleLVOqemGHAzNNiikyNIAAAAA5QgAAKgzJktpa4MpobcC4KwY02edRR1ZVfOqmcmsXl8Eiy-0PZCckDd1_W7T3bnhjmnREw; u=56727782; __utmc=74597006; ci3=1; latlng=22.527887,113.934118,1566370142419; i_extend=Gimthomepagecategory122H__a100265__b4; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; cssVersion=e09c1174; wm_order_channel=default; utm_source=; au_trace_key_net=default; openh5_uuid=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; ci=30; rvct=30%2C686%2C91%2C118%2C280%2C277%2C113%2C281%2C92%2C20%2C108; lat=22.57063; lng=114.05787; uuid=9c4d045b375e4821990f.1566526658.1.0.0; _lxsdk_s=16cd1d6e583-6b1-ee7-049%7C%7C3',
            # 'Host': 'apimobile.meituan.com',
            # 'Origin': 'https://sz.meituan.com',
            # 'Referer': 'https://sz.meituan.com/jiankangliren/pn3/',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',

            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': '__mta=218019497.1565764895582.1566457307006.1566894545491.17; _lxsdk_cuid=16c8edc21825f-0d2831709596ea-36664c08-1fa400-16c8edc2183c8; _hc.v=830a45c4-443f-e2e9-c4d1-ed8fcb171aa5.1565769197; iuuid=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; _lxsdk=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; _ga=GA1.2.1348654524.1565938623; cityname=%E6%B7%B1%E5%9C%B3; webp=1; __utmz=74597006.1566210835.3.3.utmcsr=meishi.meituan.com|utmccn=(referral)|utmcmd=referral|utmcct=/i/; isid=52FD344F5848EC3D3150CCF9FC21EC7D; logintype=normal; __utma=74597006.1348654524.1565938623.1566210835.1566368904.4; a2h=4; IJSESSIONID=78jhqc02kupgoa4pnvsui3f0; oops=WCEN-yeleLVOqemGHAzNNiikyNIAAAAA5QgAAKgzJktpa4MpobcC4KwY02edRR1ZVfOqmcmsXl8Eiy-0PZCckDd1_W7T3bnhjmnREw; u=56727782; __utmc=74597006; ci3=1; latlng=22.527887,113.934118,1566370142419; i_extend=Gimthomepagecategory122H__a100265__b4; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; cssVersion=e09c1174; wm_order_channel=default; utm_source=; au_trace_key_net=default; openh5_uuid=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; ci=30; rvct=30%2C686%2C91%2C118%2C280%2C277%2C113%2C281%2C92%2C20%2C108; __mta=218019497.1565764895582.1566457304870.1566466187104.11; lat=22.57063; lng=114.05787; uuid=9c4d045b375e4821990f.1566526658.1.0.0; _lxsdk_s=16cd231558a-85-d9b-1b8%7C%7C2',
            # 'Host': 'sz.meituan.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',

        },
        'LOG_FILE': 'sz_liren.txt',
    }
    area_id_list = []
    category_id_list = []

    # def start_requests(self):

    def parse(self, response):
        # pprint(response.text)
        raw_data = response.text
        json_data = re.findall('<script>window.AppData = (.*?);</script>', raw_data, re.S)
        if json_data:
            dict_data = json.loads(json_data[0])
            # pprint(dict_data)
            # self.area_id_list.append(dict_data.get('area').get('id'))
            # 解析商圈地址开始
            area_list = dict_data.get('area').get('children')
            if area_list[0].get('name') == '推荐商圈':
                area_list = area_list[1:]
            # print('area_list: {}'.format(area_list))
            area_item = AreaItem()
            for area in area_list:
                print('area: {}'.format(area))
                # area_item = AreaItem()
                area_item['id'] = area.get('id')
                area_item['districtId'] = area.get('districtId')
                area_item['cityId'] = area.get('cityId')
                area_item['areaId'] = area.get('areaId')
                area_item['type'] = area.get('type')
                area_item['name'] = area.get('name')
                area_item['slug'] = area.get('slug')
                area_item['hot'] = area.get('hot')
                area_item['masterId'] = area.get('masterId')
                area_item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.area_id_list.append(area.get('id'))
                yield area_item
                children_area_item = AreaItem()
                if 'children' in area:
                    for children_area in area.get('children'):
                        print('children_area: {}'.format(area.get('children')))
                        children_area_item['id'] = children_area.get('id')
                        children_area_item['districtId'] = children_area.get('districtId')
                        children_area_item['cityId'] = children_area.get('cityId')
                        children_area_item['areaId'] = children_area.get('areaId')
                        children_area_item['type'] = children_area.get('type')
                        children_area_item['name'] = children_area.get('name')
                        children_area_item['slug'] = children_area.get('slug')
                        children_area_item['hot'] = children_area.get('hot')
                        children_area_item['masterId'] = children_area.get('masterId')
                        children_area_item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        self.area_id_list.append(children_area.get('id'))
                        yield children_area_item
            self.area_id_list.append(dict_data.get('area').get('id'))
            # 解析商圈地址结束，由于dict_data.get('area').get('id')代表不选择商圈，此时的json数据中deals字段（即商品数量不全）所以放在最后。

            # 解析类别开始
            category_data = dict_data.get('category')
            self.category_id_list.append(category_data.get('id'))
            category_item = CategoryItem()
            category_item['id'] = category_data.get('id')
            category_item['name'] = category_data.get('name')
            category_item['url'] = category_data.get('url')
            category_item['pinyin'] = category_data.get('pinyin')
            category_item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield category_item
            category_list = category_data.get('children')
            for category in category_list:
                # category_item = CategoryItem()
                category_item['id'] = category.get('id')
                category_item['name'] = category.get('name')
                category_item['url'] = category.get('url')
                category_item['pinyin'] = category.get('pinyin')
                category_item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.category_id_list.append(category.get('id'))
                yield category_item
                if 'children' in category:
                    for children_category in category.get('children'):
                        category_item['id'] = children_category.get('id')
                        category_item['name'] = children_category.get('name')
                        category_item['url'] = children_category.get('url')
                        category_item['pinyin'] = children_category.get('pinyin')
                        category_item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        self.category_id_list.append(children_category.get('id'))
                        yield category_item
            # 解析类别结束
        print('area_id_list:{} len: {}'.format(self.area_id_list, len(self.area_id_list)))
        print('category_id_list:{} len: {}'.format(self.category_id_list, len(self.category_id_list)))

        first_url_count = 0
        for cateId in self.category_id_list:
            for areaId in self.area_id_list:
                shop_detail_url = self.shop_detail_baseurl.format(cateId=cateId, areaId=areaId)
                pprint('shop_detail_url:{}'.format(shop_detail_url))
                self.logger.debug('shop_detail_url:{}'.format(shop_detail_url))
                yield Request(shop_detail_url, callback=self.parse_shop_detail, dont_filter=True,
                              meta={'cateId': cateId, 'areaId': areaId})
                first_url_count += 1
                pprint('first_url_count:{}'.format(first_url_count))
                self.logger.debug('first_url_count:{}'.format(first_url_count))
                # self.get_shop_detail(shop_detail_url, cateId, areaId)

    def parse_shop_detail(self, response):
        # pprint('parse_shop_detail response.text:{}'.format(response.text))
        shop_detail_url = response.url
        cateId = response.meta.get('cateId')
        areaId = response.meta.get('areaId')
        pprint('parse_shop_detailshop_detail_url:{}'.format(shop_detail_url))
        self.logger.debug('parse_shop_detail cateId:{} areaId:{}'.format(cateId, areaId))
    #     self.get_shop_detail(shop_detail_url, cateId, areaId)
    #
    # def get_shop_detail(self, url, cateId, areaId):
        sleep(random.randint(1, 5))
        json_data = html_from_uri(shop_detail_url)
        pprint('parse_shop_detailjson_data:{}'.format(json_data))
        self.logger.debug('parse_shop_detailjson_data:{}'.format(json_data))
        if json_data:
            pprint('pjson_data:{}'.format(json_data))
            dict_data = json.loads(json_data)
            total_count = dict_data.get('data').get('totalCount')
            shop_list = dict_data.get('data').get('searchResult')
            shop_item = ShopItem()
            true_total_count = 0
            for shop in shop_list:
                shop_item['cateId'] = cateId
                shop_item['areaId'] = areaId
                shop_item['id'] = shop.get('id')
                shop_item['title'] = shop.get('title')
                shop_item['address'] = shop.get('address')
                shop_item['lowestprice'] = shop.get('lowestprice')
                shop_item['avgprice'] = shop.get('avgprice')
                shop_item['latitude'] = shop.get('latitude')
                shop_item['longitude'] = shop.get('longitude')
                shop_item['showType'] = shop.get('showType')
                shop_item['avgscore'] = shop.get('avgscore')
                shop_item['comments'] = shop.get('comments')
                shop_item['historyCouponCount'] = shop.get('historyCouponCount')
                shop_item['backCateName'] = shop.get('backCateName')
                shop_item['areaname'] = shop.get('areaname')
                shop_item['categoryIdList'] = shop.get('cate')
                groupCoupon = shop.get('abstracts')
                shop_item['groupCoupon'] = '&'.join(
                    groupCoupon[i].get('message') for i in range(len(groupCoupon))) if groupCoupon else None
                dangleAbstracts = shop.get('dangleAbstracts')
                shop_item['dangleAbstracts'] = '&'.join(
                    dangleAbstracts[i].get('message') for i in range(len(dangleAbstracts))) if dangleAbstracts else None
                deals = shop.get('deals')
                shop_item['dealsNum'] = len(deals) if deals else 0
                if deals:
                    goods_item = GoodsItem()
                    for deal in deals:
                        goods_item['shopId'] = shop.get('id')
                        goods_item['shopTitle'] = shop.get('title')
                        goods_item['id'] = deal.get('id')
                        goods_item['title'] = deal.get('title')
                        goods_item['price'] = deal.get('price')
                        goods_item['value'] = deal.get('value')
                        goods_item['sales'] = deal.get('sales')
                        goods_item['value'] = deal.get('value')
                        goods_item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                        dealid = deal.get('id')
                        goods_comment_url = self.goods_comment_baseurl.format(dealid=dealid, offset=0)
                        yield scrapy.Request(goods_comment_url, callback=self.parse_goods_comment,
                                             meta={'dealid': dealid, 'offset': 0})
                        # pprint('shopId:{}, dealsId:{}'.format(goods_item['shopId'], goods_item['id']))
                        # self.logger.debug('shopId:{}, dealsId:{}'.format(goods_item['shopId'], goods_item['id']))
                        # self.get_goods_comment(goods_comment_url, dealid, 0, 1)
                        yield goods_item
                shop_item['hasAds'] = shop.get('hasAds')
                shop_item['cityId'] = shop.get('cityId') if shop.get('cityId') else 30
                shop_item['city'] = shop.get('city') if shop.get('city') else '深圳'
                shop_item['full'] = shop.get('full')
                shop_item['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                yield shop_item
                shopid = shop.get('id')
                shop_comment_url = self.shop_comment_baseurl.format(shopid=shopid, offset=0)
                yield scrapy.Request(shop_comment_url, callback=self.parse_shop_comment,
                                     meta={'shopid': shop.get('id'), 'offset': 0})
                # true_total_count += 1
                # pprint('total_count:{} true_total_count:{}'.format(total_count,true_total_count))
                # self.logger.debug('total_count:{} true_total_count:{}'.format(total_count,true_total_count))
                # self.get_shop_comment(shop_comment_url, shopid, 0, 1)


    def parse_goods_comment(self, response):
        pprint('parse_goods_comment response.text:{}'.format(response.text))
        self.logger.debug('parse_goods_comment response.text:{}'.format(response.text))
        goods_comment_url = response.url
        dealid = response.meta.get('dealid')
        offset = response.meta.get('offset')
        pprint('parse_goods_comment goods_comment_url:{}'.format(goods_comment_url))
        self.logger.debug('parse_goods_comment goods_comment_url:{}'.format(goods_comment_url))
        self.get_goods_comment(goods_comment_url, dealid, offset, 1)

    def parse_shop_comment(self, response):
        pprint('parse_shop_comment response.text:{}'.format(response.text))
        self.logger.debug('parse_shop_comment response.text:{}'.format(response.text))
        shop_comment_url = response.url
        shopid = response.meta.get('shopid')
        offset = response.meta.get('offset')
        pprint('parse_shop_comment goods_comment_url:{}'.format(shop_comment_url))
        self.logger.debug('parse_shop_comment shop_comment_url:{}'.format(shop_comment_url))
        self.get_shop_comment(shop_comment_url, shopid, offset, 1)

    def get_goods_comment(self, url, dealid, offset, page):
        pprint('get_goods_comment offset:{} dealid:{}'.format(offset, dealid))
        self.logger.debug('get_goods_comment offset:{} dealid:{}'.format(offset, dealid))
        sleep(random.randint(1, 5))
        print('开始爬取goods_comment第{}页......,url为{}'.format(page, url))
        self.logger.debug('开始爬取goods_comment第{}页......,url为{}'.format(page, url))
        # html = requests.get(url, headers=headers, proxies=p)
        json_data = html_from_uri(url)
        pprint(json_data)
        self.logger.debug(json_data)
        # #从直接浏览器得到的结果看需要正则提取，但用requests_html库返回的数据已经是json格式了，所以注释了
        # dict_data = re.findall('RawParsed(.*){"tags": ', html)[0]
        dict_data = json.loads(json_data)
        goods_tag = GoodsTagItem()
        for tag in dict_data['tags']:
            goods_tag['id'] = calc_md5(tag)
            goods_tag['goodsId'] = dealid
            goods_tag['content'] = tag.get('content')
            goods_tag['count'] = tag.get('count')
            goods_tag['isPositive'] = tag.get('isPositive')
            goods_tag['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield goods_tag
        if 'list' in dict_data:
            comment_groups = dict_data['list']
            goods_comment = GoodsCommentItem()
            for comment in comment_groups:
                goods_comment['id'] = calc_md5(comment)
                goods_comment['goodsId'] = dealid
                goods_comment['content'] = comment.get('content')
                picUrls = comment.get('picUrls')
                goods_comment['picUrls'] = ', '.join(picUrl for picUrl in picUrls) if picUrls else None
                goods_comment['modTime'] = comment.get('modTime')
                goods_comment['star'] = comment.get('star') / 10
                user = comment.get('user')
                goods_comment['userName'] = user.get('userName')
                goods_comment['isAnonymous'] = user.get('isAnonymous')
                goods_comment['imgUrl'] = user.get('imgUrl')
                goods_comment['shopTitle'] = comment.get('poi').get('title')
                goods_comment['recordCount'] = dict_data.get('recordCount')
                goods_comment['startIndex'] = dict_data.get('startIndex')
                goods_comment['nextStartIndex'] = dict_data.get('nextStartIndex')
                goods_comment['isEnd'] = dict_data.get('isEnd')
                goods_comment['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                yield goods_comment

            offset += 10
            next_url = self.goods_comment_baseurl.format(dealid=dealid, offset=offset)
            page = page + 1
            self.get_goods_comment(next_url, dealid, offset, page)

    def get_shop_comment(self, url, shopid, offset, page):
        pprint('get_shop_comment offset:{} shopid:{}'.format(offset, shopid))
        self.logger.debug('get_shop_comment offset:{} shopid:{}'.format(offset, shopid))
        sleep(random.randint(1, 5))
        print('开始爬取shop_comment第{}页......,url为{}'.format(page, url))
        self.logger.debug('开始爬取shop_comment第{}页......,url为{}'.format(page, url))
        # html = requests.get(url, headers=headers, proxies=p)
        json_data = html_from_uri(url)
        print(json_data)
        self.logger.debug(json_data)
        # dict_data = re.findall('RawParsed(.*){"tags": ', html)[0]
        dict_data = json.loads(json_data)
        shop_tag = ShopTagItem()
        for tag in dict_data['tags']:
            shop_tag['id'] = calc_md5(tag)
            shop_tag['shopId'] = shopid
            shop_tag['tag'] = tag.get('tag')
            shop_tag['count'] = tag.get('count')
            shop_tag['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            yield shop_tag
        if 'comments' in dict_data and dict_data['comments']:
            comment_groups = dict_data['comments']
            shop_comment = ShopCommentItem()
            for comment in comment_groups:
                shop_comment['id'] = calc_md5(comment)
                shop_comment['shopId'] = shopid
                shop_comment['userName'] = comment.get('userName')
                shop_comment['userUrl'] = comment.get('userUrl')
                shop_comment['avgPrice'] = comment.get('avgPrice')
                shop_comment['comment'] = comment.get('comment')
                shop_comment['merchantComment'] = comment.get('merchantComment')
                shop_comment['picUrls'] = comment.get('picUrls')
                shop_comment['commentTime'] = comment.get('commentTime')
                shop_comment['replyCnt'] = comment.get('replyCnt')
                shop_comment['zanCnt'] = comment.get('zanCnt')
                shop_comment['readCnt'] = comment.get('readCnt')
                shop_comment['userLevel'] = comment.get('userLevel')
                shop_comment['userId'] = comment.get('userId')
                shop_comment['uType'] = comment.get('uType')
                shop_comment['star'] = comment.get('star')
                shop_comment['quality'] = comment.get('quality')
                shop_comment['alreadyZzz'] = comment.get('alreadyZzz')
                shop_comment['reviewId'] = comment.get('reviewId')
                shop_comment['menu'] = comment.get('menu')
                shop_comment['did'] = comment.get('did')
                shop_comment['dealEndtime'] = comment.get('dealEndtime')
                shop_comment['anonymous'] = comment.get('anonymous')
                shop_comment['crawl_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                yield shop_comment

            offset += 10
            next_url = self.goods_comment_baseurl.format(shopid=shopid, offset=offset)
            page = page + 1
            self.get_shop_comment(next_url, shopid, offset, page)
