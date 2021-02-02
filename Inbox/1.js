import requests
import json

  url = "https://kd.youth.cn/TaskCenter/getSign";
  body = "cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzX2whIyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3dW2Fso6ar6m6apqGcXY&cookie_id=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzX2whIyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3dW2Fso6ar6m6apqGcXY&app_version=1.8.2&channel=80000000&device_type=1";
  headers = {
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://kd.youth.cn",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Connection": "keep-alive",
    "Referer": "https://kd.youth.cn/html/taskCenter/index.html?uuid=72c368f1c842c7ee64dd935cef8e2cef&sign=caabe69e9b6a8f107b11eff35b7292c1&channel_code=80000000&uid=53046201&channel=80000000&access=WIfI&app_version=1.8.2&device_platform=iphone&cookie_id=033aa39f67ec64c5183f86e84012e25a&openudid=72c368f1c842c7ee64dd935cef8e2cef&device_type=1&device_brand=iphone&sm_device_id=20210117174702dc03d4fe2a3786e8c335094d6a1a1f930154097f25a73432&device_id=49053187&version_code=182&os_version=14.3&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzX2whIyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3dW2Fso6ar6m6apqGcXY&device_model=iPhone_6_Plus&subv=1.5.1&&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzX2whIyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3dW2Fso6ar6m6apqGcXY&cookie_id=033aa39f67ec64c5183f86e84012e25a",
    "Content-Length": "297",
    "Cookie": "sensorsdata2019jssdkcross=%7B%22distinct_id%22%3A%2253046201%22%2C%22%24device_id%22%3A%221770fbe0c099aa-0518affe903e318-754c1451-370944-1770fbe0c0a9f8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221770fbe0c099aa-0518affe903e318-754c1451-370944-1770fbe0c0a9f8%22%7D; sajssdk_2019_cross_new_user=1"
};

try:
  r = requests.post (url, data = body, headers=headers);
  print(r.json())
except Exception as e:
  raise
else:
  pass
finally:
  pass
    
  
