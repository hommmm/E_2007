import datetime
import logging
import json

import azure.functions as func

from .src.config import DATE_FORMAT, ENV
from .src import analyze_tweets, collect_tweets


def get_now():
    if ENV == "local":
        return datetime.datetime.now()
    else:
        return datetime.datetime.now() + datetime.timedelta(hours=9)


def main(req: func.HttpRequest, db: func.Out[func.Document], reports: func.DocumentList) -> func.HttpResponse:
    # ==========
    # define vars
    user_id = req.route_params.get('userId')
    report = len(reports) and reports[0]
    now_dt = get_now()
    logging.info(f'Python HTTP trigger function processed a request. user_id = {user_id}')

    resp_data = []
    if req.method == 'GET':
        if not report or "tweets" not in report:
            return func.HttpResponse(f"report not found. user_id = {user_id}", status_code=404)

        for tweet_data in report["tweets"]:
             resp_data.append({**tweet_data})

    elif req.method == 'POST':
        # ==========
        # collect tweets
        logging.info(f'Get tweets and filter them.')
        logging.info(f'report = {report}')
        if report and "updated_at" in report:
            updated_at = datetime.datetime.strptime(report["updated_at"], DATE_FORMAT)
            tweets = collect_tweets.get_all_tweets(user_id, updated_at)
        else:
            tweets = collect_tweets.get_all_tweets(user_id)
        filtered_tweets = collect_tweets.filter_tweets(tweets)
        user_info = collect_tweets.get_user(user_id)

        # ==========
        # analyze tweets
        logging.info(f"Analyze tweets. len(tweets) = {len(filtered_tweets)}")
        analyzed_tweets = analyze_tweets.analyze_tweets(filtered_tweets)

        # ==========
        # Add or Update DB
        if report:
            new_report = {
                **report,
                "name": user_info.name,
                "profile_image_url": user_info.profile_image_url,
                "updated_at": now_dt.strftime(DATE_FORMAT),
                "tweets": [*analyzed_tweets, *report['tweets']] if "tweets" in report else [*analyzed_tweets]
            }
        else: 
            new_report = {
                "user_id": user_id,
                "name": user_info.name,
                "profile_image_url": user_info.profile_image_url,
                "updated_at": now_dt.strftime(DATE_FORMAT),
                "tweets": analyzed_tweets
            }
        db.set(func.Document.from_dict(new_report))
        resp_data = new_report["tweets"][:5]
    
    return func.HttpResponse(json.dumps({'reports': resp_data}, ensure_ascii=False), headers={'Content-Type': 'application/json'})