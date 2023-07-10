from socket import *

def start_honetpot():
    ip_add = '192.168.161.105'
    port = 80
    print("HONEYPOT START...")
    try:
        honeypot = socket(AF_INET,SOCK_STREAM)
        honeypot.bind((ip_add,port))
        honeypot.listen(5)
        print(f'Honeypot started on {ip_add}:{port}...')
        while 1:
            client_con,client_addr = honeypot.accept()
            print(f'Connection received from: {client_addr[0]}:{client_addr[1]}')
            client_con.send(b"<marquee>This is an example of html marquee </marquee>")
            data = client_con.recv(2048)
            print(data.decode('utf-8'))
    except error as identifier:
            print("[+] Unspecified error [{}]".format(identifier))
    except KeyboardInterrupt as ky:
            print("[-] process stopped !")
            get_socket_con.close()
    finally:
        honeypot.close()
    

if __name__ == "__main__":
    start_honetpot()
