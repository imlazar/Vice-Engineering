# Laravel Web App template theme free download source code

A landing page website build with laravel the php artisan



[Screenshot 2025-03-17 at 00 37 49](https://github.com/user-attachments/assets/e64faa49-056b-4e17-b9b5-bed53d92bb38)

Monitoring server for: 

- Dr Cabinet
- Webservers South
- Remus Restaurant
- Kogalniceanu 1
- Kogalniceanu 2
- Social Media
- @Deco
- Mai era ceva
- Avocatwo
- LuxElectro
- LuxMed(ium)
- Request STEM (scoala de tech)


Always show details

# Create a new PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "How to Host a Telegram Bot on Raspberry Pi / Home Server", ln=True, align='C')
pdf.ln(10)

# Content
instructions = """

If you want to run your Telegram bot 24/7 on your Raspberry Pi or home server, follow these steps:

1️⃣ INSTALL REQUIRED SOFTWARE  
First, install Python and required dependencies for your bot:

sudo apt update && sudo apt upgrade -y
 sudo apt install python3 python3-pip -y
 pip3 install python-telegram-bot telebot requests

Always show details


2️⃣ RUN YOUR BOT WITH A PROCESS MANAGER  
You need to keep your bot running even after you close the terminal. Use one of these methods:

🔹 OPTION 1: USING TMUX  
sudo apt install tmux -y
tmux new -s mybot
python3 bot.py

Always show details

Detach: `Ctrl + B`, then press `D`  
Reattach: `tmux attach -t mybot`

🔹 OPTION 2: USING SCREEN  
sudo apt install screen -y
screen -S mybot
python3 bot.py

Always show details

Detach: `Ctrl + A`, then `D`  
Reattach: `screen -r mybot`

🔹 OPTION 3: USING SYSTEMD  
sudo nano /etc/systemd/system/telegram-bot.service

Always show details


Add the following content:

[Unit]
 Description=Telegram Bot Service
 After=network.target

[Service]
 ExecStart=/usr/bin/python3 /path/to/bot.py
 WorkingDirectory=/path/to/
 Restart=always
 User=pi

[Install]
 WantedBy=multi-user.target

Always show details


Save and exit (`CTRL + X`, then `Y`, then `Enter`).  
Reload systemd and enable the service:

sudo systemctl daemon-reload
 sudo systemctl enable telegram-bot
 sudo systemctl start telegram-bot

Always show details


Check status:
sudo systemctl status telegram-bot

Always show details


3️⃣ SET UP DYNAMIC DNS (IF NO STATIC IP)  
If your ISP does not give you a static IP, you need Dynamic DNS (DDNS) to access your home server remotely.

🔹 Step 1: Get a Free Dynamic DNS (DDNS)  
Sign up for a free DDNS service like No-IP (https://www.noip.com/) or DuckDNS (https://www.duckdns.org/).  
Set up a hostname (e.g., `mybot.ddns.net`).

🔹 Step 2: Install DDNS Client  
For No-IP:

sudo apt install noip2 -y
sudo noip2 -C

Always show details


For DuckDNS:

mkdir duckdns && cd duckdns
 echo "your-token" > token
 echo "your-subdomain" > subdomain
 wget -O duck.sh https://www.duckdns.org/install.sh
 chmod +x duck.sh
 ./duck.sh

Always show details


4️⃣ SET UP PORT FORWARDING (IF USING WEBHOOK MODE)  
If your bot needs to receive updates via webhooks instead of polling, set up port forwarding:

1. Log into your router settings (`192.168.1.1` or similar).  
2. Find "Port Forwarding" settings.  
3. Forward port `443` or `8443` to your Raspberry Pi IP (`192.168.1.xxx`).  

Now, your bot can receive updates directly from Telegram servers.

🎉 Your Telegram bot is now running 24/7 on your Raspberry Pi or home server!
"""

# Add content to PDF
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 8, instructions)

# Save PDF
pdf_filename = "/mnt/data/Telegram_Bot_Hosting_Guide.pdf"
pdf.output(pdf_filename)

# Return the file path
pdf_filename
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[1], line 2
      1 # Create a new PDF instance
----> 2 pdf = FPDF()
      3 pdf.set_auto_page_break(auto=True, margin=15)
      4 pdf.add_page()

NameError: name 'FPDF' is not defined
It looks like the required library is missing. Let me fix that and generate the PDF again. ​​


Analysis paused
Always show details

# Re-import the required library and generate the PDF again
from fpdf import FPDF

# Create a new PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "How to Host a Telegram Bot on Raspberry Pi / Home Server", ln=True, align='C')
pdf.ln(10)

