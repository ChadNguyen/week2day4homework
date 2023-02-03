
class SodaStore:

    def __init__(self, brand, sold, redeemed, deposit, total):
        self.brand = brand
        self.sold = sold
        self.redeemed = redeemed
        self.deposit = 0.05
        self.total = total = cart = {}
        
    

    def add_item(self, brand, quantity, deposit):
        total += quantity * 0.05
        if brand in cart:
            cart[brand]['quantity'] += 0.05 * (quantity)
        else:
            cart[brand] = {
                'quantity': quantity,
                'deposit': cost
            }
        


    def redeem_item(self, brand, quantity, deposit):
        self.total -= quantity * 0.05
        if brand in cart:
            cart[brand]['quantity'] -= quantity
        else:
            cart[brand] = {
                'quantity': quantity,
                'deposit': cost,
            }
        Showlist(cart)

    def Showlist(cart):
        print('\n','='*10)
        print(cart)

    '''
    cart= {
        brand : {
            quantity: 2
            price: 4
        }
    }
    '''


    def driver():
        cart = {}
        shopping = True
        while shopping:
            user_choice = input('What are you here for today? (buy/redeem/show/quit) ').lower()
            if user_choice == 'buy':
                item = input('Which brand would you like to buy?: CocaCola or Pepsi').lower()
                if user_choice == 'CocaCola':
                    while True:
                        try:
                            quantity = int(input('How many do you want to buy?: '))
                            break
                        except:
                            print('Please Try again with a quantity in digits')
                    while True:
                            user_choice = input('Is there a deposit on these? (yes/no) ').lower()
                            if user_choice == 'yes':
                                print("Yes, 0.05 per container.")
                                break
                            elif user_choice == 'no':
                                break
                                add_item(ShopTotal, brand, quantity, deposit)
                elif user_choice == 'Pepsi':
                    while True:
                        try:
                            quantity = int(input('How many do you want to buy?: '))
                            break
                        except:
                            print('Please Try again with a quantity in digits')
                    while True:
                            print('There is a bottle deposit fee of $0.05 per container. ')
                            user_choice = input('Would you still like to purchase?:  (yes/no) ').lower()
                        if user_choice == 'yes':
                            add_item(ShopTotal, brand, quantity, deposit)
                    elif user_choice == 'no':
                            add_item(ShopTotal, brand, quantity, deposit)
                            return
                elif user_choice == 'redeem':
                    redeem_item = input('which brand will you redeem?: (CocaCola/ Pepsi) ')
                    while True:
                        try:
                            quantity = int(input('How many containers do you want to redeem?: '))
                            break
                        except:
                            print("Please enter quantity in digits")
                            redeem_item(ShopTotal, brand, quantity, deposit)
                elif user_choice == 'show':
                    Showlist(cart)
                elif user_choice == 'quit':
                    shopping = False
                else:
                    print('Please Enter Valid Choice')
        Showlist(ShopTotal)
driver()
    
                    

                
                   

                    
                    

                

