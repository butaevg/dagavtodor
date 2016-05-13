#coding: utf-8
from django.contrib.syndication.views import Feed
from django.utils.xmlutils import SimplerXMLGenerator
from django.utils.feedgenerator import Rss201rev2Feed

from django.utils import timezone
from pytz import timezone as tz
import datetime

from pressa.models import Post



class SXG(SimplerXMLGenerator):
    def addQuickElementCDATA(self, name, contents=None, attrs=None):
        if attrs is None: attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            self._write('<![CDATA['+contents+']]>')
        self.endElement(name)
        

class Rss(Rss201rev2Feed):
    def write(self, outfile, encoding):
        handler = SXG(outfile, encoding)
        handler.startDocument()
        handler.startElement(u"rss", self.rss_attributes())
        handler.startElement(u"channel", self.root_attributes())
        self.add_root_elements(handler)
        self.write_items(handler)
        self.endChannelElement(handler)
        handler.endElement(u"rss")

    # Добавляем тэги "yandex:logo" в которых мы дадим ссылке до логотипов 
    # нашего издания
    def add_root_elements(self, handler):
        super(Rss, self).add_root_elements(handler)
        handler.addQuickElement(u'yandex:logo', 'http://mixisport.com/media/img/rss/logo100.png',)     
        handler.addQuickElement(u'yandex:logo', 'http://mixisport.com/media/img/rss/logo180.png', {'type': 'square'})     

class RssYandex(Rss):
    def rss_attributes(self):
        attrs = super(RssYandex, self).rss_attributes()
        attrs.update({'xmlns:yandex':'http://news.yandex.ru', 'xmlns:media':'http://search.yahoo.com/mrss/'})
        return attrs
    
    # Добавляем кастомный тэг "yandex:full-text" в котором будем отдавать 
    # контент нашей статьи
    def add_item_elements(self, handler, item):
        if item['description'] is not None:
            handler.addQuickElement(u'yandex:full-text', item['description'])
        super(RssYandex, self).add_item_elements(handler, item)
        
class YandexRSS(Feed):
    feed_type = RssYandex
    title = "Агентство по дорожному хозяйству Республики Дагестан"
    description = "Новости дорожной отрасли Дагестана"
    
    link = "/"

    # Опытным путем удалось определить, что Яндексу интересны новости 
    # не старше 7 дней, все остальное при проверке он будет помечать как 
    # "плохая статья", поэтому выбираем статьи за 7 дней
    def items(self):
        return Post.objects.filter(putdate__gt=(timezone.now() - datetime.timedelta(days=9))).order_by('-putdate')
        #return Post.objects.order_by('-putdate')

    def item_title(self, item):
        return item.name

    # По-умолчанию будет отдаваться часовой пояс -0000, 
    # контент-менеджеру Яндекса этот момент не понравился и просили 
    # установить часовой пояс местонахождения сервера
    def item_putdate(self, item):
        return item.putdate.replace(tzinfo=tz('Etc/GMT+3'))

    def item_description(self, item):
        return item.body