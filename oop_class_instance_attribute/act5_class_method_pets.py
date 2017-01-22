class Pets:
    name = "pet animals"

    # @staticmethod
    # def about():
    #     print("This class is about {}!".format(Pets.name))
    
    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))


class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"


class Cats(Pets):
    name = "cats"


p = Pets()
p.about()

d = Dogs()
d.about()

c = Cats()
c.about()