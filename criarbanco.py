from fakePinterest import database, app
# Importa o objeto 'database' e a aplicação 'app' do módulo 'fakePinterest'
# Estes são provavelmente definidos no arquivo __init__.py do seu projeto

from fakePinterest.models import Usuario, Foto
# Importa os modelos 'Usuario' e 'Foto' do módulo 'models' dentro do pacote 'fakePinterest'

# Criar banco de dados
with app.app_context():
     database.create_all()
     # Cria todas as tabelas no banco de dados que ainda não existem
     # O contexto da aplicação é necessário para que o SQLAlchemy possa interagir com o banco de dados
