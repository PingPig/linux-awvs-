import time

class define:
    GREEN       = "\033[32m"
    RED         = "\033[0;31m"
    BLUE        = "\033[94m"
    ORANGE      = "\033[33m"
    host        = "https://139.155.128.39:13443/"     #端口后面一定要加/
    api_key     = "1986ad8c0a5b3df4d7028d5f3c06e936ce89a21c1265241f8bdfbb819fa299055"                            #替换此处apikey
    api_header  = {'X-Auth':api_key,'content-type':'application/json'}
    filename    = 'out/%s.xlsx' % time.strftime("%Y-%m-%d-%H-%M", time.localtime(time.time()))
    awvs_scan_rule = {
                "full": "11111111-1111-1111-1111-111111111111",
                "highrisk": "11111111-1111-1111-1111-111111111112",
                "XSS": "11111111-1111-1111-1111-111111111116",
                "SQL": "11111111-1111-1111-1111-111111111113",
                "Weakpass": "11111111-1111-1111-1111-111111111115",
                "crawlonly": "11111111-1111-1111-1111-111111111117"
                    }
    banner = '''

                             __..--.._
      .....              .--~  .....  `.
    .":    "`-..  .    .' ..-'"    :". `
    ` `._ ` _.'`"(     `-"'`._ ' _.' '
         ~~~      `.          ~~~
                  .'
                 /
                (
                 ^---'

    [*] Author:dacAIniao@重明安全
    [*] Web:chmsec.com
    '''
    usage = '''
    Usage: 
        python3 Acunitix12-Scan-Agent.py [options]

    Options:
        -f  filename     Read the file and add the target to the awvs
        -o               Output all the vulnerability information to XLSX 
        -d               Delete all targets
    '''
