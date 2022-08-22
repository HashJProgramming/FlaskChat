data = {
'user_id': 1,
'username': 'wewe',
'message': 'wewe'
};   

data.update({'user_id': 2, 'username': '123', 'message': 'wewe'})
print(data.get('username'))