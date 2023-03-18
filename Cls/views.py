from flask import Blueprint, render_template, url_for, request, session, flash,redirect
from wtforms import TextField #如果之後沒有要用到要刪掉
from .models import Clothes_category,Product,Order, Subscribe
from .forms import checkout_form
from . import db
bp=Blueprint('main',__name__)

@bp.route('/')#return render template
def home():
    category_name = Clothes_category.query.all()
    all_products= Product.query.all()
    return render_template('home.html',c = category_name, products=all_products)
#------------------------------------------------------------------#
@bp.route('/category/<int:categoryid>/')#just the address name
def items(categoryid):# self deined name
    category_name = Clothes_category.query.all()#for getting the category name
    products_cate=Product.query.filter(Product.clothes_category_id == categoryid)
    return render_template('items.html', c = category_name, p=products_cate)#c and p refer to the tags in items pages
                                        #category name displayed
                                        
    # items= [] #create array as a list (originally, without DB)  
    # for product in products:
    #       if int(product.clothes_category.id)==int(categoryid):
    #         items.append(product)
#------------------------------------------------------------------#
@bp.route('/detail/<int:detailid>/')
def details(detailid):
    category_name = Clothes_category.query.all()
    single_item=Product.query.filter(Product.id == detailid)
    return render_template('details.html', c = category_name, products=single_item)
#------------------------------------------------------------------#
@bp.route('/shoppingcart',methods=['POST','GET'])
def cart(): 
    category_name = Clothes_category.query.all()#for getting the category name
    # in case of going to cart in different way, we get the id first 
    #we can use form, values, but not args, cuz we are not getting it grom GET
    product_id = request.values.get('product_id')#product_id is the arrays of items in the cart
   
    #display the cart if there is somthing
    if 'order_id' in session.keys():#existing order and is stored in the session key called 'order_id'
        cart = Order.query.get(session ['order_id'])
    else:
        cart=None#there is nothing in the cart
    
    if cart is None: #then, create new cart
        cart=Order(status=False,firstname='',lastname='',title='',phone='',email='',comment='',total_price=0)
        # print(cart)
        try:
            db.session.add(cart)
            db.session.commit()
            session['order_id']= cart.id
        except:
            print('failed to create a new cart')
            cart = None # noting there again
        
    totalprice=0 #count total
    if cart is not None:
        for product in cart.products:
            totalprice += product.price

    if product_id is not None and cart is not None:
        product = Product.query.get(product_id)
        if product not in cart.products:
            try:
                cart.products.append(product)
                db.session.commit()
            except:
                return 'Failling to add the item to the cart'
            return redirect(url_for('main.cart'))
        else:
            flash('Oops! -  The item has already existed in your cart - ')
            return  redirect(url_for('main.cart'))
        
    return render_template('cart.html', c=category_name, cart=cart, subtotal=totalprice)
#------------------------------------------------------------------#
@bp.route('/deletesingleitem', methods = ['POST'])
def deletesingleitem():
    id = request.form['id']
    if 'order_id' in session:
        cart = Order.query.get_or_404 (session['order_id'])
        delete_item = Product.query.get(id)
        try:
            cart.products.remove(delete_item)
            db.session.commit()
            return redirect(url_for('main.cart'))
        except:
            return 'Something happened when deleting the item.'
    return redirect(url_for('main.cart'))
#------------------------------------------------------------------#
@bp.route('/deleteall')
def deleteall():
    if 'order_id' in session:
        del session['order_id']
        flash('Oh No ! The cart is sad and hungry :( ')
    return redirect(url_for('main.cart'))
#------------------------------------------------------------------#
@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    category_name = Clothes_category.query.all()
    form = checkout_form()
    
    if 'order_id' in session:
        order=Order.query.get_or_404(session['order_id'])
        if form.validate_on_submit():
            order.status = True 
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.title = form.title.data
            order.phone = form.phone.data
            order.email = form.email.data
            order.comment =form.comment.data   
            totalprice =0
            for product in order.products: # in Order class, the attribute called products 
                totalprice += product.price
            order.total_price = totalprice
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you very much, and we will be contacting you soon. Have a nice day.')   
                return redirect(url_for('main.checkout'))
            except:
                return'An issue has occured when finalizing the order!'     
        else :
            print('debug')#trying to debug                            
    return render_template('checkout.html', c=category_name, form=form)
#---------------------------------------------------------#
@bp.route('/search')
def search():
    category_name = Clothes_category.query.all()
    search=request.args.get('Search')#to get the value from the page with the "name" in search HTML code
    search='%{}%'.format(search) #'%{}%' for matching with what every it contains the keywords
    product=Product.query.filter(Product.name.like(search)).all()#for searching by product name
    if not product:
        flash('Uh no !!  No match found. Please try another search.')
    return render_template('items.html',c=category_name,  p=product)

@bp.route('/subscribe', methods =['POST'])
def subscribe():
    category_name = Clothes_category.query.all()
    all_products= Product.query.all()
    subs = request.form.get('Subs')
    subscribe=Subscribe(email=subs)
    # print(subscribe)# I was doing debuging
    db.session.add(subscribe)
    db.session.commit()
    flash('Thank you for your subscription : ) ')
    return render_template('home.html',c=category_name, products=all_products, subscribe=subs)
 