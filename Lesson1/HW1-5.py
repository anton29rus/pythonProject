comp_name = input('Enter your company name: ')
comp_revenue = int(input('Enter your revenue: '))
comp_costs = int(input('Enter your costs: '))
fin_result = comp_revenue - comp_costs
if fin_result > 0:
    profit = fin_result/comp_costs*100
    print('Company is in profit = ', profit, '%')
    comp_stuff = int(input('Enter the number of employees: '))
    profit_stuff = fin_result/comp_stuff
    print('Company profit per one person: ', profit_stuff)
else:
    print('Company is at a loss')
