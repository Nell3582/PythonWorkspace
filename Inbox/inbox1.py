
import requests
import json
# import rsa
import base64
import time
from itertools import groupby
import hashlib
from datetime import datetime, timedelta
import os
import re
# 对应方案2: 下载到本地,需要此处填写

CookieYouth =[
'{"X-Requested-With":"XMLHttpRequest","Connection":"keep-alive","Accept-Encoding":"gzip, deflate, br","Content-Type":"application/x-www-form-urlencoded","Origin":"https://kd.youth.cn","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","Cookie":"sensorsdata2019jssdkcross=%7B%22distinct_id%22%3A%2246366889%22%2C%22%24device_id%22%3A%221720d24c659a23-03f9b6d6e568c4-724c1351-370944-1720d24c65a1147%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221720d24c659a23-03f9b6d6e568c4-724c1351-370944-1720d24c65a1147%22%7D; Hm_lvt_268f0a31fc0d047e5253dd69ad3a4775=1591606823,1591606833,1594107921,1594108077; Hm_lvt_6c30047a5b80400b0fd3f410638b8f0c=1589358673,1589358748,1589359001,1590415318","Host":"kd.youth.cn","Referer":"https://kd.youth.cn/html/taskCenter/index.html?uuid=44e514b8c81b6448bbdda59dc7d8022b&sign=13aab674074f6bf29ce9918a447495ca&channel_code=80000000&uid=46366889&channel=80000000&access=WIfI&app_version=1.7.6&device_platform=iphone&cookie_id=922bad827b2fe72798f2e32c7ae353dd&openudid=44e514b8c81b6448bbdda59dc7d8022b&device_type=1&device_brand=iphone&sm_device_id=20200513161155a2fa3f0e12281efbce2df867ae6af2c1010ee7100121ac90&version_code=176&os_version=13.4&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejlq-bsWSxzZtthoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupY7Knn7OFjJiXrs-2apqGcXY&device_model=iPhone_6_Plus&subv=1.5.1&&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejlq-bsWSxzZtthoyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupY7Knn7OFjJiXrs-2apqGcXY&cookie_id=922bad827b2fe72798f2e32c7ae353dd","Accept-Language":"zh-cn","Accept":"*/*","Content-Length":"297"}',
'{"Content-Type":"application/x-www-form-urlencoded","Accept-Encoding":"gzip, deflate, br","Cookie":"sensorsdata2019jssdkcross=%7B%22distinct_id%22%3A%2253046866%22%2C%22%24device_id%22%3A%221770fdd4654376-0cd46caa8efb51-754c1451-370944-1770fdd4655afb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221770fdd4654376-0cd46caa8efb51-754c1451-370944-1770fdd4655afb%22%7D; Hm_lvt_268f0a31fc0d047e5253dd69ad3a4775=1610878896; sajssdk_2019_cross_new_user=1","Connection":"keep-alive","Accept":"*/*","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","Referer":"https://kd.youth.cn/html/taskCenter/index.html?uuid=72c368f1c842c7ee64dd935cef8e2cef&sign=c6e78a360fa0549f00df2645d21e1825&channel_code=80000000&uid=53046866&channel=80000000&access=WIfI&app_version=1.8.2&device_platform=iphone&cookie_id=481d6ad9d1fc075fde77911ca2358d01&openudid=72c368f1c842c7ee64dd935cef8e2cef&device_type=1&device_brand=iphone&sm_device_id=20210117174702dc03d4fe2a3786e8c335094d6a1a1f930154097f25a73432&device_id=49053187&version_code=182&os_version=14.3&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualq2jmrCarWOw3XVphaKcmK_OqmqXr6NthJl7mI-shMmXeqDau4StacS3o7GFonrdsKnEZ4N5jWyEY2Ft&device_model=iPhone_6_Plus&subv=1.5.1&&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualq2jmrCarWOw3XVphaKcmK_OqmqXr6NthJl7mI-shMmXeqDau4StacS3o7GFonrdsKnEZ4N5jWyEY2Ft&cookie_id=481d6ad9d1fc075fde77911ca2358d01","Accept-Language":"zh-cn","X-Requested-With":"XMLHttpRequest"}',
'{"Accept":"*/*","X-Requested-With":"XMLHttpRequest","Accept-Language":"zh-cn","Accept-Encoding":"gzip, deflate, br","Content-Type":"application/x-www-form-urlencoded","Origin":"https://kd.youth.cn","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","Connection":"keep-alive","Referer":"https://kd.youth.cn/html/taskCenter/index.html?uuid=72c368f1c842c7ee64dd935cef8e2cef&sign=caabe69e9b6a8f107b11eff35b7292c1&channel_code=80000000&uid=53046201&channel=80000000&access=WIfI&app_version=1.8.2&device_platform=iphone&cookie_id=033aa39f67ec64c5183f86e84012e25a&openudid=72c368f1c842c7ee64dd935cef8e2cef&device_type=1&device_brand=iphone&sm_device_id=20210117174702dc03d4fe2a3786e8c335094d6a1a1f930154097f25a73432&device_id=49053187&version_code=182&os_version=14.3&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzX2whIyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3dW2Fso6ar6m6apqGcXY&device_model=iPhone_6_Plus&subv=1.5.1&&cookie=MDAwMDAwMDAwMJCMpN-w09Wtg5-Bb36eh6CPqHualIejl66rpWKxzX2whIyp4LDPyGl9onqkj3ZqYJa8Y898najWsJupZLC3dW2Fso6ar6m6apqGcXY&cookie_id=033aa39f67ec64c5183f86e84012e25a","Content-Length":"297","Cookie":"sensorsdata2019jssdkcross=%7B%22distinct_id%22%3A%2253046201%22%2C%22%24device_id%22%3A%221770fbe0c099aa-0518affe903e318-754c1451-370944-1770fbe0c0a9f8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221770fbe0c099aa-0518affe903e318-754c1451-370944-1770fbe0c0a9f8%22%7D; sajssdk_2019_cross_new_user=1"}',
]

