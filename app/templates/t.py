date_of_birth = db.Column(db.DateTime)
    gender = db.Column(db.String(30), nullable=False)
    genotype = db.Column(db.String(5), nullable=False)
    ailment = db.Column(db.String(100), nullable=False) 