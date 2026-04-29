import random
import time
from datetime import datetime, timedelta

class MockWeiboSpider:
    """
    模拟微博爬虫
    在实际项目中，这里会替换为 scrapy.Spider 类，对接真实 API 或网页
    """
    def __init__(self):
        # 模拟一些热门话题的关键词
        self.topics = ["新款手机发布", "公司年终奖", "周末去哪玩", "某品牌食品安全"]
        self.templates = [
            "真的太棒了！强烈推荐大家尝试一下。",
            "简直是灾难，以后再也不会买了，非常失望。",
            "感觉一般般吧，没有想象中那么好，也没有那么差。",
            "这也太让人生气了！服务态度极其恶劣！",
            "还可以，性价比挺高的，值得入手。"
        ]

    def fetch_data(self, count=50):
        """抓取数据"""
        print(f"🕷️ 正在启动爬虫，目标抓取 {count} 条数据...")
        data_list = []
        
        for _ in range(count):
            # 模拟网络延迟
            time.sleep(0.05) 
            
            topic = random.choice(self.topics)
            content = f"关于{topic}：" + random.choice(self.templates)
            
            # 生成随机时间（过去24小时内）
            random_time = datetime.now() - timedelta(minutes=random.randint(0, 1440))
            
            data_list.append({
                "id": random.randint(10000, 99999),
                "content": content,
                "publish_time": random_time.strftime("%Y-%m-%d %H:%M:%S"),
                "source": "Weibo_Mock"
            })
            
        print("✅ 数据采集完成。")
        return data_list
