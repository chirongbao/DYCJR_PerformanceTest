from locust import HttpLocust, TaskSet, task


class UserBebavier(TaskSet):
    @task
    def getIsNotDianzi(self):
        heade = {'vkey':'ta8JmkuiG7mZ0Nkk4G2z5D47j67IVB10d6Q68PMwTATB0ZeiolezajGcX/5Z/1JU3SfAl615EBF+g3TgZAV5CQ==','X-di':'b7788172face52f6','Content-Type': 'application/json'}
        # param = {'appCode': 'SN190604155914000323'}
        res = self.client.get('/api/order/getPaperless',params=param, headers=heade)
        if res.status_code != 200:
            print('返回异常')
        else:
            print('返回正常')



class WebsitUser(HttpLocust):
    host = 'http://crmprovider.test.victorplus.cn'
    task_set = UserBebavier
    min_wait = 3000
    max_wait = 6000
