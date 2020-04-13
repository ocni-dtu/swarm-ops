__author__ = "Christian Kongsgaard"
__license__ = 'MIT'




import celery


@celery.task()
def main():
    pass
    # pull git repo
    # check for updates
    # if there is any updates:
        # apply them to docker stack