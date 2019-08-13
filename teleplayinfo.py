# 一部电影信息


class TeleplayinfoModel:
    def __init__(self):
        self.__name = None
        self.__director_list = []
        self.__author_list = []
        self.__actor_list = []
        self.__score = 0
        self.__description = []

    #设置电视剧的名字
    def set_name(self, n):
        self.__name = n


    #添加导演
    def add_director(self, director):
        self.__director_list.append(director)

    #添加编剧
    def add_author(self, author):
        self.__author_list.append(author)

    #添加主演
    def add_actor(self, actor):
        self.__actor_list.append(actor)

    #设置评分
    def set_score(self, s):
        self.__score = s

    # 添加简介
    def add_description(self, description):
        self.__description.append(description)

    #打印
    def __repr__(self):
        #name = self.__name
        director_list = "/".join(self.__director_list)
        author_list = "/".join(self.__author_list)
        actor_list = "/".join(self.__actor_list)

        s = "片名：{}\n导演：{}\n编剧：{}\n主演：{}\n评分：{}\n简介：{}\n".format(self.__name,
                                                         director_list, author_list, actor_list, self.__score,
                                                                self.__description)

        return s
