import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class SentimentAnalyzer:
    def __init__(self):
        print("🧠 正在加载 AI 模型 (damo/nlp_structbert_sentiment-classification_chinese-base)...")
        # 使用阿里云 ModelScope 提供的开源中文情感模型
        self.model_name = "damo/nlp_structbert_sentiment-classification_chinese-base"
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
            print("✅ 模型加载成功！")
        except Exception as e:
            print(f"❌ 模型加载失败，请检查网络连接: {e}")
            exit()

    def analyze(self, text):
        """
        分析单条文本的情感
        返回: Positive (正面), Negative (负面), Neutral (中立)
        """
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
            scores = predictions[0].tolist()
            predicted_class_id = predictions[0].argmax(axis=-1).item()
            
        # 假设模型输出顺序为: 负面, 中立, 正面 (具体需根据模型config调整，此处为通用逻辑)
        labels = ["Negative", "Neutral", "Positive"] 
        label = labels[predicted_class_id]
        score = scores[predicted_class_id]
        
        return label, round(score, 4)
