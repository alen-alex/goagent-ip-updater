# -*- coding:utf8 -*-
from utils.config import config_thread_num
from utils.common import adapt_encoding
from utils.connect import filter_useful_ip
from utils.io import get_iplist,update_ini

def main():
    try:
        thread_num = config_thread_num()
        ip_file = "iplist.lst"
        iplist = get_iplist(ip_file)
        useful_ip = filter_useful_ip(iplist,thread_num)
    except Exception as e:
        print(e)
    else:
        try:
            ini_file = "local/proxy.ini"
            update_ini(useful_ip,ini_file)
        except IOError as e:
            ip_file = "output.txt"
            with open(ip_file, 'wb') as f:
                text='|'.join(useful_ip)
                f.write(text)
            print(adapt_encoding("请将程序放在goagent目录下，"+
                "与local和server文件夹并列，以自动更新goagent配置文件"))
        except Exception as e:
            print(e)
        else:
            print(adapt_encoding("配置文件更新成功，请重启goagent服务"))
    exit()

def exit():
    print(adapt_encoding("输入回车退出..."))
    a = raw_input()

if __name__ == '__main__':
    main()