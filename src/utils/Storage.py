data = {"Twitter": [], "Facebook": [], "Instagram": [], "kill": False}


class Storage:
    @staticmethod
    def save(platform, posts):
        data[platform] = posts
        return Storage

    @staticmethod
    def get(platform):
        return data[platform]

    @staticmethod
    def clear():
        data = {"Twitter": [], "Facebook": [], "Instagram": []}
