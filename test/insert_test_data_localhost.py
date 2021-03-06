import sys
import os
#sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import csv
from datetime import datetime, timedelta
from app.models import User, Dataset, Pipeline
from app import db

class InsertTestDataset(object):

    def __init__(self):
        self.users_file = 'users.csv'
        self.datasets_file = 'datasets.csv'
        self.datasets_stats_file = 'datasets_stats.csv'
        self.pipelines_file = 'pipelines.csv'
        self.loris_image = 'loris.png'

    def insert_sample_users(self):

        with open(self.users_file, 'r') as users_file:

            reader = csv.reader(users_file)
            next(reader)

            for row in reader:
                user = User(
                    id = row[0],
                    oauth_id = row[1],
                    username = row[2],
                    email = row[3],
                    is_whitelisted = row[4] == 'True',
                    is_pi = row[5] == 'True',
                    is_account_expired = row[6] == 'True',
                    affiliation = row[7],
                    expiration = datetime.now() + timedelta(6*365/12), # 6 months
                    date_created = datetime.now(),
                    date_updated = datetime.now()
                )
                user.set_password('p4ssword')
                db.session.add(user)
        db.session.commit()
        users_file.close()


    def insert_sample_datasets(self):

        with open(self.datasets_file, 'r') as dataset_file:
            reader = csv.reader(dataset_file)
            next(reader)

            for row in reader:
                dataset = Dataset(
                    dataset_id = row[0],
                    annex_uuid = row[1],
                    description = row[2],
                    owner_id = row[3],
                    download_path = row[4],
                    raw_data_url = row[5],
                    name = row[6],
                    modality = row[7],
                    version = row[8],
                    format = row[9],
                    category = row[10],
                    image = self.read_image(row[11]),
                    date_created = datetime.now(),
                    date_updated = datetime.now(),
                    is_private = row[12] == 'True'
                )
                db.session.add(dataset)
        db.session.commit()
        dataset_file.close()

    def read_image(self,image):
        return open(image,'rb').read()


    def insert_sample_pipelines(self):

        with open(self.pipelines_file, 'r') as pipelines_file:

            reader = csv.reader(pipelines_file)
            next(reader)

            for row in reader:
                pipeline = Pipeline(
                    id = row[0],
                    pipeline_id = row[1],
                    owner_id = row[2],
                    name = row[3],
                    version = row[4],
                    is_private = row[5] == 'True',
                    date_created = datetime.now(),
                    date_updated = datetime.now()
                )
                db.session.add(pipeline)
        db.session.commit()
        pipelines_file.close()


test_dataset = InsertTestDataset()
#test_dataset.insert_sample_users()
test_dataset.insert_sample_datasets()
#test_dataset.insert_sample_pipelines()
#print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

