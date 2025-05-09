import pickle
import ipaddress
from collections import defaultdict

# 读取你的 txt 文件
with open("3_give.txt", "r") as f:
    seeds = [line.strip() for line in f if line.strip()]

# 按 BGP 前缀分类（这里假设前缀是 /32，你可以调整）
prefix_dict = defaultdict(list)
for addr in seeds:
    ip = ipaddress.IPv6Address(addr)
    prefix = f"{ip.exploded[:10]}::/48"  # 例如 2001:0001:abde::/32
    prefix_dict[prefix].append(addr)

# 保存为 .pkl 文件
with open("new_allseeds.pkl", "wb") as f:
    pickle.dump(dict(prefix_dict), f)