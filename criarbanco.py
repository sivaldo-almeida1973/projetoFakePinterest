from fakePinterest import database, app
#import do __init__

from fakePinterest.models import Usuario, Foto

#criar banco
with app.app_context():
     database.create_all()
