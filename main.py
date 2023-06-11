from multiprocessing import Pool
from multiprocessing import cpu_count
import pandas as pd
from pymongo import MongoClient
import pandas as pd
from tqdm import tqdm
from faker import Faker

fake = Faker()

num_cores = cpu_count() - 1
def create_dataframe(arg):
    x = int(60000/num_cores)
    data = pd.DataFrame()
    for i in tqdm(range(x), desc='Creating DataFrame'):
        data.loc[i, 'first_name'] = fake.first_name()
        data.loc[i, 'last_name'] = fake.last_name()
        data.loc[i, 'job'] = fake.job()
        data.loc[i, 'address'] = fake.address()
        data.loc[i, 'city'] = fake.city()
        data.loc[i, 'email'] = fake.email()
    return data

if __name__ == "__main__":
    num_cores = cpu_count() - 1
    with Pool() as pool:
        data = pd.concat(pool.map(create_dataframe, range(num_cores)))
    data_dict = data.to_dict('records')
    uri = "mongodb://localhost:27017/company"
    client = MongoClient(uri)
    db = client["company"]

    collection = db["employees"]
    collection.insert_many(data_dict)