# Content
instructions = """

If you want to run your Telegram bot 24/7 on your Raspberry Pi or home server, follow these steps:

1️⃣ INSTALL REQUIRED SOFTWARE  
First, install Python and required dependencies for your bot:

sudo apt update && sudo apt upgrade -y
 sudo apt install python3 python3-pip -y
 pip3 install python-telegram-bot telebot requests

Always show details


2️⃣ RUN YOUR BOT WITH A PROCESS MANAGER  
You need to keep your bot running even after you close the terminal. Use one of these methods:

🔹 OPTION 1: USING TMUX  
sudo apt install tmux -y
tmux new -s mybot
python3 bot.py

Always show details

Detach: `Ctrl + B`, then press `D`  
Reattach: `tmux attach -t mybot`

🔹 OPTION 2: USING SCREEN  
sudo apt install screen -y
screen -S mybot
python3 bot.py

Always show details

Detach: `Ctrl + A`, then `D`  
Reattach: `screen -r mybot`

🔹 OPTION 3: USING SYSTEMD  
sudo nano /etc/systemd/system/telegram-bot.service

Always show details


Add the following content:

[Unit]
 Description=Telegram Bot Service
 After=network.target

[Service]
 ExecStart=/usr/bin/python3 /path/to/bot.py
 WorkingDirectory=/path/to/
 Restart=always
 User=pi

[Install]
 WantedBy=multi-user.target

Always show details


Save and exit (`CTRL + X`, then `Y`, then `Enter`).  
Reload systemd and enable the service:

sudo systemctl daemon-reload
 sudo systemctl enable telegram-bot
 sudo systemctl start telegram-bot

Always show details


Check status:
sudo systemctl status telegram-bot

Always show details


3️⃣ SET UP DYNAMIC DNS (IF NO STATIC IP)  
If your ISP does not give you a static IP, you need Dynamic DNS (DDNS) to access your home server remotely.

🔹 Step 1: Get a Free Dynamic DNS (DDNS)  
Sign up for a free DDNS service like No-IP (https://www.noip.com/) or DuckDNS (https://www.duckdns.org/).  
Set up a hostname (e.g., `mybot.ddns.net`).

🔹 Step 2: Install DDNS Client  
For No





You said:
I want to download this as pdf
ChatGPT said:

Analysis errored
Always show details

# Recreate the PDF with the same content

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "How to Host a Telegram Bot on Raspberry Pi / Home Server", ln=True, align='C')
pdf.ln(10)

# Content
instructions = """

If you want to run your Telegram bot 24/7 on your Raspberry Pi or home server, follow these steps:

1️⃣ INSTALL REQUIRED SOFTWARE  
First, install Python and required dependencies for your bot:

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
pip3 install python-telegram-bot telebot requests

2️⃣ RUN YOUR BOT WITH A PROCESS MANAGER  
You need to keep your bot running even after you close the terminal. Use one of these methods:

🔹 OPTION 1: USING TMUX  
sudo apt install tmux -y  
tmux new -s mybot  
python3 bot.py  
Detach: Ctrl + B, then press D  
Reattach: tmux attach -t mybot

🔹 OPTION 2: USING SCREEN  
sudo apt install screen -y  
screen -S mybot  
python3 bot.py  
Detach: Ctrl + A, then D  
Reattach: screen -r mybot

🔹 OPTION 3: USING SYSTEMD  
sudo nano /etc/systemd/system/telegram-bot.service

Add the following content:

[Unit]
Description=Telegram Bot Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/bot.py
WorkingDirectory=/path/to/
Restart=always
User=pi

[Install]
WantedBy=multi-user.target

Save and exit (CTRL + X, then Y, then Enter).  
Reload systemd and enable the service:

sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

Check status:
sudo systemctl status telegram-bot

3️⃣ SET UP DYNAMIC DNS (IF NO STATIC IP)  
If your ISP does not give you a static IP, you need Dynamic DNS (DDNS) to access your home server remotely.

