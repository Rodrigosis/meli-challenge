from typing import Dict, List
from src.infra.dataset import Dataset


class CommonFriends:

    def __init__(self, data: Dataset):
        self.data = data

    def get_common_friends(self, p1: str, p2: str) -> Dict:
        p1_friends = self.get_friend(p1)
        p2_friends = self.get_friend(p2)

        all_friends = list(set(p1_friends + p2_friends))

        common_friends = []
        for friend in all_friends:
            if friend in p1_friends and friend in p2_friends:
                common_friends.append(friend)

        return {"common_friends": common_friends}

    def get_friend(self, people: str) -> List[str]:
        friends = self.data.dataset[(self.data.dataset['personagem_1'].str.lower() == people.lower()) |
                                    (self.data.dataset['personagem_2'].str.lower() == people.lower())]

        friends_list = list(friends['personagem_1']) + list(friends['personagem_2'])
        friends_list = list(filter(lambda a: a != people, friends_list))

        return friends_list
