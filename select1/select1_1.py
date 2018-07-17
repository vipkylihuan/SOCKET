import select
import socket


sk1 = socket.socket()
sk1.bind(('127.0.0.1',8081))
sk1.listen()



message_dic = {}
outputs = []
inputs= [sk1,]

while True:
    r_list, w_list, e_list = select.select(inputs, [], inputs, 1)
    print('正在监听的对象%d' %len(inputs))
    print(r_list)
    for sk1_or_conn in r_list:
        if sk1_or_conn ==sk1:
            conn,address = sk1_or_conn.accept()
            inputs.append(conn)
            message_dic[conn] = []
        else:
            try:
                data_bytes = sk1_or_conn.recv(1024)
                data_str = str(data_bytes, encoding="utf-8")
                sk1_or_conn.sendall(bytes(data_str + "好", encoding="utf-8"))
            except Exception as ex:
                inputs.remove(sk1_or_conn)
            else:
                data_str = str(data_bytes, encoding="utf-8")
                message_dic[sk1_or_conn].append(data_str)
                outputs.append(sk1_or_conn)
            for conn in w_list:
                recv_str = message_dic[conn][0]
                del message_dic[conn][0]
                conn.sendall(bytes(recv_str + "好", encoding="utf-8"))
            for sk in e_list:
                inputs.remove(sk)