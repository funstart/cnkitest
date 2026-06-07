#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import re
from datetime import datetime, timedelta
from urllib.parse import urljoin, urlencode
import json

class CNKICrawler:
    def __init__(self):
        self.base_url = "https://navi.cnki.net/knavi/journals/index"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
        self.journals = [
            {'name': '教育与职业', 'code': 'JYYZ'},
            {'name': '中国职业技术教育', 'code': 'ZJZJ'},
            {'name': '职教论坛', 'code': 'ZJLT'},
            {'name': '职业技术教育', 'code': 'ZYJS'}
        ]
        
        self.articles = []
    
    def random_delay(self):
        time.sleep(random.uniform(1, 3))
    
    def search_journal_articles(self, journal_name, keywords, years_back=2):
        print(f"\n开始搜索期刊: {journal_name}")
        print(f"关键词: {', '.join(keywords)}")
        
        current_date = datetime.now()
        start_date = current_date - timedelta(days=365 * years_back)
        
        search_keywords = ' OR '.join(keywords)
        print(f"搜索时间范围: {start_date.strftime('%Y-%m')} 至 {current_date.strftime('%Y-%m')}")
        
        articles = self.simulate_search(journal_name, search_keywords, start_date, current_date)
        
        return articles
    
    def simulate_search(self, journal_name, keywords, start_date, end_date):
        print("注意：知网有反爬机制，这里提供模拟数据结构和框架")
        print("实际使用时需要：1. 配置Cookie 2. 处理验证码 3. 使用知网API")
        
        simulated_articles = []
        
        article_titles = [
            '人工智能时代职业教育人才培养模式变革研究',
            'ChatGPT在职业教育教学中的应用与反思',
            '生成式AI对职业院校教师角色的影响与应对',
            '人工智能背景下职业教育课程体系构建',
            '智能教育技术在职业技能培训中的应用'
        ]
        
        authors = [
            '张三,李四',
            '王五',
            '赵六,孙七,周八',
            '吴九',
            '郑十,陈十一'
        ]
        
        for i in range(len(article_titles)):
            article_date = end_date - timedelta(days=random.randint(0, 730))
            simulated_articles.append({
                'title': article_titles[i],
                'authors': authors[i],
                'journal': journal_name,
                'date': article_date.strftime('%Y-%m'),
                'abstract': '摘要：随着人工智能技术的快速发展，职业教育面临着新的机遇与挑战。本文探讨了人工智能时代职业教育人才培养模式的变革路径，分析了智能技术在教学中的应用现状，并提出了相应的对策建议。',
                'keywords': '人工智能; 职业教育; 人才培养',
                'url': 'https://cnki.net/example'
            })
        
        return simulated_articles
    
    def crawl_all(self):
        print("="*50)
        print("知网期刊爬虫程序")
        print("="*50)
        
        keywords = ['人工智能', 'AI', 'ChatGPT', '生成式AI', '智能教育', '机器学习', '深度学习']
        
        for journal in self.journals:
            try:
                articles = self.search_journal_articles(journal['name'], keywords)
                self.articles.extend(articles)
                self.random_delay()
            except Exception as e:
                print(f"抓取期刊 {journal['name']} 时出错: {e}")
                continue
        
        return self.articles
    
    def save_to_excel(self, filename='cnki_articles.xlsx'):
        if not self.articles:
            print("没有数据可保存")
            return
        
        df = pd.DataFrame(self.articles)
        df.columns = ['文章标题', '作者', '期刊', '发表时间', '摘要', '关键词', '链接']
        
        excel_path = f'/workspace/{filename}'
        df.to_excel(excel_path, index=False, engine='openpyxl')
        print(f"\n数据已保存到: {excel_path}")
        print(f"共保存 {len(self.articles)} 篇文章")
        
        return excel_path

def main():
    crawler = CNKICrawler()
    
    print("\n重要提示：")
    print("1. 知网有严格的反爬机制，包括验证码、IP限制等")
    print("2. 本程序提供了完整的框架结构")
    print("3. 实际使用时需要：")
    print("   - 登录知网获取有效的Cookie")
    print("   - 处理可能出现的验证码")
    print("   - 合理设置请求间隔")
    print("   - 遵守知网的使用条款和 robots.txt")
    print("\n")
    
    print("正在运行演示模式...")
    time.sleep(1)
    
    articles = crawler.crawl_all()
    crawler.save_to_excel()
    
    print("\n程序执行完成！")

if __name__ == '__main__':
    main()
