class arrays():
    zmienna=", "
    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_line(array):
        pom=0
        for v in array:
            pom+=1
            print(v, end="")
            if pom!=len(array):
                print(arrays.zmienna,end="")
    @staticmethod
    def z12a(amount, value):
        tab=[]
        for v in range(0, amount):
            tab.append(value)
        return tab
    @staticmethod
    def z12b(amount, vmin, vmax):
        tab=[]
        import random
        for v in range (0, amount):
            pom=random.randint(vmin, vmax)
            tab.append(pom)
        return tab
    @staticmethod
    def z12c(tab,vmin,vmax):
        amount=0
        for v in tab:
            if v >= vmin and v <= vmax:
                amount+=1
        print(tab)
        return amount
    @staticmethod
    def zmienZmienna(newzmienna):
        arrays.zmienna = newzmienna
my_array = [4,1,8,7,2]
#arrays.print_in_col(my_array)
'''
twoarrays.py
arrays.print_in_line(my_array)
print()
print(arrays.z12a(3,6))
print(arrays.z12b(5,1,10))
print(arrays.z12c(arrays.z12b(10,0,10),0,6))
arrays.zmienZmienna("_")
arrays.print_in_line(my_array)
'''