🔹 Step 1: Get a Free Dynamic DNS (DDNS)  
Sign up for a free DDNS service like No-IP (https://www.noip.com/) or DuckDNS (https://www.duckdns.org/).  
Set up a hostname (e.g., mybot.ddns.net).

🔹 Step 2: Install DDNS Client  
For No-IP:

sudo apt install noip2 -y  
sudo noip2 -C

For DuckDNS:

mkdir duckdns && cd duckdns
echo "your-token" > token
echo "your-subdomain" > subdomain
wget -O duck.sh https://www.duckdns.org/install.sh
chmod +x duck.sh
./duck.sh

4️⃣ SET UP PORT FORWARDING (IF USING WEBHOOK MODE)  
If your bot needs to receive updates via webhooks instead of polling, set up port forwarding:

1. Log into your router settings (192.168.1.1 or similar).  
2. Find "Port Forwarding" settings.  
3. Forward port 443 or 8443 to your Raspberry Pi IP (192.168.1.xxx).  

Now, your bot can receive updates directly from Telegram servers.

🎉 Your Telegram bot is now running 24/7 on your Raspberry Pi or home server!
"""

# Add content to PDF
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 8, instructions)

# Save PDF
pdf_filename = "/mnt/data/Telegram_Bot_Hosting_Guide.pdf"
pdf.output(pdf_filename)

# Return the file path
pdf_filename
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[2], line 3
      1 # Recreate the PDF with the same content
----> 3 pdf = FPDF()
      4 pdf.set_auto_page_break(auto=True, margin=15)
      5 pdf.add_page()

NameError: name 'FPDF' is not defined
It looks like the required library is missing. Let me fix that and generate the PDF again. ​​


Analysis errored
Always show details

# Import the required library
from fpdf import FPDF

# Create a new PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "How to Host a Telegram Bot on Raspberry Pi / Home Server", ln=True, align='C')
pdf.ln(10)

# Content
instructions = """

If you want to run your Telegram bot 24/7 on your Raspberry Pi or home server, follow these steps:

1️⃣ INSTALL REQUIRED SOFTWARE  
First, install Python and required dependencies for your bot:

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
pip3 install python-telegram-bot telebot requests

2️⃣ RUN YOUR BOT WITH A PROCESS MANAGER  
You need to keep your bot running even after you close the terminal. Use one of these methods:

🔹 OPTION 1: USING TMUX  
sudo apt install tmux -y  
tmux new -s mybot  
python3 bot.py  
Detach: Ctrl + B, then press D  
Reattach: tmux attach -t mybot

🔹 OPTION 2: USING SCREEN  
sudo apt install screen -y  
screen -S mybot  
python3 bot.py  
Detach: Ctrl + A, then D  
Reattach: screen -r mybot

🔹 OPTION 3: USING SYSTEMD  
sudo nano /etc/systemd/system/telegram-bot.service

Add the following content:

[Unit]
Description=Telegram Bot Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/bot.py
WorkingDirectory=/path/to/
Restart=always
User=pi

[Install]
WantedBy=multi-user.target

Save and exit (CTRL + X, then Y, then Enter).  
Reload systemd and enable the service:

sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

Check status:
sudo systemctl status telegram-bot

3️⃣ SET UP DYNAMIC DNS (IF NO STATIC IP)  
If your ISP does not give you a static IP, you need Dynamic DNS (DDNS) to access your home server remotely.

🔹 Step 1: Get a Free Dynamic DNS (DDNS)  
Sign up for a free DDNS service like No-IP (https://www.noip.com/) or DuckDNS (https://www.duckdns.org/).  
Set up a hostname (e.g., mybot.ddns.net).

🔹 Step 2: Install DDNS Client  
For No-IP:

sudo apt install noip2 -y  
sudo noip2 -C

For DuckDNS:

mkdir duckdns && cd duckdns
echo "your-token" > token
echo "your-subdomain" > subdomain
wget -O duck.sh https://www.duckdns.org/install.sh
chmod +x duck.sh
./duck.sh

4️⃣ SET UP PORT FORWARDING (IF USING WEBHOOK MODE)  
If your bot needs to receive updates via webhooks instead of polling, set up port forwarding:

1. Log into your router settings (192.168.1.1 or similar).  
2. Find "Port Forwarding" settings.  
3. Forward port 443 or 8443 to your Raspberry Pi IP (192.168.1.xxx).  

Now, your bot can receive updates directly from Telegram servers.

🎉 Your Telegram bot is now running 24/7 on your Raspberry Pi or home server!
"""

# Add content to PDF
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 8, instructions)

# Save PDF
pdf_filename = "/mnt/data/Telegram_Bot_Hosting_Guide.pdf"
pdf.output(pdf_filename)

# Return the file path
pdf_filename
---------------------------------------------------------------------------
UnicodeEncodeError                        Traceback (most recent call last)
Cell In[3], line 112
    110 # Save PDF
    111 pdf_filename = "/mnt/data/Telegram_Bot_Hosting_Guide.pdf"
--> 112 pdf.output(pdf_filename)
    114 # Return the file path
    115 pdf_filename

File ~/.local/lib/python3.11/site-packages/fpdf/fpdf.py:1065, in FPDF.output(self, name, dest)
   1063 #Finish document if necessary
   1064 if(self.state<3):
-> 1065     self.close()
   1066 dest=dest.upper()
   1067 if(dest==''):

File ~/.local/lib/python3.11/site-packages/fpdf/fpdf.py:246, in FPDF.close(self)
    244 self._endpage()
    245 #close document
--> 246 self._enddoc()

File ~/.local/lib/python3.11/site-packages/fpdf/fpdf.py:1636, in FPDF._enddoc(self)
   1634 def _enddoc(self):
   1635     self._putheader()
-> 1636     self._putpages()
   1637     self._putresources()
   1638     #Info

File ~/.local/lib/python3.11/site-packages/fpdf/fpdf.py:1170, in FPDF._putpages(self)
   1167 #Page content
   1168 if self.compress:
   1169     # manage binary data as latin1 until PEP461 or similar is implemented
-> 1170     p = self.pages[n].encode("latin1") if PY3K else self.pages[n] 
   1171     p = zlib.compress(p)
   1172 else:

UnicodeEncodeError: 'latin-1' codec can't encode characters in position 299-300: ordinal not in range(256)
It looks like there’s an encoding issue with special characters like emojis. I’ll fix it and regenerate the PDF. ​​


Analysis errored
Always show details

# Recreate the PDF without special characters to avoid encoding issues

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", style='', size=12)

# Title
pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, "How to Host a Telegram Bot on Raspberry Pi / Home Server", ln=True, align='C')
pdf.ln(10)

# Content without special characters
instructions = """

If you want to run your Telegram bot 24/7 on your Raspberry Pi or home server, follow these steps:

1. INSTALL REQUIRED SOFTWARE  
First, install Python and required dependencies for your bot:

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
pip3 install python-telegram-bot telebot requests

2. RUN YOUR BOT WITH A PROCESS MANAGER  
You need to keep your bot running even after you close the terminal. Use one of these methods:

Option 1: Using tmux  
sudo apt install tmux -y  
tmux new -s mybot  
python3 bot.py  
Detach: Ctrl + B, then press D  
Reattach: tmux attach -t mybot

Option 2: Using screen  
sudo apt install screen -y  
screen -S mybot  
python3 bot.py  
Detach: Ctrl + A, then D  
Reattach: screen -r mybot

Option 3: Using systemd  
sudo nano /etc/systemd/system/telegram-bot.service

Add the following content:

[Unit]
Description=Telegram Bot Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/bot.py
WorkingDirectory=/path/to/
Restart=always
User=pi

[Install]
WantedBy=multi-user.target

Save and exit (CTRL + X, then Y, then Enter).  
Reload systemd and enable the service:

sudo systemctl daemon-reload
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot

Check status:
sudo systemctl status telegram-bot

3. SET UP DYNAMIC DNS (IF NO STATIC IP)  
If your ISP does not give you a static IP, you need Dynamic DNS (DDNS) to access your home server remotely.

Step 1: Get a Free Dynamic DNS (DDNS)  
Sign up for a free DDNS service like No-IP (https://www.noip.com/) or DuckDNS (https://www.duckdns.org/).  
Set up a hostname (e.g., mybot.ddns.net).

Step 2: Install DDNS Client  
For No-IP:

sudo apt install noip2 -y  
sudo noip2 -C

For DuckDNS:

mkdir duckdns && cd duckdns
echo "your-token" > token
echo "your-subdomain" > subdomain
wget -O duck.sh https://www.duckdns.org/install.sh
chmod +x duck.sh
./duck.sh

4. SET UP PORT FORWARDING (IF USING WEBHOOK MODE)  
If your bot needs to receive updates via webhooks instead of polling, set up port forwarding:

1. Log into your router settings (192.168.1.1 or similar).  
2. Find "Port Forwarding" settings.  
3. Forward port 443 or 8443 to your Raspberry Pi IP (192.168.1.xxx).  

Now, your bot can receive updates directly from Telegram servers.

Your Telegram bot is now running 24/7 on your Raspberry Pi or home server!
"""

# Add content to PDF
pdf.set_font("Arial", size=11)
pdf.multi_cell(0, 8, instructions)

# Save PDF
pdf_filename = "/mnt/data/Telegram_Bot_Hosting_Guide.pdf"
pdf.output(pdf_filename)

# Return the file path
pdf_filename
It seems like I can’t generate the PDF file right now. Please try again later or use an online tool like an online Markdown-to-PDF converter if you need the instructions urgently. Let me know how else I can help! ​​
