echo "Cloning Repository"
git clone https://github.com/Jegaa1/md-renamebot1 /md-renamebot1
cd /md-renamebot1
echo "installing requirements"
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
