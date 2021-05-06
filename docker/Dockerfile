FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN sed -i "s#deb http://deb.debian.org/debian buster main#deb http://deb.debian.org/debian buster main contrib non-free#g" /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  # Firefox dependencies
  libgtk-3-0 libdbus-glib-1-2 libx11-xcb1 libxt6 firefox-esr \
  # Firefox downlader dependencies
  bzip2 \
  wget \
  gcc \
  g++ \
  && wget -q https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-arm7hf.tar.gz -O /tmp/geckodriver-v0.23.0-arm7hf.tar.gz \
  && tar -xvzf /tmp/geckodriver-v0.23.0-arm7hf.tar.gz -C /usr/local/bin/ \
  && chmod +x /usr/local/bin/geckodriver \
  && pip install --no-cache-dir -U -r /app/requirements.txt \
  && apt-get purge -y --auto-remove \
  gcc \
  g++ \
  bzip2 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  # Disabling geckodriver log file
  && sed -i "s#browser = webdriver.Firefox(#browser = webdriver.Firefox(service_log_path=os.devnull,#g" /usr/local/lib/python3.9/site-packages/instapy/browser.py \
  # Fix webdriverdownloader not handling asc files
  && sed -i "s#bitness in name]#bitness in name and name[-3:] != 'asc' ]#g" /usr/local/lib/python3.9/site-packages/webdriverdownloader/webdriverdownloader.py

COPY bot.py /app/bot.py

ENV PATH /usr/local/bin:$PATH

CMD ["python", "bot.py"]