# REDBODYs = [
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjazbBlBp4-3VBqIE6FTR2KhfyLVi7Pl1_m0wwPJgXu-Fmh7S-5HqV6o2kNNfxbTBdHNeGGUACeILyWR3zMN6Iw3IXfZs4Lu-yb9ynQmQje6lCx_IwxRVvI2SNym5MJ3oH5lFqmbtpdkJfwhB1sUJEdEgJ5iEwGnEtnWJDQPgSUh_43T95feCdA6znUBf7UdpUNuu05JsguiVtt7K_tT2UIuuVvof9Ue3GPhbcYOf2RkxK2Lm3EvI0o599EHSz8GOjyzbxSObMbWvZZwgkKHFQXVOzyoQTTWHFLADZSIgWXcViAEHw4v7N4JP82BlQXsKGgv4dNrEf1VdrUKNKxG3N6KDEB01P3CPua6FvVkUbard09CVB7EtXnTKT1tA6PN2ZnC18_44WENRdSnyX0OKFBy1isFDpep83gNvhCLoDvpAGgSJruf8zQD9GhS2XykfsYutxKDLen8fktWSwT5_OwekSn69xKRkyefjQBVGav9W0hJUtOL-MwuerrWpJXzjmMZiz-A-24K-bYLjCnU43GD3wnCYmVhLpAMqSoqxdkeIXTOz98GDS7xJhsXNsGWnl9noOZVMHcgiZGmuELMwt_kepT26mvBWj2mY8XEkYfGZB_l7BGgBKJj3rZwVZm-yEHoO7ZCEZo6LKP9p4m69bTYtUPXC7Ekp78_MKieZRMKyu_BeaURSSJmGPsVirO9onrMGwr1s7qZlr2Qr0QUsXEMd0mB-g4VO-hVocAezEqoQ1oYy48nNMBkKoSPpYSDZ_o6cMBfTpdLvkU6dy5xhbRWyrtSZB94xt0PjsuNWvU7KjiZNfij52VwKkAGVal0qPPtlfZVKXRrbA%3D%3D',
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjazbBlBp4-3VBqIE6FTR2KhfyLVi7Pl1_m0wwPJgXu-Fmh7S-5HqV6o1vMtEls8mPJh514T6M7mT424qvh8QrkxvplMO-SYOVD8eel3ty7vwxe_wa7ZfSZfXdjTiw3cbhIZT-OnIao6ZrF_hSdmQipG4Rvvz3nXQ6gK5CyHYI1D1-baeHBTpn7ijSSnjFXoXswynYfcRFREAK6HrLDYDIdu0oZIh0YNKqAVdXUyBTfE6kd6fc5T-hlFBv2LCI_iiLt9NSTeaGPX5E7QZ-3UBGxfQhaM577hsZs9F6gLr6zAiaip3_bx9APCAzfrdfUqaLKWJL3n-5JMkNWuLm9bMAR5ttUQ5kgUKNaDiXBMBILe-HPAEeZCjdjuNgV1-VfFstvEMl0g13vDwaMeBXY_-yie9XGrPEHDWApBYYniaZPOvUpc9r0RvdlRq7ArPvpTqM_eJ_Z50oa9pk6vcgpzMb821MjFD63LkQv9V4TEYyFznawlUhOQBg6tpO9pjzOaprXcZH4wzm_MXcPGEAGgNHrKDsVAhie2ql9-jLn5PhTrXOkLBWKAC19h7InJaQpyyzwakY8qiV6dpDfO845HeBGsK_XKD_GcKeG8mVhbJR3QFYauUNVGz_VQs7rA7wGFlpc7lq00wY5R6_69uR5NpV1DuusgsOpD48A_fMx4skEceX_vhMWnHhjbCXqBw8fTBrhDZoHjV1bpF2QauEgg4vQdroH1YDRfqoaWkNWtZpNmB7F0lip9nB_W81JMmJvnv2cWWqhriW8-R7D2Tj8MIsHAHg3Xx6-otIcOfyub87cJEV3a1brx2ld6DtlxWkkG95EGWy5Gp-Zfkw%3D%3D',
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjazbBlBp4-3VBqIE6FTR2KhfyLVi7Pl1_m0wwPJgXu-Fmh7S-5HqV6o1vMtEls8mPJh514T6M7mT424qvh8QrkxvplMO-SYOVD8eel3ty7vwxe_wa7ZfSZfXdjTiw3cbhIZT-OnIao6ZrF_hSdmQipG4Rvvz3nXQ6gK5CyHYI1D1-baeHBTpn7ijSSnjFXoXswynYfcRFREAK6HrLDYDIdu0oZIh0YNKqAVdXUyBTfE6kd6fc5T-hlFBv2LCI_iiLt9NSTeaGPX5E7QZ-3UBGxfQhaM577hsZs9F6gLr6zAiaip3_bx9APCAzfrdfUqaLKWJL3n-5JMkNWuLm9bMAR5ttUQ5kgUKNaDiXBMBILe-HPAEeZCjdjuNgV1-VfFstvEMl0g13vDwaMeBXY_-yie9XGrPEHDWApBYYniaZPOvUpc9r0RvdlRq7ArPvpTqM_eJ_Z50oa9pk6vcgpzMb821MjFD63LkQv9V4TEYyFznawlUhOQBg6tpO9pjzOaprXcZH4wzm_MXcPGEAGgNHrKVAPuemipaHgwDN-_jfIcJfH7ccvWxsyv3fp3_fkWpSglU30uBHpA5uulOWeJLzI6T0OMP6sYvsIu2IxqHkdSLf8600pVQGiyrClAOCxQazKlFbdJgWT57lSdsW--y51Ax_l__dGWM8LcKWzIZ4XOn_DQ9dgYIKdChVm6OpttWOVfoN4pH34zD6pgkfcI-RmmuJOZzdeRB8MWIyYJYp0PCRt6e2BRG4XbVYyDaNakfkJv3R2oge6Uokdn2UiJOD8UQ-77iROFq83jDoFlz59lycBdzv0_-FhGm3wj3hihyeMD0ywwl6mzQg%3D%3D',
# ]

