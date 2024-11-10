import x
import uuid
import time
import random
from werkzeug.security import generate_password_hash
from faker import Faker

fake = Faker()

from icecream import ic
ic.configureOutput(prefix=f'***** | ', includeContext=True)

try:
    db, cursor = x.db()

    ##############################
    cursor.execute("DROP TABLE IF EXISTS users_roles") # dependent table
    cursor.execute("DROP TABLE IF EXISTS users")
    q = """
        CREATE TABLE users (
            user_pk CHAR(36),
            user_name VARCHAR(20) NOT NULL,
            user_last_name VARCHAR(20) NOT NULL,
            user_email VARCHAR(100) NOT NULL UNIQUE,
            user_password VARCHAR(255) NOT NULL,
            user_avatar VARCHAR(50),
            user_created_at INTEGER UNSIGNED,
            user_deleted_at INTEGER UNSIGNED,
            user_blocked_at INTEGER UNSIGNED,
            user_updated_at INTEGER UNSIGNED,
            user_verified_at INTEGER UNSIGNED,
            user_verification_key CHAR(36),
            PRIMARY KEY(user_pk)
        )
        """        
    cursor.execute(q)


    ##############################
    cursor.execute("DROP TABLE IF EXISTS roles")
    q = """
        CREATE TABLE roles (
            role_pk CHAR(36),
            role_name VARCHAR(10) NOT NULL UNIQUE,
            PRIMARY KEY(role_pk)
        );
        """        
    cursor.execute(q)


    ##############################    
    q = """
        CREATE TABLE users_roles (
            user_role_user_fk CHAR(36),
            user_role_role_fk CHAR(36),
            PRIMARY KEY(user_role_user_fk, user_role_role_fk)
        );
        """        
    cursor.execute(q)
    cursor.execute("ALTER TABLE users_roles ADD FOREIGN KEY (user_role_user_fk) REFERENCES users(user_pk) ON DELETE CASCADE ON UPDATE RESTRICT") 
    cursor.execute("ALTER TABLE users_roles ADD FOREIGN KEY (user_role_role_fk) REFERENCES roles(role_pk) ON DELETE CASCADE ON UPDATE RESTRICT") 


    ############################## 
    # Create roles
    admin_role_pk = str(uuid.uuid4())
    customer_role_pk = str(uuid.uuid4())
    partner_role_pk = str(uuid.uuid4())
    restaurant_role_pk = str(uuid.uuid4())
    q = f"""
        INSERT INTO roles (role_pk, role_name)
        VALUES ("{admin_role_pk}", "admin"), ("{customer_role_pk}", "customer"), ("{partner_role_pk}", "partner"), ("{restaurant_role_pk}", "restaurant")
        """
    cursor.execute(q)

    ############################## 
    # Create admin user
    user_pk = str(uuid.uuid4())
    user_name = "Santiago"
    user_last_name = "Donoso"
    user_email = "admin@fulldemo.com"
    user_password = generate_password_hash("password")
    user_avatar = "profile_10.jpg"
    user_created_at = int(time.time())
    user_deleted_at = 0
    user_blocked_at = 0
    user_updated_at = 0
    user_verified_at = int(time.time())
    user_verification_key = str(uuid.uuid4()) 

    values = (
        user_pk,
        user_name,
        user_last_name,
        user_email,
        user_password,
        user_avatar,
        user_created_at,
        user_deleted_at,
        user_blocked_at,
        user_updated_at,
        user_verified_at,
        user_verification_key
    )       
    q = """
        INSERT INTO users
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)        
        """
    cursor.execute(q, values)
    
    # Assign role to admin user
    q = f"""
        INSERT INTO users_roles (user_role_user_fk, user_role_role_fk) VALUES ("{user_pk}", "{admin_role_pk}")        
        """    
    cursor.execute(q)

   ############################## 
    # Create customer
    user_pk = str(uuid.uuid4())
    user_name = "John"
    user_last_name = "Customer"
    user_email = "customer@fulldemo.com"
    user_password = generate_password_hash("password")
    user_avatar = "profile_11.jpg"
    user_created_at = int(time.time())
    user_deleted_at = 0
    user_blocked_at = 0
    user_updated_at = 0
    user_verified_at = int(time.time())
    user_verification_key = str(uuid.uuid4()) 

    values = (
        user_pk,
        user_name,
        user_last_name,
        user_email,
        user_password,
        user_avatar,
        user_created_at,
        user_deleted_at,
        user_blocked_at,
        user_updated_at,
        user_verified_at,
        user_verification_key
    )       
    q = """
        INSERT INTO users
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)        
        """
    cursor.execute(q, values)
    
    # Assign role to admin user
    q = f"""
        INSERT INTO users_roles (user_role_user_fk, user_role_role_fk) VALUES ("{user_pk}", "{customer_role_pk}")        
        """    
    cursor.execute(q)


   ############################## 
    # Create partner
    user_pk = str(uuid.uuid4())
    user_name = "John"
    user_last_name = "Partner"
    user_email = "partner@fulldemo.com"
    user_password = generate_password_hash("password")
    user_avatar = "profile_12.jpg"
    user_created_at = int(time.time())
    user_deleted_at = 0
    user_blocked_at = 0
    user_updated_at = 0
    user_verified_at = int(time.time())
    user_verification_key = str(uuid.uuid4()) 

    values = (
        user_pk,
        user_name,
        user_last_name,
        user_email,
        user_password,
        user_avatar,
        user_created_at,
        user_deleted_at,
        user_blocked_at,
        user_updated_at,
        user_verified_at,
        user_verification_key
    )       
    q = """
        INSERT INTO users
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)        
        """
    cursor.execute(q, values)
    
    # Assign role to admin user
    q = f"""
        INSERT INTO users_roles (user_role_user_fk, user_role_role_fk) VALUES ("{user_pk}", "{partner_role_pk}")        
        """    
    cursor.execute(q)

   ############################## 
    # Create restaurant
    user_pk = str(uuid.uuid4())
    user_name = "John"
    user_last_name = "Restaurant"
    user_email = "restaurant@fulldemo.com"
    user_password = generate_password_hash("password")
    user_avatar = "profile_13.jpg"
    user_created_at = int(time.time())
    user_deleted_at = 0
    user_blocked_at = 0
    user_updated_at = 0
    user_verified_at = int(time.time())
    user_verification_key = str(uuid.uuid4()) 

    values = (
        user_pk,
        user_name,
        user_last_name,
        user_email,
        user_password,
        user_avatar,
        user_created_at,
        user_deleted_at,
        user_blocked_at,
        user_updated_at,
        user_verified_at,
        user_verification_key
    )       
    q = """
        INSERT INTO users
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)        
        """
    cursor.execute(q, values)
    
    # Assign role to admin user
    q = f"""
        INSERT INTO users_roles (user_role_user_fk, user_role_role_fk) VALUES ("{user_pk}", "{restaurant_role_pk}")        
        """    
    cursor.execute(q)


    ############################## 
    # Create 50 customer
    q_customers = """
        INSERT INTO users (
            user_pk,
            user_name,
            user_last_name,
            user_email,
            user_password,
            user_avatar,
            user_created_at,
            user_deleted_at,
            user_blocked_at,
            user_updated_at,
            user_verified_at,
            user_verification_key)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    
    q_customers_role = """
        INSERT INTO users_roles (
            user_role_user_fk,
            user_role_role_fk)
            VALUES (%s, %s)
        """

    domains = ["example.com", "testsite.org", "mydomain.net", "website.co", "fakemail.io", "gmail.com", "hotmail.com"]
    user_password = hashed_password = generate_password_hash("password")
    for _ in range(50):
        
        user_pk = str(uuid.uuid4())
        user_name = fake.first_name()
        user_last_name = fake.last_name()
        user_email = fake.unique.user_name() + "@" + random.choice(domains)
        # user_password = hashed_password = generate_password_hash(fake.password(length=20))
        user_avatar = "profile_"+ str(random.randint(1, 100)) +".jpg"
        user_created_at = int(time.time())
        user_deleted_at = 0
        user_blocked_at = 0
        user_updated_at = 0
        user_verified_at = 0
        user_verification_key = str(uuid.uuid4())

        values_customer = (
            user_pk,
            user_name,
            user_last_name,
            user_email,
            user_password,
            user_avatar,
            user_created_at,
            user_deleted_at,
            user_blocked_at,
            user_updated_at,
            user_verified_at,
            user_verification_key
        )

        values_customer_role = (user_pk, customer_role_pk)

        cursor.execute(q_customers, values_customer)
        cursor.execute(q_customers_role, values_customer_role)


   ############################## 
    # Create 50 partners
    q_partners = """
        INSERT INTO users (
            user_pk,
            user_name,
            user_last_name,
            user_email,
            user_password,
            user_avatar,
            user_created_at,
            user_deleted_at,
            user_blocked_at,
            user_updated_at,
            user_verified_at,
            user_verification_key)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
    
    q_partners_role = """
        INSERT INTO users_roles (
            user_role_user_fk,
            user_role_role_fk)
            VALUES (%s, %s)
        """

    user_password = hashed_password = generate_password_hash("password")
    for _ in range(50):
        user_pk = str(uuid.uuid4())
        user_name = fake.first_name()
        user_last_name = fake.last_name()
        user_email = fake.unique.email()
        # user_password = hashed_password = generate_password_hash(fake.password(length=20))
        user_avatar = "profile_"+ str(random.randint(1, 100)) +".jpg"
        user_created_at = int(time.time())
        user_deleted_at = 0
        user_blocked_at = 0
        user_updated_at = 0
        user_verified_at = 0
        user_verification_key = str(uuid.uuid4())

        values_customer = (
            user_pk,
            user_name,
            user_last_name,
            user_email,
            user_password,
            user_avatar,
            user_created_at,
            user_deleted_at,
            user_blocked_at,
            user_updated_at,
            user_verified_at,
            user_verification_key
        )

        values_customer_role = (user_pk, partner_role_pk)

        cursor.execute(q_partners, values_customer)
        cursor.execute(q_partners_role, values_customer_role)

    db.commit()

except Exception as ex:
    ic(ex)
    if "db" in locals(): db.rollback()

finally:
    if "cursor" in locals(): cursor.close()
    if "db" in locals(): db.close()


