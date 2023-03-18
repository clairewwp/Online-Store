from flask import Blueprint
from . import db
from . models import Clothes_category,Product,Order

bp = Blueprint('admin', __name__, url_prefix='/admin/')

@bp.route('/dbseed')
def dbseed():
    tops=Clothes_category(name='Tops',description='T-shirt / Sweater / Crop-top')
    dresses=Clothes_category(name='Dresses', description='Mini / Midi / Maxi')
    skirts=Clothes_category(name='Skirts', description='High waisted / Bubble / A-Line')
    try:
        db.session.add(tops)
        db.session.add(skirts)
        db.session.add(dresses)
        db.session.commit()
    except:
        return 'An issue occured while adding category'

    product1=Product(name='Mockneck Sweater',clothes_category_id=tops.id,price=45.00,main_image='top1.jpeg',img1='top1-1.jpeg',img2='top1-2.jpeg', description=' A comfy sweater made of merino wool, with the mock neck, keeps you warm all the time.',note1='100% merino wool',note2='lightweight, slight stretch',note3='Handwash only')

    product2=Product(name='Mist-Blue Crewneck Sweater', clothes_category_id=tops.id,price=35.00,main_image='top2.jpeg',img1='top2-1.jpeg',img2='top2-2.jpeg ',description='Soft and cozy sweater in a comfy knit fabric with drop shoulder detail, and crewneck.',note1='100% merino wool ',note2=' lightweight, slight stretch ',note3=' Handwash only ')
    
    product3=Product(name=' Denim Mini Skirt ' , clothes_category_id=skirts.id, price=39.75, main_image='skirt8.jpg',img1='skirt8-1.jpg',img2='',description='Mini denim skirt with button-up detail.', note1='100% Cotton', note2='Turn garment inside out, wash before wear to avoid color transfer.', note3='Machine washable')
    
    product4=Product(name='Beige Skirt',clothes_category_id=skirts.id,price=35.29, main_image='skirt2.png',img1='',img2='',description='High-rise mini skirt with tiered detailing. ', note1='80% Viscose, 20% Linen', note2='Machine wash cold, with like colors', note3='Line dry')

    product5=Product(name='Mini Strap Dress', clothes_category_id=dresses.id, price=40.75,main_image='dress1.jpg',img1='dress1-1.jpg',img2='dress1-2.jpg',description=' Slim-fitting mini dress in a lightweight georgette fabric featuring adjustable tie straps and dots decorated.',note1='100% Polyester ',note2=' Machine wash cold, with like colors ',note3='Line dry')

    product6=Product(name='Mini Striped Dress', clothes_category_id= dresses.id, price=39.15,main_image='dress2.jpg',img1='',img2='',description='Slim-fitting mini dress in our soft crepe fabric.',note1='90% Polyester, 10% Elastane',note2='Machine was cold, with like colors',note3='Line dry')

    product7=Product(name='Bohemian Crewneck Sweater' ,clothes_category_id=tops.id, price=47.75, main_image='top3.jpeg',img1='',img2='',description=' Soft and cozy sweater in a comfy knit fabric with drop shoulder detail, and crewneck.', note1='100% merino wool ',note2=' lightweight, slight stretch ',note3=' Handwash only ')

    product8=Product(name=' Pale-Orange Skirt ' ,clothes_category_id=skirts.id, price=35.29, main_image='skirt3.jpg',img1='',img2='',description='High-rise mini skirt with tiered detailing.', note1='80% Viscose, 20% Linen', note2='Machine wash cold, with like colors', note3='Line dry')

    product9=Product(name='Shirt Dress ', clothes_category_id=dresses.id, price=47.75, main_image='dress3.jpg',img1='',img2='', description='Comfortable three-quarter sleeve shirt dress in a soft linen fabric with classic button-up front.',note1='75% Linen, 25% Viscose',note2='Machine wash cold, with like colors', note3='Line dry')

    product10=Product(name=' V-Neck Knit Vest ', clothes_category_id=tops.id, price=57.25,main_image='top4.jpg',img1='',img2='',description='Sleevelss sweater vest fits every style easily, featuring in V-neckline.', note1='100% merino wool ',note2=' lightweight, slight stretch ',note3=' Handwash only ')

    product11=Product(name='Mockneck Beige Sweater ' ,clothes_category_id=tops.id, price=48.00, main_image='top5.jpg',img1='',img2='',description=' Cozy sweater featuring in a soft yarn with puff sleeves.', note1='100% merino wool ',note2=' lightweight, slight stretch ',note3=' Handwash only ')
    
    product12=Product(name=' Turtleneck Sweater' ,clothes_category_id=tops.id, price=47.75, main_image='top6.jpg',img1='top6-1.jpg',img2='',description='Cozy sweater in a comfy knit fabric with drop shoulder detail, and turtleneck.', note1='100% merino wool ',note2=' lightweight, slight stretch ',note3=' Handwash only ')

    product13=Product(name=' Wheat Skirt' ,clothes_category_id=skirts.id, price=35.29, main_image='skirt4.jpg',img1='',img2='',description=' High-rise mini skirt with tiered detailing.', note1='80% Viscose, 20% Linen', note2='Machine wash cold, with like colors', note3='Line dry')

    product14=Product(name='Narcissus Skirt ', clothes_category_id=skirts.id, price=35.29, main_image='skirt5.jpg',img1='',img2='',description=' High-rise mini skirt with tiered detailing.', note1='80% Viscose, 20% Linen', note2='Machine wash cold, with like colors', note3='Line dry')

    product15=Product(name='Polka-Dot Cutout Dress' ,clothes_category_id=dresses.id, price=49.75,main_image='dress4.jpg',img1='',img2='',description='Flattering mini dress in a soft linen-blend fabric featuring in cutout detail.',note1='100% Cottom',note2='Machine wash cold, with like colors',note3='Tumble dry low')

    product16=Product(name='Tiered Midi Dress ' , clothes_category_id=dresses.id, price=45.35, main_image='dress5.jpg',img1=' dress5-1.jpg ',img2=' dress5-2.jpg ', description=' Easy-fitting midi dress in a soft linen-blend fabric featuring a tiered skirt. ', note1='60% Linen, 40% Viscose', note2='Machine wash cold, with like colors', note3='Line dry')

    product17=Product(name='Button-up Mini Dress', clothes_category_id=dresses.id, price=47.75, main_image='dress6.jpg',img1='',img2='',description=' Easy-fitting mini shirt-dress with comfortable short-sleeves. ', note1='55% Linen, 45% Viscose', note2='Machine wash cold, with like colors', note3='Line dry')

    product18=Product(name=' Mockneck Blue Sweater ', clothes_category_id=tops.id, price=48.00, main_image='top7.jpg',img1='',img2='', description=' Cozy sweater featuring in a soft yarn with puff sleeves.', note1='100% merino wool ',note2=' lightweight, slight stretch ',note3=' Handwash only ')

    product19=Product(name='Skirt ', clothes_category_id=skirts.id, price=47.75, main_image='skirt6.jpg',img1='',img2='',description='', note1='80% Viscose, 20% Linen', note2='Machine wash cold, with like colors', note3='Line dry')

    product20=Product(name='Mockneck Grey Sweater', clothes_category_id=tops.id,price=48.00, main_image='top8.jpg ',img1='',img2='', description=' Cozy sweater featuring in a soft yarn with puff sleeves.', note1='100% merino wool ', note2=' lightweight, slight stretch ', note3=' Handwash only ')

    product21=Product(name='Tiered Maxi Skirt  ', clothes_category_id=skirts.id, price=41.00, main_image='skirt7.jpg',img1='',img2='',description=' High-rise maxi skirt in a soft fabric, featuring tiered detail.', note1='100% Viscose', note2='Machine wash cold, with like colors', note3='Line dry')

    product22=Product(name='Polka-Dot Skirt', clothes_category_id=skirts.id, price=35.29, main_image='skirt1.jpg', img1='', img2='', description='High-rise mini skirt with tiered detailing and dots decorated. ', note1='80% Viscose, 20% Linen', note2='Machine wash cold, with like colors', note3='Line dry')
    
    product23=Product(name='Mini Strap Dress', clothes_category_id=dresses.id, price=40.75,main_image='dress7.jpg',img1='',img2='',description=' Slim-fitting mini dress in a lightweight georgette fabric featuring adjustable tie straps.',note1='100% Polyester ',note2=' Machine wash cold, with like colors ',note3='Line dry')

    product24=Product(name='Cutout Mini dress ', clothes_category_id=dresses.id, price=42.39, main_image='dress8.jpg',img1='',img2='',description='Flattering slip mini dress in a soft linen-blend fabric featuring cutout front and adjustable tie at waist.',note1='100% Cotton',note2='Machine wash cold, with like colors',note3='Tumble dry low')


    try:
        db.session.add(product1)
        db.session.add(product2)
        db.session.add(product3)
        db.session.add(product4)
        db.session.add(product5)
        db.session.add(product6)
        db.session.add(product7)
        db.session.add(product8)
        db.session.add(product9)
        db.session.add(product10)
        db.session.add(product11)
        db.session.add(product12)
        db.session.add(product13)
        db.session.add(product14)
        db.session.add(product15)
        db.session.add(product16)
        db.session.add(product17)
        db.session.add(product18)
        db.session.add(product19)
        db.session.add(product20)
        db.session.add(product21)
        db.session.add(product22)
        db.session.add(product23)
        db.session.add(product24)

        db.session.commit()
    except:
        return 'An issue occured when adding products into the databaseseed'

    return 'Data has been successful loaded'


