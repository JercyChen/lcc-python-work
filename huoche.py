# -*- coding: utf-8 -*-
"""
@author: Akagi201
"""

from splinter.browser import Browser
from time import sleep
import traceback

###�ݴ����Ĳ��ã����ǵ����Ҳ�����࣬��Ҽ���

# �û���������
username = u"�ĳ��û���"
passwd = u"�ĳ��û���"
# cookiesֵ���Լ�ȥ��, ���������ֱ����Ϻ�, Ӫ�ڶ�
starts = u"%u4E0A%u6D77%2CSHH"
ends = u"%u8425%u53E3%u4E1C%2CYGT"
# ʱ���ʽ2016-01-31
dtime = u"2016-02-01"
# ���Σ�ѡ��ڼ��ˣ�0�����֮�����ε��
order = 0
###�˿���
pa = u"�ĳɳ˿�����"

"""��ַ"""
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"


def login():
    b.find_by_text(u"��¼").click()
    sleep(3)
    b.fill("loginUserDTO.user_name", username)
    sleep(1)
    b.fill("userDTO.password", passwd)
    sleep(1)
    print u"�ȴ���֤�룬��������..."
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break

def huoche():
    global b
    b = Browser(driver_name="chrome")
    b.visit(ticket_url)

    while b.is_text_present(u"��¼"):
        sleep(1)
        login()
        if b.url == initmy_url:
            break

    try:
        print u"��Ʊҳ��..."
        # ���ع�Ʊҳ��
        b.visit(ticket_url)

        # ���ز�ѯ��Ϣ
        b.cookies.add({"_jc_save_fromStation": starts})
        b.cookies.add({"_jc_save_toStation": ends})
        b.cookies.add({"_jc_save_fromDate": dtime})
        b.reload()

        sleep(2)

        count = 0
        # ѭ�����Ԥ��
        if order != 0:
            while b.url == ticket_url:
                b.find_by_text(u"��ѯ").click()
                count +=1
                print u"ѭ�������ѯ... �� %s ��" % count
                sleep(1)
                try:
                    b.find_by_text(u"Ԥ��")[order - 1].click()
                except:
                    print u"��û��ʼԤ��"
                    continue
        else:
            while b.url == ticket_url:
                b.find_by_text(u"��ѯ").click()
                count += 1
                print u"ѭ�������ѯ... �� %s ��" % count
                sleep(1)
                try:
                    for i in b.find_by_text(u"Ԥ��"):
                        i.click()
                except:
                    print u"��û��ʼԤ��"
                    continue
        sleep(1)
        b.find_by_text(pa)[1].click()
        print  u"�����Ķ�����.....���ٶ�����������κβ���"
    except Exception as e:
        print(traceback.print_exc())

if __name__ == "__main__":
    huoche()