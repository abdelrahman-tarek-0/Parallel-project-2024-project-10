data = {"Twitter": [], "Facebook": [], "Instagram": [], "kill": False}


class InMemorySharedStorage:
    @staticmethod
    def save(platform, posts):
        data[platform] = posts
        return InMemorySharedStorage

    @staticmethod
    def get(platform):
        return data[platform]
