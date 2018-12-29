from string import Template
class myTemplate(Template):
    delimiter = "#"
    #idpattern = "[0-9]+"

def Main():
    cart=[]
    cart.append(dict(item="coke",price=8,qty=2))
    cart.append(dict(item="cake", price=12, qty=1))
    cart.append(dict(item="fish", price=32, qty=4))

    t=Template("$qty x $item = $$$price") # defined the template then we can use it with data
    t=myTemplate("#qty X #item=#price")
    #t = myTemplate("#0 X #1=#2")
    total=0
    print("cart:")
    for data in cart:
        print(t.substitute(data))
        total+=data["price"]
    print(f"total:{total}")


if __name__ == '__main__':
    Main()

"""
below are template error which can occurs:
1.KeyError:No Place holder match,it will give key error in which the template wasn't given a value 
for a placeholder
2.value error:
BadPlaceHolder will give value error.The place holder started with and invalid character(Usually number)

template can handle this error and give us back string still if we use safe_substitute method
but we also get placeholder in returned if there is error with it
e.g. Template("$name had $money") o/p "Jim had $money"

It is also possible to use custom delimited for placeholder variable by overriding default in Template Class
Lets change delimiter to Hash symbol


Template save time and reduce code
allow user to crete table
good with CGI programming also provide safe substitute
we can escape delimiters if needed using delimiter that is #
"""

'''
Why use one?
1.Save time and reduce code
2.Easy to implement custom template e.g. fileformat:myphoto_$n$ext=MyPhoto_0.jpg,MyPhoto_1.jpg
Extremely useful with web pages
3.If you need to use the character that is delimiter you can escape it using two repeating delimiters
4.Also when creating subclass we can ovveride the regular expression for template the variable id
pattern is set to "[_a-z][_a-z0-9]* by default"
5.To  attach a string to the end of a place holder then we need to specify the place holder in {}
"the ${plcae}yard is ..."
'''
