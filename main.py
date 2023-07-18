from multiprocessing import Pool
from multiprocessing import cpu_count
import pandas as pd
import random
from pymongo import MongoClient
import pandas as pd
from tqdm import tqdm
from faker import Faker
from models.investor import generate_investor
from models.borrower import generate_borrower
from models.deal import generate_deal
from models.express_interest import generate_express_interest

fake = Faker()

num_cores = cpu_count() - 1
def create_dataframe(arg):
    x = int(12/num_cores)
    data = pd.DataFrame()
    for i in tqdm(range(x), desc='Creating DataFrame'):
        data.loc[i, 'first_name'] = fake.first_name()
        data.loc[i, 'last_name'] = fake.last_name()
        data.loc[i, 'job'] = fake.job()
        data.loc[i, 'address'] = fake.address()
        data.loc[i, 'city'] = fake.city()
        data.loc[i, 'email'] = fake.email()
        data.loc[i, 'company'] = fake.company()
    return data

if __name__ == "__main__":
    # num_cores = cpu_count() - 1
    # with Pool() as pool:
    #     data = pd.concat(pool.map(create_dataframe, range(num_cores)))
    # data_dict = data.to_dict('records')
    uri = "mongodb://localhost:27017/company"
    client = MongoClient(uri)
    # db = client["company"]

    # collection = db["employees"]
    # res = collection.insert_many(data_dict)
    # print(res.inserted_ids)
    # print([type(r) for r in res.inserted_ids])
    db = client["yubidb"]
    investor_collection = db["investors"]
    borrower_collection = db["borrowers"]
    deal_collection = db["deals"]
    express_interest_collection = db["express_interests"]
    investors_list = [generate_investor() for i in range(1_000)]
    investor_ids = investor_collection.insert_many(investors_list).inserted_ids
    print("investor_ids: ", len(investor_ids))
    borrowers_list = [generate_borrower() for i in range(2_000)]
    borrower_ids = borrower_collection.insert_many(borrowers_list).inserted_ids
    print("borrower_ids: ", len(borrower_ids))
    deals_list = [generate_deal(borrower_id=borrower_id) for borrower_id in borrower_ids for i in range(random.randint(0, 6))]
    deal_ids = deal_collection.insert_many(deals_list).inserted_ids
    print("deal_ids: ", len(deal_ids))
    express_interests_list = [generate_express_interest(investor_id=investor_id, deal_id=deal_id) for investor_id in investor_ids for deal_id in deal_ids if random.randint(0, 1)]
    express_interest_ids = express_interest_collection.insert_many(express_interests_list).inserted_ids
    print("express_interest_ids: ", len(express_interest_ids))
    # print(generate_investor())
    # print(generate_borrower())
    # print(generate_deal(random.randint(10000000, 1000000000)))