# ARTBODYs =[
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmX9yDzh9viCys70pKCUuRrHMvec1dbf9in75vpmfRUgmDkIOIwmaDUdhG4A54HpMWDheruvLzPv_rPGu2Q9AFB4yDkWIoXwVphhPwsJlyeW6FpaILrvt_IAJarZJ6U4YhgWffkXZ0HLt0nTU-UB0NsK6rsVDjEy1qebHzCwfkXSh3ToP8zn1_g2AjH69qD2DrZvCavkUBMl09tZcd9I2GmyxCBI_o4kHaKPPyonpr8xM2ceK2a4tcsFqNCV4vsak1qmC3ghKH15aZSJy9wXVEX76Yaj4NYMcVi7t2eppd4nrdgfHeHis51a2dEPzSpUZ-cpnQCh1_3oupvSjzIljwL7YZEGXSVj044lgEpsCDy8uVKwG0p0j_iSAj8WTTJEjWP0Lzg961AP1D6wUd5khzGyE_qSMXBSotksVX6bQVjrflfYo_zBT0HJOijXRHMOtCdoSVec_PJiQT9OUAzYTEGeMdAJppziUOmt0OYlnbZGIWCwertWF86JeUY8wNMKmPDRLrSHXIHiUr7i7mICcTftRAK8FLpyaWjuW6MKNQOJbEfwIf-1t0vLMHHV2PHekl5Qte7whJ1ETspo4I07OCupt7A2njxtd7zj9v3bz5CBmdD2_5jrQ5oohj8bajinQrpqfBf8mbAG6UYKlQsp20u8PdsfIGmn8Lo1H4beNCltA%3D%3D',
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_kF97hamPuz4ZZk3rmRrVU_m2Z51XN3szZYaCPxNG07BYjyjwYkBVGTfTGYPVecze9u-jGHCQmfvey4yZrPyKR-cA01PbV3h61GBiHFc-skGrpoDK0eliCfJPX7f9_IVT-MEKcW_xpZA4LYK-zPANFjqRCwIjF9EEH7Kj7IudQYQD2OtIaZ_4Q5iaJIQgZGbpyURKdxm82vJFjI7CttJ649cgA-Nl0bB65gb7GBt3nXFoBtmaK7UuNbwoOedlFmrhMwDRB3U-S5p_M46c9pOov2ZD9XjH4vMi7_opBwkQ2jaReAI3kG03zWqz1imHcZwl36cMuXeW7jcIecQwnlc3CjXbKfDYHR-c_d3a-GgPZ3u3su7E0JGXj44dxS4cZRXVdeJW975BmKJxfjCN9fLd4GF7MSpLF5r6DcZ1zw2gJBfSyrfX5v21P1ZAUCXvCRkvRn7OWOg-IfTA5pkAyhDqFNeoAZ69yH_1pYwt7QT-eZpxIQyevKEBfmNeffgDIN4bEZzRs1rJ8kLkBXJPemTXxD82Gn9jXpf8RZjERp1oO4xuL7NBWqOwmM7x-ZTZeW1gjvi3mgJP78qbTjCx-uStrWDw4cgLmMYuWeGozEQrVtSWpdq-byYr99Ngwwd5fh2r86Q2Fom9fxlljsXkw78Va-oqZ8kHnu9LTgsBEhSlbGNJcU-JlWlBEuT9gs7f2MI5yfxxAJHGGZwLfGuJAIX2l0G9ecj4U7nxZQhOxQqjC0LY4sH12k1kGfbmLgkZR5y9GEIMO7sAy7609IPFspVCtK_tTsL6NH-RX_cb4rsmfNHYosAmi8R2iw%3D%3D',
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_kF97hamPuz4ZZk3rmRrVU_m2Z51XN3szZYaCPxNG07BYjyjwYkBVGTfTGYPVecze9u-jGHCQmfvey4yZrPyKR-cA01PbV3h61GBiHFc-skGrpoDK0eliCfJPX7f9_IVT-MEKcW_xpZA4LYK-zPANFjqRCwIjF9EEH7Kj7IudQYQD2OtIaZ_4Q5iaJIQgZGbpyURKdxm82vJFjI7CttJ649cgA-Nl0bB65gb7GBt3nXFoBtmaK7UuNbwoOedlFmrhMwDRB3U-S5p_M46c9pOov2ZD9XjH4vMi7_opBwkQ2jaReAI3kG03zWqz1imHcZwl36cMuXeW7jcIecQwnlc3CjXbKfDYHR-c_d3a-GgPZ3u3su7E0JGXj44dxS4cZRXVdeJW975BmKJxfjCN9fLd4GF7MSpLF5r6DcZ1zw2gJBfSyrfX5v21P1ZAUCXvCRkvRn7OWOg-IfTA5pkAyhDqFNeoAZ69yH_1pYwt7QT-eZpxIQyevKEBfmNeffgDIN4bEZzRs1rJ8kLkBXJPemTXxD82Gn9jXpf8RZjERp1oO4xuL7NBWqOwmM7x-ZTZeW1gjvi3mgJP78qbTjCx-uStrWDw4cgLmMYuWeGozEQrVtSWpdq-byYr99Ngwwd5fh2r86Q2Fom9fxlljsXkw78Va-oqZ8kHnu9LTgsBEhSlbGNJcU-JlWlBEuT9gs7f2MI5yfxxAJHGGZwLfGuJAIX2l0G9ecj4U7nxZQhOxQqjC0LY4sH12k1kGfbmLgkZR5y9GEIMO7sAy7609IPFspVCtK_tTsL6NH-RX_cb4rsmfNHYosAmi8R2iw%3D%3D',
# ]

