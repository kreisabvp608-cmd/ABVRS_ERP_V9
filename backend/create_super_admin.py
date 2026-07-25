from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.user import User
from app.auth.hashing import hash_password


def create_super_admin():
    db: Session = SessionLocal()

    try:
        existing_user = (
            db.query(User)
            .filter(User.username == "admin")
            .first()
        )

        if existing_user:
            print("✅ Super Admin already exists.")
            return

        admin = User(
            username="admin",
            password_hash=hash_password("Admin@123"),
            full_name="System Administrator",
            email="admin@abvrs.local",
            mobile="9999999999",
            role="SUPER_ADMIN",
            is_active=True,
        )

        db.add(admin)
        db.commit()

        print("✅ Super Admin created successfully!")
        print("Username : admin")
        print("Password : Admin@123")

    except Exception as e:
        db.rollback()
        print("❌ Error:", e)

    finally:
        db.close()


if __name__ == "__main__":
    create_super_admin()