# # seed_super_admin.py

# from app import create_app, db
# from app.models.user import User
# from werkzeug.security import generate_password_hash

# # Create Flask app context
# app = create_app()

# with app.app_context():
#     # Check if super admin already exists
#     super_admin_email = "superadmin@unihub.co.ug"
#     existing_admin = User.query.filter_by(email=super_admin_email).first()

#     if existing_admin:
#         print("✅ Super Admin already exists:", existing_admin.email)
#     else:
#         # Create new super admin user
#         super_admin = User(
#             first_name="Phiona",
#             last_name="Aladina",
#             email='phionaaladina@gmail.com',
#             contact='0773874765',
#             password=generate_password_hash("superadmin123"),  # 🔒 Secure it
#             user_type="super_admin"
#         )
#         db.session.add(super_admin)
#         db.session.commit()
#         print("✅ Super Admin account created successfully.")



from app import create_app, db
from app.models.user import User
from app.extensions import bcrypt  # <--- use flask_bcrypt's bcrypt

app = create_app()

with app.app_context():
    super_admin_email = "superadmin@unihub.co.ug"
    existing_admin = User.query.filter_by(email=super_admin_email).first()

    if existing_admin:
        print("✅ Super Admin already exists:", existing_admin.email)
    else:
        hashed_password = bcrypt.generate_password_hash("superadmin123").decode('utf-8')

        super_admin = User(
            first_name="Phiona",
            last_name="Aladina",
            email='phionaaladina@gmail.com',
            contact='0773874765',
            password=hashed_password,
            user_type="super_admin"
        )
        db.session.add(super_admin)
        db.session.commit()
        print("✅ Super Admin account created successfully.")
