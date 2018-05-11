class Bouquet:
    def __init__(self):
        self.content = []
        self.price = 0
    def calculate_cost(self):
        self.price = 0
        for each in self.content:
            self.price += each[1]*each[2]       # price * quantity
    def add(self,item,quantity):
        result = []
        for i in range(2):
            result.append(item.name_price[i])   # item list unpacking to make a new list with quantity
        result.append(quantity)                 # result ==  ['name',price,quantity]
        self.content.append(result)
    def print_summary(self):
        self.calculate_cost()
        print(f'Your bouquet consits of:')
        for i in range(len(self.content)):
            if self.content[i][2] > 1:
                print(f'\t{self.content[i][2]} {self.content[i][0]}s') # plural form
            else:
                print(f'\t{self.content[i][2]} {self.content[i][0]}')  # singular form
        print(f'\tand costs {self.price}$.')
                   
class BouquetItem:
    def __init__(self,name,price):
        self.name_price = [name,price]

if __name__ == '__main__':
    rose = BouquetItem('rose',3.50)       
    tulip = BouquetItem('tulip',1.25)
    wrap = BouquetItem('wrapping',0.25)
    decor = BouquetItem('decorative',0.75)
    
    tulip_bouquet = Bouquet()
    tulip_bouquet.add(tulip,3)
    tulip_bouquet.add(decor,3)
    tulip_bouquet.add(wrap,1)
    tulip_bouquet.print_summary()
    
    rose_bouquet = Bouquet()
    rose_bouquet.add(rose,9)
    rose_bouquet.add(decor,3)
    rose_bouquet.add(wrap,1)
    rose_bouquet.print_summary()