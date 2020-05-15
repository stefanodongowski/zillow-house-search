# Stefano Dongowski
# 11.22.2019
# Test

class House(object):
    def __init__(self, index, sq_ft, beds, baths, zip, year_built, list_price ):
        self.index = int(index)
        self.sq_ft = int(sq_ft)
        self.beds = int(beds)
        self.baths = float(baths)
        self.zip = int(zip)
        self.year_built = int(year_built)
        self.list_price = int(list_price)

    def __str__(self):
        output_str = f'{self.index:3}'+f'{self.sq_ft:5}'+f'{self.beds:2}'+f'{self.baths:4}'+f'{self.zip:6}'+f'{self.year_built:5}'+" $"+f'{self.list_price:10,.2f}'
        return output_str

    def get_index(self):
        return self.index

    def get_sq_ft(self):
        return self.sq_ft

    def get_beds(self):
        return self.beds

    def get_baths(self):
        return self.baths

    def get_zip(self):
        return self.zip

    def get_year_built(self):
        return self.year_built

    def get_list_price(self):
        return self.list_price

