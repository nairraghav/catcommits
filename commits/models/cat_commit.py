
class CatCommit:
    def __init__(self, commit_item):
        self.url = commit_item.get('html_url')
        self.message = commit_item.get('commit').get('message')
        try:
            self.author_image_url = commit_item.get('author').get('avatar_url')
        except:
            self.author_image_url= "https://github.githubassets.com/images/modules/open_graph/github-octocat.png"

    def serialize(self):
        return {
            'url': self.url,
            'author_image_url': self.author_image_url,
            'message': self.message,
        }