# READTIME = [
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_nHSVk1s5Pk1lOQlYKzDUPU9y0FiOH2nIRqKp1NEljKT7rNHR8sm-zNM1uYF037ZLhJ3Xl0xswFUmY-cQ_hr0wixkQsFjVI3HBBKV9Vi7Arv9ucr9IYetIj9Zqs0mPLwQax27ryeUONmX9yDzh9viCys70pKCUuRrHMvec1dbf9in75vpmfRUgmDkIOIwmaDUdhG4A54HpMWDheruvLzPv_rPGu2Q9AFB4yDkWIoXwVo2XvtXYF6lnhT4HfLLzsNUjIjXlI7CGaf_dcxME_x9bmYg2o2wOAgeIVJ9PGB_xffMaz56FxkBvAL9C3Is-slMjCtOoHFY3rYmnh27uf0kAOJZcDhDAZb1Q1oyqOlQB7pLZLxtScm0Y8BDiact0jpPZweI7gvep3sbATkPqDs9nEImOJ90Kp-tFJPHTdZImSBFPV8VZjAn0C4XfOW6cLclMaw3YKrXUEOKjwD9BC_5j12gJpOsHI_gRYyoQ6dCOMaO-qsMhffqhaaxpCQkTTmGLLyb16ui_xzgWSeoUBOomb3igcdtRQVYAGatMYP-KJWNSec4wwelnTSJK8_SQzwpPBcL4OajenJ5gk0_77wh6OacOv_Wgf8_lrcwQ8t_xmq_kUNQOOUV70Dg1dqV0VaZc9ynAl1HfwGv8GCdz76DhN7XBWkoJ16yBZRQOgOOrG-66wHEKu7Kte7vK92RupSgqdRILcNwNB9vkQrB75yAPHLNV_BtEwj3XsaE1XXi_-l7W5U1i9mdRKgIEcBIWrFRQ_NeV55ZA80POgVVmTfqG_Y40wjLlLbZqMsMMFUigds%3D',
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_kF97hamPuz4ZZk3rmRrVU_m2Z51XN3szZYaCPxNG07BYjyjwYkBVGTfTGYPVecze9u-jGHCQmfvey4yZrPyKR-cA01PbV3h61GBiHFc-skGrpoDK0eliCfJPX7f9_IVT-MEKcW_xpZA4LYK-zPANFjqRCwIjF9EEH7Kj7IudQYQD2OtIaZ_4Q5iaJIQgZGbpyURKdxm82vJFjI7CttJ649cgA-Nl0bB65gb7GBt3nXEzjE-AKmGdQzaFVCp5T4exgNOtCkUFQa9T6DxO8TN5km4BQXhhFefz0gSiP_pCMORD_wHuHfq3eRTiERbtdY9UOtnNE9pc1lwxk5vD7xqf5RwNgITuRVtwvD4NTMhmsZcd7J-vGoU8qL676fmQlY5PdYZwuqCbEWKjjwckM42GitEb56rEguCTAYNZl61H5PcWxKgvhlFTpDNnwtSVD6dQo7gIUsnBaSkhhpZWTbS1iL2ibfy-HvKVxEQPR9iatB7xppvpa6FbK2UrO49lf1yamvX8QxoJao7H26Iz87kdZ7cqwpTIVKVo07wvwvRMYIi60huaEQp4KFlpfpxCXtxdUVHD-YUlyyEISgVW1Ljtum4kcl_v4piOo312vyiVMB_0xvfr3E1SIpXxK99qmwgRHEXnyTZV78TqP4JleFFkCgwagVx91cIxXgQkMIInYhY3sCgBwA6HAOGaGlHgBEYgIQ6HNxEY8gvBPP2seRYnqzps4Ckxmg8bUUd3rX73Af9EoijyfS63UKexOn5KrIw-DjzfrYbtlxFQpvsZSz-Tl22vjvvLC3PooUFqsHrJn9c%3D',
# 'p=9NwGV8Ov71o%3DgW5NEpb6rjb84bkaCQyOq-myT0C-Ktb_kF97hamPuz4ZZk3rmRrVU_m2Z51XN3szZYaCPxNG07BYjyjwYkBVGTfTGYPVecze9u-jGHCQmfvey4yZrPyKR-cA01PbV3h61GBiHFc-skGrpoDK0eliCfJPX7f9_IVT-MEKcW_xpZA4LYK-zPANFjqRCwIjF9EEH7Kj7IudQYQD2OtIaZ_4Q5iaJIQgZGbpyURKdxm82vJFjI7CttJ649cgA-Nl0bB65gb7GBt3nXEzjE-AKmGdQzaFVCp5T4exgNOtCkUFQa9T6DxO8TN5km4BQXhhFefz0gSiP_pCMORD_wHuHfq3eRTiERbtdY9UOtnNE9pc1lwxk5vD7xqf5RwNgITuRVtwvD4NTMhmsZcd7J-vGoU8qL676fmQlY5PdYZwuqCbEWKjjwckM42GitEb56rEguCTAYNZl61H5PcWxKgvhlFTpDNnwtSVD6dQo7gIUsnBaSkhhpZWTbS1iL2ibfy-HvKVOAkywO1S7vM9FLKGXmQrlMX5vp6Ttd7Jc8PhLjSuC6PSb69c91e1Wy3NkgrsSW75NpqBgpHxn4Q35N0YE1PKB0Az2RmODP1FXMmKXBLs6Rk1aYHzC6NBlbySWRUMW7XNIgcM6q2LIhir61Oe0g6eC5e5PH4W86KhB7RBh7rvbn1xdfxPbEzZ-0dgCiQ23jqNb0Ftp0UeJSBimiZhDvGB6M9JTbVJAp4hW7NLLsbzGq5qd_0NHEn1ZeES88is5TCO_UTfQdLid_o0iirhG3KmBT0KT5JG1UC3bBafmF0E_QMnp08v6w1C7JMjDS3xtIekR38nJAM9ses%3D',
# ]


