import wikipedia
import re
import time
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


# get wikipedia article page content
def get_wikipedia_plain_text(title):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts",
        "explaintext": True
    }

    # 设置重试策略
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])

    session = requests.Session()
    session.mount('https://', HTTPAdapter(max_retries=retries))

    response = session.get(base_url, params=params, timeout=10)  # 设置超时为10秒
    data = response.json()
    page = next(iter(data['query']['pages'].values()))
    return page.get('extract', '')


def clean_text(text):
    # 去除 \n 字符
    text = text.replace('\n', ' ')
    # 去除数字标号和 [] 符号
    text = re.sub(r'\[\d+\]', '', text)
    return text

# re 
def count_keyword_occurrences(text, keyword):
    # 使用正则表达式计数关键字A的出现次数
    # \b 表示单词边界，确保匹配到的是一个独立的单词
    # 这里是完全匹配
    #return len(re.findall(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE))
    return text.lower().count(keyword.lower())
    # 在文章里包含该字段
    
# 传入文本text，和要查询的字段 keyword 即可
# count_keyword_occurrences(text, keyword)
# 上述计数不为0，就表示B出现在A相关概念的article中

# 分母是 所有和A相关的关键字的权重
# 分子是 B是否出现了，出现了就保留，不出现就不加权重
# 得到的是一个0-1之间的数

def get_A_cite_B(keyword_A_list,keyword_B,weight_list_A):
    refd_A_B_1 = 0
    refd_A_B_2 = 0

    for i in range(len(keyword_A_list)):
        content_A = get_wikipedia_plain_text(keyword_A_list[i])
        content_A = clean_text(content_A)
        #time.sleep(5)
        count_B = count_keyword_occurrences(content_A, keyword_B)
        if count_B !=0:
            # B的数量多于0，就指定为1
            # 否则，指定为0
            refd_A_B_1 += weight_list_A[i]*1
        else:
            refd_A_B_1 = refd_A_B_1
        refd_A_B_2 += weight_list_A[i]
    return refd_A_B_1/refd_A_B_2

# get_A_cite_B(keyword_B_list,keyword_A,weight_list_B) 获得的就是B相关概念对A的引用
# get_A_cite_B(keyword_A_list,keyword_B,weight_list_A) A对B