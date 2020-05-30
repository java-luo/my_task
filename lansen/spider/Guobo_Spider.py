import requests
import time
from lansen.util import SpiderUtil
from lansen.message import my_message
import threading

"""国家博物馆爬虫类"""
headers = {
    "Referer": "http://ticket.chnmuseum.cn/yuyue/index",
    "Origin": "http://ticket.chnmuseum.cn",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "User-Agent": SpiderUtil.get_user_agent()
}


# 场次
ticket_date = {}
# 票量
ticket_number = []
# 已提醒列表
send_success = []
# 爬虫是否正常
spider_is_ok = True

"""获取国家博物馆票数据"""

def init_ticker():
    global send_success
    for ticket in ticket_number:
        # print("日期%s 票量%s" %(ticket['t_date'],ticket['tp_last_stock_sum']))
        for t in ticket['tp']:
            # print(t['tp_last_stock'],type(t['tp_last_stock']))
            if ((t['tp_last_stock'] < 200) & (t['td_tp_id'] not in send_success)):
                send_success.append(t['td_tp_id'])


def get_ticket():
    global spider_is_ok
    #
    try:
        reponse = requests.get("https://ticketapi.chnmuseum.cn/api/ticket/calendar?p=w", headers=headers)
        if (reponse.status_code != 200):
            message = "国博请求异常,HTTP响应码:%s" % reponse.status_code
            # 发送提醒
            my_message.ifttt_send_meaasge({"value1": message})
            spider_is_ok = False
        if (reponse.json()['status'] != 1):
            message = "国博请求异常,JSON响应码为:%s" % reponse.json()['status']
            # 发送提醒
            my_message.ifttt_send_meaasge({"value1": message})
            spider_is_ok = False
    except Exception as e:
        # 发送提醒
        message = "国博程序发生异常:%s" % e
        my_message.ifttt_send_meaasge({"value1": message})
        spider_is_ok = False
    return reponse.json()


"""解析国家博物馆票数据"""


def analysis(data):
    global ticket_date, ticket_number
    ticket_tps = data['data']['tps']
    for tps in ticket_tps:
        ticket_date[tps['tp_id']] = tps['time_period_show']
    ticket_number = data['data']['yy_date']


"""检查票量"""


def check_ticket_number():
    global send_success
    for ticket in ticket_number:
        # print("日期%s 票量%s" %(ticket['t_date'],ticket['tp_last_stock_sum']))
        for t in ticket['tp']:
            # print(t['tp_last_stock'],type(t['tp_last_stock']))

            if ((t['tp_last_stock'] < 200) & (t['td_tp_id'] not in send_success)):
                msg = "%s日%s场,仅剩余%s张,注意关班!!!" % (ticket['t_date'], ticket_date[t['tp_id']], t['tp_last_stock'])
                my_message.ifttt_send_meaasge({"value1": msg})
                send_success.append(t['td_tp_id'])


def init():
    data = get_ticket()
    analysis(data)
    init_ticker()

def start():
    data = get_ticket()
    analysis(data)
    check_ticket_number()




# my_message.ifttt_send_meaasge({"Value1":"message"})




