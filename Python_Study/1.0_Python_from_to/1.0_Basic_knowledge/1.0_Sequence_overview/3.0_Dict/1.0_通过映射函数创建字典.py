# -*- coding: utf-8 -*-


user_name = ['XX', 'YY', 'ZZ', 'QQ']   # 作为键
user_id = ['11', '22', '33', '44']     # 作为值

dictionary = dict(zip(user_name, user_id))    # 转换成字典
print(dictionary)
# 输出结果： {'XX': '11', 'YY': '22', 'ZZ': '33', 'QQ': '44'}


dictionary1 = tuple(zip(user_name, user_id))  # 转换成元组
print(dictionary1)
# 输出结果：  (('XX', '11'), ('YY', '22'), ('ZZ', '33'), ('QQ', '44'))


dictionary2 = list(zip(user_name, user_id))   # 转换成列表
print(dictionary2)
# 删除结果:  [('XX', '11'), ('YY', '22'), ('ZZ', '33'), ('QQ', '44')]






