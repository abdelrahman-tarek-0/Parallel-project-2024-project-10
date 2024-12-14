data = {} # this will be shared with all the threads

class InMemorySharedStorage:
    @staticmethod
    def save(platform, posts):
        data[platform] = posts
        return InMemorySharedStorage

    @staticmethod
    def get(platform):
        return data[platform]
