import requests
import json
def translate(content,source_lang='auto',target_lang='en-US'):
    url = 'https://open.bigmodel.cn/api/v1/agents'
    print(source_lang,target_lang)
    try:
        payload = {
            "agent_id": "general_translation",
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ],
            "stream": False,
            "custom_variables": {
                "source_lang": source_lang,
                "target_lang": target_lang,
                "strategy": "general",
                "strategy_config": {
                    "general": { "suggestion": "专业技术文档翻译风格" },
                    "cot": { "reason_lang": "to" }
                }
            }
        }
        headers = {
            "Authorization": "Bearer 0a9a351dd6f4454681db9075d6be6e2d.3CafKJEVKVBBBuCE",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        result = response.json()
        return result['choices'][0]['messages'][0]['content']['text']
        # return json.dumps(result, ensure_ascii=False, indent=2)
    except Exception as e:
        return str(e)

def bind_target_lang(target_lang_comboBox):
    target_lang_comboBox.addItems([
    "中文（简体，中国大陆地区）",
    "中文（繁体，中国台湾地区）",
    "文言文",
    "粤语（广东话）",
    "英语",
    "英语（英国）",
    "英语（美国）",
    "日语",
    "韩语（朝鲜语）",
    "法语",
    "德语",
    "西班牙语",
    "俄语",
    "葡萄牙语",
    "意大利语",
    "阿拉伯语",
    "印地语",
    "保加利亚语",
    "捷克语",
    "丹麦语",
    "希腊语",
    "爱沙尼亚语",
    "芬兰语",
    "匈牙利语",
    "印尼语",
    "立陶宛语",
    "拉脱维亚语",
    "荷兰语",
    "挪威语",
    "波兰语",
    "罗马尼亚语",
    "斯洛伐克语",
    "斯洛文尼亚语",
    "瑞典语",
    "泰语",
    "土耳其语",
    "乌克兰语",
    "越南语",
    "缅甸语",
    "马来语",
    "汉语拼音",
    "国际音标"
])

def change_target_lang(target_lang):
    print(target_lang)
    match target_lang:
        case '中文（简体，中国大陆地区）':
            return 'zh-CN'
        case '中文（繁体，中国台湾地区）':
            return 'zh-TW'
        case '文言文':
            return 'wyw'
        case '粤语（广东话）':
            return 'yue'
        case '英语':
            return 'en-US'
        case '英语（英国）':
            return 'en-GB'
        case '英语（美国）':
            return 'en-US'
        case '日语':
            return 'ja'
        case '韩语（朝鲜语）':
            return 'ko'
        case '法语':
            return 'fr'
        case '德语':
            return 'de'
        case '西班牙语':
            return 'es'
        case '俄语':
            return 'ru'
        case '葡萄牙语':
            return 'pt'
        case '意大利语':
            return 'it'
        case '阿拉伯语':
            return 'ar'
        case '印地语':
            return 'hi'
        case '保加利亚语':
            return 'bg'
        case '捷克语':
            return 'cs'
        case '丹麦语':
            return 'da'
        case '希腊语':
            return 'el'
        case '爱沙尼亚语':
            return 'et'
        case '芬兰语':
            return 'fi'
        case '匈牙利语':
            return 'hu'
        case '印尼语':
            return 'id'
        case '立陶宛语':
            return 'lt'
        case '拉脱维亚语':
            return 'lv'
        case '荷兰语':
            return 'nl'
        case '挪威语':
            return 'no-'
        case '波兰语':
            return 'pl'
        case '罗马尼亚语':
            return 'ro'
        case '斯洛伐克语':
            return 'sk'
        case '斯洛文尼亚语':
            return 'sl'
        case '瑞典语':
            return 'sv'
        case '泰语':
            return 'th'
        case '土耳其语':
            return 'tr'
        case '乌克兰语':
            return 'uk'
        case '越南语':
            return 'vi'
        case '缅甸语':
            return 'my'
        case '马来语':
            return 'ms'
        case '汉语拼音':
            return 'PinYin'
        case '国际音标':
            return 'IPA'
if __name__ == '__main__':
    print(translate('我是一个学生'))