import scrapy
import time
import json


class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open("github.jl", "w", encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(item)
        self.file.write(f"{line}\n")
        return item



# Gajesh Bhat, https://gist.github.com/gajeshbhat/67a3db79a6aecd1db42343190f9a2f17
def convert_str_to_number(x):
    if x:
        total_nums = 0
        num_map = {"K": 1000, "M": 1000000, "B": 1000000000}
        if x.isdigit():
            total_nums = int(x)
        else:
            if len(x) > 1:
                total_nums = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
        return int(total_nums)
    else:
        return 0






class GitpySpider(scrapy.Spider):
    name = "gitpySpider"
    allowed_domains = ['github.com']
    custom_settings = {
        "ITEM_PIPELINES": {JsonWriterPipeline: 401},
        "CONCURRENT_REQUESTS": 1,
        "DOWNLOAD_TIMEOUT": 1800,
        # 'LOG_LEVEL': 'DEBUG',
        # 'LOG_FILE': 'log_%s.txt' % time.time(),  # 配置的日志
    }


    def start_requests(self):
        urls = ["http://github.com/topics/python?page=1"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        article = response.css("article.color-bg-secondary")
        for i, repos in enumerate(article):
            user, proj = repos.css("h3 a::text").getall()[:2]  # 用户和项目名称
            star = repos.css("a.social-count::text").get()
            primary = repos.css("div.color-bg-primary.rounded-bottom-1")
            about = primary.css("div.px-3.pt-3 div::text").get()

            proj_page = repos.css("h3 a[data-ga-click='Explore, go to repository, location:explore feed']::attr(href)").get()
            proj_page_link = f"http://github.com{proj_page}"

            item = dict({
                "user": user and user.strip(),                             # 上传者
                "proj": proj and proj.strip(),                             # 项目名
                "star": star and convert_str_to_number(star.strip()),      # 收藏数
                "proj_page_link": f"http://github.com{proj_page}",         # 项目地址
                "about": about and about.strip(),                          # 项目简介
            })

            yield scrapy.Request(url=proj_page_link, callback=self.parse_proj, cb_kwargs=dict(quote=item))   # 进入项目详情页

        time.sleep(1)
        next_page = response.css("body main form.ajax-pagination-form.js-ajax-pagination input::attr(value)").get()
        if next_page:  # 翻页
            next_url = f"http://github.com/topics/python?page={next_page}"
            yield scrapy.Request(url=next_url, callback=self.parse)





    def parse_proj(self, response, quote):  # 进入项目页爬取信息

        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        def extract_with_allcss(query):   # 获取所有元素
            return list(map(str.strip, response.css(query).getall()))

        def extract_with_allcss_zip(query):  # 打包键值对（用于爬取语言组成）
            kv = response.css(query).getall()
            if kv:
                keys = []
                values = []
                for i in range(0, len(kv), 2):
                    keys.append(kv[i])
                    values.append(kv[i + 1])
                return list(zip(map(str.strip, keys), map(str.strip, values)))
            else:
                return []

        Readme_text = extract_with_css("article[class='markdown-body entry-content container-lg']::text")
        fork_num = extract_with_css("body main ul li a[href$='network/members']::text")
        Releases_num = extract_with_css("h2[data-pjax^='#repo']  a span[data-view-component='true']::text")
        branches_num = extract_with_css("a[href$='branches'] strong::text")
        Contributors_num = extract_with_css("div[class='BorderGrid-cell'] h2 a[href$='contributors'] span::text")

        quote.update(
            {
                "Readme": Readme_text,                                                     # Readme
                "fork": convert_str_to_number(fork_num),                                   # 复刻数
                "Releases": convert_str_to_number(Releases_num),                           # 发行数
                "branches": branches_num,                                                  # 分支数
                "Contributors": Contributors_num,                                          # 贡献者数量
                "toptags": extract_with_allcss("div[class='f6'] a[data-ga-click='Topic, repository page']::text"),      # 主题标
                "Languages": extract_with_allcss_zip("ul[class='list-style-none'] a[class^='d-inline'] span::text"),    # 语言构成

            }
        )
        time.sleep(1)
        issues_page_link = f"{quote['proj_page_link']}/issues"
        yield scrapy.Request(url=issues_page_link, callback=self.parse_proj_issues, cb_kwargs=dict(quote=quote))


    def parse_proj_issues(self, response, quote):
        def extract_with_css(query):
            res = response.css(query).getall()
            if res:
                return res[-1].split()[0].strip()  # 去除多余部分，只取出数字
            else:
                return 0

        quote.update(
            {
                "issues_open_num": extract_with_css("div[class$='no-wrap'] div[class^='table-list-header'] a[data-ga-click$='Open']::text"),     # 开放议题数
                "issues_closed_num": extract_with_css("div[class$='no-wrap'] div[class^='table-list-header'] a[data-ga-click$='Closed']::text")  # 关闭议题数
            }
        )
        time.sleep(1)
        pulls_page_link = f"{quote['proj_page_link']}/pulls"
        yield scrapy.Request(url=pulls_page_link, callback=self.parse_proj_pulls, cb_kwargs=dict(quote=quote))


    def parse_proj_pulls(self, response, quote):
        def extract_with_css(query):
            res = response.css(query).getall()
            if res:
                return res[-1].split()[0].strip()  # 去除多余部分，只取出数字
            else:
                return 0

        quote.update(
            {
                "pulls_open_num": extract_with_css("div[class^='d-block'] a[href$='pr']::text"),        # 开放拉取请求数
                "pulls_closed_num": extract_with_css("div[class^='d-block'] a[href$='closed']::text")   # 关闭拉取请求数
            }
        )
        time.sleep(1)
        dependency_page_link = f"{quote['proj_page_link']}/network/dependencies"
        yield scrapy.Request(url=dependency_page_link, callback=self.parse_proj_dependency, cb_kwargs=dict(quote=quote))


    def parse_proj_dependency(self, response, quote):
        def extract_with_allcss(query):  # 获取所有元素
            return list(map(str.strip, response.css(query).getall()))

        quote.update(
            {
                "dependency": extract_with_allcss("div[class^='Box-row'] span a span::text")        # 依赖项
            }
        )
        print(f"***************************************** 项目'{quote['proj']}'已爬取完毕 *****************************************")
        yield quote





from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(GitpySpider)
process.start()

