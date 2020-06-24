from app import db
from models import Pet

db.drop_all()
db.create_all()

# current pets to add to database

ava = Pet(name="Ava", species="dog", photo_url="https://images.unsplash.com/photo-1543333108-4f3e0f5a7d11?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1336&q=80",
          age="3",
          notes="Husky",
          available=True)
larry = Pet(name="Benny",
            species="cat",
            photo_url="https://images.unsplash.com/photo-1503324280674-50695c3ae35f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80",
            age="5",
            notes="Shetland Sheepdog",
            available=False)
peaches = Pet(name="Peaches",
              species="cat",
              photo_url="https://images.unsplash.com/photo-1506891536236-3e07892564b7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80",
              age="3",
              notes="Orange Tabby",
              available=True)
daisy = Pet(name="Daisy",
            species='dog',
            photo_url="https://images.unsplash.com/photo-1562176566-e9afd27531d4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80",
            age=1,
            notes="Golden Retriever",
            available=True)

db.session.add_all([ava, larry, peaches, daisy])
db.session.commit()
