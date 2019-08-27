from locust import HttpLocust, TaskSet, task
# def IsnotDaiZi(l):
#     heade = {'Content-Type': 'application/json'}
#     param = {'appCode': 'SN190604155914000323'}
#     res = l.client.get('/api/order/getPaperless', params=param, headers=heade)
#     if res.status_code == 200:
#         print('response success')
#     else:
#         print('response false')


def shouye(l):
    header={'vkey':'ta8JmkuiG7mZ0Nkk4G2z5D47j67IVB10d6Q68PMwTATB0ZeiolezajGcX/5Z/1JU3SfAl615EBF+g3TgZAV5CQ==','X-di':'b7788172face52f6','Content-Type': 'application/json'}
    res = l.client.get('/system/home', headers=header)
    if res.status_code == 200:
        print('response success')
    else:
        print('response false')

class UserBehavier(TaskSet):
    @task
    def getIsNotDianzi(self):
        shouye(self)



class WebsitUser(HttpLocust):
    host = 'http://crmapi-test.victorplus.cn'
    task_set = UserBehavier
    min_wait = 3000
    max_wait = 5000