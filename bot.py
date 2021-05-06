import os
import time
import schedule
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

insta_username = os.environ.get('IG_USERNAME', 'username')
insta_password = os.environ.get('IG_PASSWORD', 'password')
friendlist = os.environ['IG_FRIENDLIST'].split(',')

set_workspace(path=os.path.dirname(os.path.realpath(__file__)))

def like():
    bot = InstaPy(username=insta_username, password=insta_password, headless_browser=True)
    with smart_run(bot, threaded=True):
        print('💞 Showing friends some love 💖')
        bot.set_relationship_bounds(enabled=False)
        bot.set_skip_users(skip_private=False)
        bot.set_do_like(True,percentage=100)
        bot.interact_by_users(friendlist,amount=1,randomize=False)


print('-------------------------------------')
print(f'User: {insta_username}')
print(f'UserList: {friendlist}')
schedule.every(1).minutes.do(like)
while True:
    schedule.run_pending()
    time.sleep(60)
