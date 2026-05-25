sudo apt-get update
sudo apt-get install -y wget unzip xvfb libxi6 libgconf-2-4

# Install Chrome
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb || sudo apt --fix-broken install -y

# Install matching ChromeDriver
CHROME_MAJOR=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
DRIVER_VERSION=$(curl -s "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_$CHROME_MAJOR")

wget -q "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$DRIVER_VERSION/linux64/chromedriver-linux64.zip"
unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
