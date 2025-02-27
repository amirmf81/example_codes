from redis import Redis
redis = Redis('localhost', 6379, decode_responses=True)


def get_company_scale_func(company_id):
    scales = eval(redis.get(f"scale_{company_id}"))
    return scales
