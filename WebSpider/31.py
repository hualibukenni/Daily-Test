import requests
headers = {
    'Cookie':'tgw_l7_route=bc9380c810e0cf40598c1a7b1459f027; _xsrf=7363fc9f-dcb0-410d-ba42-c53b23d93631; d_c0="AKAlQdqpwA2PTlEphog8uQpnT2mlMS0GSq0=|1529047727"; q_c1=5b7db1aec399441ab487747fa6cf3522|1529047727000|1529047727000; _zap=3c17861c-b9ef-4304-9692-ef10695049dd; capsion_ticket="2|1:0|10:1529047744|14:capsion_ticket|44:NjhkOTI3YjAwMzlkNDU2ZGFjN2E0NTFmY2RiYWE1NDg=|f976387110e0137522fb212b5f54a06c5bce18393327fe99aeab687be4814bfc"; z_c0="2|1:0|10:1529047765|4:z_c0|92:Mi4xaDdWZ0FRQUFBQUFBb0NWQjJxbkFEU1lBQUFCZ0FsVk4xYmdRWEFBSUY2SG1BdHVKVVBqSmlJbzR0Q3o4MjFDQUFR|5cc24bd015594fb1e5fc11983db3088d6eb35b6bfe6b5ec1b8307f60c4be69db"',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)
