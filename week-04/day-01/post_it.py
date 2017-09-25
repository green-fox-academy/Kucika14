class PostIt(object):


    def __init__(self, background, text, text_color):
        self.background = background
        self.text = text
        self.text_color = text_color


orange = PostIt("orange", "Idea1", "blue")
pink = PostIt("pink", "Awesome", "black" )
yellow = PostIt("yellow", "Superb", "green")



print(orange.background, orange.text, orange.text_color)
print(pink.background, pink.text, pink.text_color)
print(yellow.background, yellow.text, yellow.text_color)






