import tweepy
import logging
import time

#API information stored here
from createAPI import createAPI

logger = logging.getLogger()

def followFollowers(api):
    logger.info("Following followers....")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info("Following {follower.name}")
            follower.follow()



def main():
    #Initialize API
    api = createAPI()

    while True:
        followFollowers(api)
        logger.info("Sleeping for one hour")
        time.sleep(3600)

if __name__ == "__main__":
    main()
