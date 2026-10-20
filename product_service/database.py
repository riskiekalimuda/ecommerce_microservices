import motor.motor_asyncio

#koneksi ke mongodb
MONGO_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)


#database untuk product services
db = client.product_db
product_collection = db.get_collection("products")