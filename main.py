import pandas as pd
import matplotlib.pyplot as plt
from spider import MockWeiboSpider
from analyzer import SentimentAnalyzer

# 设置 Matplotlib 支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def main():
    # 1. 初始化组件
    spider = MockWeiboSpider()
    analyzer = SentimentAnalyzer()
    
    # 2. 获取数据
    raw_data = spider.fetch_data(count=100)
    
    # 3. 批量分析
    print("\n⚡ 正在进行 AI 情感研判...")
    results = []
    for item in raw_data:
        sentiment, confidence = analyzer.analyze(item['content'])
        item['sentiment'] = sentiment
        item['confidence'] = confidence
        results.append(item)
        
    # 4. 转换为 DataFrame 进行分析
    df = pd.DataFrame(results)
    
    # 5. 统计结果
    sentiment_counts = df['sentiment'].value_counts()
    
    print("\n📊 --- 舆情监控日报 ---")
    print(f"总处理数据量: {len(df)}")
    print("-" * 20)
    for label, count in sentiment_counts.items():
        emoji = "😄" if label == "Positive" else ("😠" if label == "Negative" else "😐")
        print(f"{emoji} {label}: {count} 条 ({count/len(df)*100:.1f}%)")
    
    # 6. 绘制饼图
    plt.figure(figsize=(8, 6))
    plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('今日全网舆情情感分布')
    plt.axis('equal')  # 保证是圆形
    plt.show()

if __name__ == "__main__":
    main()