# 通知服务
BARK = ''                   # bark服务,自行搜索; secrets可填;形如jfjqxDx3xxxxxxxxSaK的字符串
SCKEY = ''                  # Server酱的SCKEY; secrets可填
TG_BOT_TOKEN = ''           # telegram bot token 自行申请
TG_USER_ID = ''             # telegram 用户ID
# 对应方案1:  GitHub action自动运行,此处无需填写;
if "XMLY_SPEED_COOKIE" in os.environ:
    """
    判断是否运行自GitHub action,"XMLY_SPEED_COOKIE" 该参数与 repo里的Secrets的名称保持一致
    """
    print("执行自GitHub action")
    xmly_speed_cookie = os.environ["XMLY_SPEED_COOKIE"]
    cookiesList = []  # 重置cookiesList
    for line in xmly_speed_cookie.split('\n'):
        if not line:
            continue
        cookiesList.append(line)
    # GitHub action运行需要填写对应的secrets
    if "BARK" in os.environ and os.environ["BARK"]:
        BARK = os.environ["BARK"]
        print("BARK 推送打开")
    if "SCKEY" in os.environ and os.environ["SCKEY"]:
        BARK = os.environ["SCKEY"]
        print("serverJ 推送打开")
    if "TG_BOT_TOKEN" in os.environ and os.environ["TG_BOT_TOKEN"] and "TG_USER_ID" in os.environ and os.environ["TG_USER_ID"]:
        TG_BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
        TG_USER_ID = os.environ["TG_USER_ID"]
        print("Telegram 推送打开")

headers = CookieYouth[0]
print(headers)
def Sign():
	try:
		r = requests.post('http://kd.youth.cn/TaskCenter/sign',json=headers)
		print(r.json())
		if r.status_code == 2:
			print('签到失败，Cookie已失效‼️')
			return;
		elif r.status_code == 1:
			print('签到成功，明日{nextScore}'.format('nextScore':r.nextScore))
		elif r.status_code == 0:
			print('今日已签过到了，无需重复签到')


	except:
		print("")




	