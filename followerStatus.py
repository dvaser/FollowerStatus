import json
import os

class FollowerStatus:
    def __init__(self):
        self.followers = []
        self.following = []
        self.notFollower = []
        self.path = os.getcwd()
        self.followersJSON = f"{self.path}\\followers.json"
        self.followingJSON = f"{self.path}\\following.json"
        self.followrs = f"{self.path}\\followrs.json"
        self.followng = f"{self.path}\\followng.json"
        self.language = 'en'

    def process(self):
        try:
            self.followersFunc()
            self.followingFunc()
            self.notFollowerFunc()
            self.getNotFollower()
        except:
            if(self.language == 'en'):
                print("An unknown error occurred !!")
            elif(self.language == 'tr'):
                print("Bilinmeyen bir hata oluştu !!")            

        if(self.language == 'en'):
            input("\n\n\nPress to Exit..      ")
        elif(self.language == 'tr'):
            input("\n\n\nÇıkmak için Tuşlayınız..      ")

    def language(self):
        if(self.language == 'en'):
            self.language = 'tr'
        else:
            self.language = 'en'

    def followersFunc(self):
        with open(self.followersJSON, "r") as fr:
            data = json.load(fr)
            
            for user in data['relationships_followers']:
                for f in user['string_list_data']:
                    nick = f['value']
                    self.followers.append(nick)

        with open(self.followrs, "w") as fr:
            json.dump(self.followers, fr)

    def followingFunc(self):
        with open(self.followingJSON, "r") as fr:
            data = json.load(fr)
            
            for user in data['relationships_following']:
                for f in user['string_list_data']:
                    nick = f['value']
                    self.following.append(nick)

        with open(self.followng, "w") as fr:
            json.dump(self.following, fr)

    def notFollowerFunc(self):
        with open(self.followrs, "r") as fr:
            followers = json.load(fr)

        with open(self.followng, "r") as fg:
            followings = json.load(fg)

        for follower in followers:
            for i, following in enumerate(followings):
                if follower == following:
                    followings[i] = ""

        for user in followings:
            if user != "":
                self.notFollower.append(user)

    def getNotFollower(self):
        for user in self.notFollower:
            print(user)


user = FollowerStatus()
user.process()