import string

nl = '\n'

fr = open('/home/ansible/test/py/var_inventory.ini', 'r')
fw = open('/home/ansible/test/py/prometheus.yml', 'a')
fra = open('/home/ansible/test/py/prometheus.yml', 'r')

cnt=0

while True:
    fradata = fra.readline()
    if fradata == '':
        break
    cnt += 1
    
fra.close()
fra = open('/home/ansible/test/py/prometheus.yml', 'r')

while True:
    data = fr.readline()
    fradata = fra.readline()
    print("data="+data)
    print("fradata="+fradata)
    i = 0
    a = 0
    if data == '':
        break
    # print(data)
    data2 = 1
    if "." in data:
        hosts = (data.split('.'))
        print(hosts[0])
        ipadr = (data.split('ansible_host='))
        print(ipadr[1])
        for i in range(1, cnt):
            fradata = fra.readline()
            if "  - job_name: " + hosts[0] in fradata:
                a = 1
        if a == 0:
            fw.write("  - job_name: " + hosts[0] + nl)
            fw.write("    static_configs:" + nl)
            fw.write("      - targets: ['" + ipadr[1].rstrip() + ":9100']" + nl+nl)

# fw.write("### Set Finished ###")

#   - job_name: {{ inventory_hostname_short }}
#     static_configs:
#       - targets: ['localhost:9100']

fr.close()
fw.close()
fra.close()