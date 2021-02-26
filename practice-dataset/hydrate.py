import re
import sys
import pandas as pd
import twint
import json
import argparse
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('target', type=argparse.FileType('wt'))
    args = parser.parse_args()
    count = 0
    for line in open(args.source):
        count += 1
    for line in tqdm(open(args.source), desc='hydrating user', ncols=80, total=count):
        data = json.loads(line)
        c = twint.Config()
        c.User_id = data['id']
        c.Format = ""
        c.Limit = 5000
        c.year  = 2020
        c.Output = 'tmp'
        c.Store_object = True
        c.Hide_output = True
        try:
            twint.run.Search(c)
            id2idx = {str(tweet['id']): i for i, tweet in enumerate(data['tweets'])}
            for tweet in twint.output.tweets_list:
                if str(tweet.id) in id2idx:
                    text = re.sub(r'#\w+', '', tweet.tweet) # remove hashtags
                    data['tweets'][id2idx[str(tweet.id)]]['text'] = text
                    del id2idx[str(tweet.id)]
            if id2idx:
                print(f"couldn't find {len(id2idx)} tweets for user {data['id']}")
            json.dump(data, args.target)
            args.target.write('\n')
            args.target.flush()
        except:
            ex = sys.exc_info()[0]
            print(f'error for user {data["id"]}. Skipping. {ex}')

if __name__ == '__main__':
    main()
