import scrap_engine as se

class PlayMap(se.Map):
    def __init__(self, height=se.height-1, width=se.width, background="#", trainers=[], name="", pretty_name="", poke_args={}, extra_actions=None, dynfps=True):
        super().__init__(height=height, width=width, background=background, dynfps=dynfps)
        for i in ["trainers", "name", "pretty_name", "poke_args"]:
            exec("self."+i+"="+i)
        self.__extra_actions = extra_actions

    def extra_actions(self):
        if self.__extra_actions != None:
            self.__extra_actions()


class PokeType():
    def __init__(self, name, effective, ineffective):
        self.name = name
        self.effective = effective
        self.ineffective = ineffective


class InvItem:
    def __init__(self, name, pretty_name, desc, price, fn=None):
        self.name = name
        self.pretty_name = pretty_name
        self.desc = desc
        self.price = price
        self.fn = fn


class BoxIndex(se.Object):
    def __init__(self):
        super().__init__("*", state="float")
        self.index = 0


class Box(se.Box):
    def __init__(self, height, width, name="", info=""):
        super().__init__(height, width)
        self.frame = se.Frame(width=width, height=height, corner_chars=["┌", "┐", "└", "┘"], horizontal_chars=["─", "─"], vertical_chars=["│", "│"], state="float")
        self.inner = se.Square(char=" ", width=width-2, height=height-2, state="float")
        self.name_label = se.Text(name, state="float")
        self.info_label = se.Text(info, state="float")
        # adding
        self.add_ob(self.frame, 0, 0)
        self.add_ob(self.inner, 1, 1)
        self.add_ob(self.name_label, 2, 0)
        self.add_ob(self.info_label, 2, self.height-1)


class ChooseBox(Box):
    def __init__(self, height, width, name="", info="", index_x=2):
        super().__init__(height, width, name, info)
        self.index_x = index_x
        self.index = BoxIndex()
        # adding
        self.add_ob(self.index, self.index_x, 1)

    def input(self, ev, list):
        if list == []:
            return
        if {"'s'": self.index.index+1 < len(list), "'w'": self.index.index-1 >= 0}[ev]:
            self.index.index += {"'s'": 1, "'w'": -1}[ev]
        else:
            self.index.index = {"'s'": 0, "'w'": len(list)-1}[ev]
        self.set_index(list)

    def set_index(self, list):
        self.set_ob(self.index, self.index.rx, list[self.index.index].ry)


class Settings():
    def __init__(self, autosave=True):
        self.keywords = ["autosave"]
        for key in self.keywords:
            exec(f"self.{key} = {key}")

    def dict(self):
        return {i: eval("self."+i, {"self": self,}) for i in self.keywords}


if __name__ == "__main__":
    print("\033[31;1mDo not execute this!\033[0m")
