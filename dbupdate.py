

def NewPrice(idProduto, oldPrice, price):
    prod = Product.query.filter_by(id=idProduto).first()
    if prod:
        prod.price = price
        db.session().commit()


