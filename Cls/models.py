from . import db

class Clothes_category(db.Model):
        __tablename__ = 'clothes'
        id=db.Column(db.Integer, primary_key=True)
        name=db.Column(db.String(64), unique=True)
        description=db.Column(db.String(500),nullable=False)#should not be null and may contains many words so set it to 500 
    
        def __repr__(self):
            str="id:{}, name:{}, description:{}\n"
            str=str.format(self.id,self.name,self.description)
            return str

class Product(db.Model):
        __tablename__='products'
        id=db.Column(db.Integer, primary_key=True)
        name=db.Column(db.String(64), nullable=False)
        clothes_category_id=db.Column(db.Integer, db.ForeignKey('clothes.id'))
        price=db.Column(db.Float, nullable=False)
        main_image=db.Column(db.String(64),nullable=False)
        img1=db.Column(db.String(64))
        img2=db.Column(db.String(64))
        description=db.Column(db.String(500),nullable=False)
        note1=db.Column(db.String(500))
        note2=db.Column(db.String(500))
        note3=db.Column(db.String(500))
        
        def __repr__(self):
            str="id:{}, name:{},clothes:{},price:{},image:{},img1:{},img2:{},description:{},note1:{},note2:{},note3:{} \n"
            str=str.format(self.id,self.name,self.clothes_category_id,self.price,self.main_image,self.img1,self.img2,self.description,self.note1,self.note2,self.note3)
            return str
orderdetails = db.Table('orderdetails',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'),nullable=False),
    db.Column('product_id', db.Integer,db.ForeignKey('products.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id','product_id') )    

class Order(db.Model):
        __tablename__='orders'
        id=db.Column(db.Integer, primary_key=True)
        status=db.Column(db.Boolean, default=False) #set the default false for the status
        total_price=db.Column(db.Float)
        firstname=db.Column(db.String(64))
        lastname=db.Column(db.String(64))
        title=db.Column(db.String(32))
        phone=db.Column(db.String(32))
        email=db.Column(db.String(128))
        comment=db.Column(db.String(500))
        products=db.relationship("Product", secondary=orderdetails ,backref="orders")
        def __repr__(self):
            str="id:{}, status:{}, firstname:{},lastname:{},title:{}, phone:{}, email:{},comment:{}, products:{}, total price:{}\n"
            str=str.format(self.id,self.status,self.firstname,self.lastname,self.title,self.phone,self.email,self.comment,self.products,self.total_price)
            return str

class Subscribe(db.Model):
        __tablename__='subs'
        id=db.Column(db.Integer, primary_key=True)
        email=db.Column(db.String(128))
        def __repr__(self):
            str="id:{}, email:{}\n"
            str = str.format(self.id, self.email)
            return str
