from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline,DropItem

class HelloPipeline:
    def process_item(self, item, spider):
        return item

class imagepipline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        url=request.url
        file_name=url.split("/")[-1]
        return file_name
    def item_completed(self, results, item, info):
        img_paths=[x["path"] for ok,x in results if ok]
        if not img_paths:
            raise  DropItem("failed")
        return item

    def get_media_requests(self, item, info):
        yield Request(item["url"])