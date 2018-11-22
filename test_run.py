import customer

ken = customer.Customer("Ken", "Tanaka", 15)
tom = customer.Customer("Tom", "Ford", 57)
ieyasu = customer.Customer("Ieyasu", "Tokugawa", 57)

print(ken.info_csv())
print(tom.info_csv())
print(ken.info_tab())
print(tom.info_tab())
print(ken.info_pipe())
print(tom.info_pipe())
