# -*- coding:utf-8 -*-

class transCookies:
    def __init__(self,cookie):
        self.cookie=cookie


    def stringToDict(self):
        '''
            将从浏览器上copy来的cookie字符串转化为scrapy 能使用额dict
        :return:
        '''
        itemDict={}
        items=self.cookie.split(':')
        for item in items:
            key=item.split('=')[0].replace(' ','')
            value=item.split('=')[1]
            itemDict[key]=value

        return itemDict

if __name__=="__main__":
    cookie="BAIDU_SSP_lcr=https://www.baidu.com/link?url=0QO3RmeRtYKXGWh4u6zs0n2BOLzTaW6Jme5ZwYF4TX3YfadoUgvkF_YFgCnykTT8voutIeUOENdCN9enguqKnDh-tIlAekWWfODO1IUYPD3bhhLD0wQmlZnxHTljutf5&wd=&eqid=dcb06f790004c9d7000000055a0d2943; UM_distinctid=15cce9daf657fe-0670326daada3c-1d356f50-384000-15cce9daf66354; uuid_tt_dd=-841616479732546655_20170622; bdshare_firstime=1498119135267; CNZZDATA1261355189=1912297889-1498109920-%7C1499394264; Hm_lvt_58fa17220158547e682e9a2edc66c8e3=1498115060,1498119135,1498122351; Hm_lpvt_58fa17220158547e682e9a2edc66c8e3=1499397602; TY_SESSION_ID=dd0e6afe-84fe-4a03-86f5-ad5fa9246b11; UN=qq_39014292; UE=""; BT=1502677382999; Hm_lvt_3f9df99a208b69b45eb52cfbe2dc3bf8=1504597264; Hm_lpvt_3f9df99a208b69b45eb52cfbe2dc3bf8=1505191526; kd_user_id=ca0c2f60-8c3e-4530-8739-89f6e87f6b5e; __utma=17226283.229984346.1498813836.1498813836.1506755810.2; __utmc=17226283; __utmz=17226283.1498813836.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAAAOgif/BAAA1tFZdV7qNCDQszQR; CNZZDATA1259587897=1326973242-1509520202-https%253A%252F%252Fwww.baidu.com%252F%7C1509520202; shown_offset=8; kd_0e1a1f29-37da-4c44-8a33-b4735dc85f10_log_id=2d596075-f95a-4fab-a14b-b5633374c412%3Aa66d0abf-315b-4f5c-8bd2-499add110897%3A1b84858b-29ed-4b5b-b712-97f3c22c60c7; kd_0e1a1f29-37da-4c44-8a33-b4735dc85f10_view_log_id=da31b350-e977-4575-98ef-01ad58848d7b; kd_0e1a1f29-37da-4c44-8a33-b4735dc85f10_kuickDeal_pageIndex=0; kd_0e1a1f29-37da-4c44-8a33-b4735dc85f10_kuickDeal_leaveTime=1510730385405; __message_sys_msg_id=0; __message_gu_msg_id=0; __message_cnel_msg_id=0; __message_in_school=0; ViewMode=contents; ADHOC_MEMBERSHIP_CLIENT_ID1.0=b7ca93f3-1102-6e02-761b-6124cdd1dfbe; uuid=6d87d75d-a028-45d3-95b4-84e149e524b5; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1511417299,1511419487,1511487085,1511502153; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1511510498; dc_tos=ozwwyq"
    trans=transCookies(cookie)
    print (trans.stringToDict())