
class CatCommit:
    def __init__(self, commit_item):
        try:
            self.url = commit_item.get('html_url')
            self.author_image_url = commit_item.get('author').get('avatar_url')
            self.message = commit_item.get('commit').get('message')
            self.good_commit = True
        except:
            self.good_commit = False
