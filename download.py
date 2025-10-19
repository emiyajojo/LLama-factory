from modelscope import snapshot_download
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# 下载模型（Qwen3-4B），指定缓存目录为当前路径下的Qwen3-4B文件夹
model_dir = snapshot_download("Qwen/Qwen3-4B", cache_dir="./Qwen3-4B")
print('模型下载后保存路径: ', model_dir)

# # 加载下载好的模型和对应的分词器
# model = AutoModelForCausalLM.from_pretrained(model_dir, trust_remote_code=True)
# tokenizer = AutoTokenizer.from_pretrained(model_dir)

# # 检测并使用GPU（若存在），否则使用CPU
# device = "cuda" if torch.cuda.is_available() else "cpu"
# print('当前使用的设备: ', device)
# model = model.to(device)

# # 测试模型生成功能，验证模型加载是否成功
# input_text = "你好啊,千问..."
# inputs = tokenizer(input_text, return_tensors="pt").to(device)
# outputs = model.generate(**inputs)
# # 解码生成结果并打印（跳过特殊token）
# print("模型测试生成结果: ", tokenizer.decode(outputs[0], skip_special_tokens=True))
