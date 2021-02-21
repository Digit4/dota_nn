import os,json
import pandas as pd
import logging

class DataConverter():
    def __init__(self):
        super().__init__()
        self.dataset_dir = None
    
    def __init__(self,dataset_dir,param_file_dir):
        super().__init__()
        self.dataset_dir = dataset_dir
        self.param_file = os.path.join(os.path.abspath(os.curdir),'data_params','params.csv')
        logging.basicConfig(level=logging.DEBUG)

    def remove_old_data_file(self):
        try:
            param_file = os.path.join(self.param_file_dir,self.param_file)
            with open(self.param_file,'w') as f:
                f.write('')
        except:
            logging.info('param file does not exist, continuing...')

    def get_matches_all(self):
        matches = os.listdir(self.dataset_dir)
        df = pd.DataFrame()
        file_mode = 'w'
        for match in matches:
            with open(os.path.join(self.dataset_dir,match),'r') as match_file:
                data = json.load(match_file)
                radiant_win = data['radiant_win']
                heroes = [x['hero_id'] for x in data['players'] if x['isRadiant']]
                heroes_dire = [x['hero_id'] for x in data['players'] if not x['isRadiant']]
                heroes.extend(heroes_dire)
                heroes_df = pd.DataFrame(heroes).T.set_index(0)
                heroes_df['win'] = radiant_win
                # print(heroes_df)
                heroes_df.to_csv(self.param_file,mode=file_mode,header=False)
                file_mode = 'a'

    def get_matches(self):
        with open('prev_scraped.csv') as prev_scraped_f:
            prev_scraped = [x.replace('\n','.json') for x in prev_scraped_f.readlines()]
            
            for match in prev_scraped:
                with open(os.path.join(self.dataset_dir,match),'r') as match_file:
                    data = json.load(match_file)
                    radiant_win = data['radiant_win']
                heroes = [x['hero_id'] for x in data['players'] if x['isRadiant']]
                heroes_dire = [x['hero_id'] for x in data['players'] if not x['isRadiant']]
                heroes.extend(heroes_dire)
                heroes_df = pd.DataFrame(heroes).T.set_index(0)
                heroes_df['win'] = radiant_win
                heroes_df.to_csv(self.param_file,mode='a',header=False)




if __name__ == "__main__":
    directory = os.path.join(os.path.abspath(os.curdir),'data')
    params_dir = os.path.join(os.path.abspath(os.curdir),"data_params")
    converter = DataConverter(directory,params_dir)
    converter.get_matches_all()