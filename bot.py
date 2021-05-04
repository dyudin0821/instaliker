import os
import schedule
import time
from instapy import InstaPy
from instapy import smart_run

insta_username = os.environ.get('IG_USERNAME', 'username')
insta_password = os.environ.get('IG_PASSWORD', 'password')
friendlist = os.environ['IG_FRIENDLIST'].split(',')


# """
# Like last new posts from friendlists
# """
def like():
    friends = InstaPy(username=insta_username, password=insta_password, headless_browser=True,)
    with smart_run(friends, threaded=True):
        print('💞 Showing friends some love 💖')
        friends.set_relationship_bounds(enabled=False)
        friends.set_skip_users(skip_private=False)
        friends.set_do_like(True,percentage=100)
        friends.interact_by_users(friendlist,amount=1,randomize=False)

        
if __name__ == '__main__':
    schedule.every(1).minutes.do(like)
    while True:
        schedule.run_pending()
        time.sleep(1)
