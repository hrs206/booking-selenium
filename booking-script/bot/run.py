from booking.booking import Booking


bot = Booking()
bot.land_first_page()
bot.dismiss_sign_in()
bot.change_currency(currency=input("Enter Curreny: "))
bot.select_place(input("Enter Place: "))
bot.choose_date(input("Enter Check in date(YYYY-MM-DD): "), input("Enter Check out date(YYYY-MM-DD): "))
adults= int(input("Enter No. of adults: "))
children = int(input("Enter No. of children: "))
age = []
for i in range(0,children):
    age.append(int(input(f"Enter age of kid no.{i+1}: ")))

bot.total_persons(adults=adults,children=children,age=age, rooms=int(input("Enter no. of Rooms: ")))
bot.search()
a = int(input("Enter no. of stars rating you want to select: "))
stars = []
for i in range(0,a):
    stars.append(int(input(f"Enter rating no.{i+1}: ")))
bot.apply_filtrations(star_values=stars)
bot.report()