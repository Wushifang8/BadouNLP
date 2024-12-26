#week3作业

#词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

#待切分文本
sentence = "经常有意见分歧"

#实现全切分函数，输出根据字典能够切分出的所有的切分方式
def all_cut(sentence, Dict):
    #TODO
    def backtrack(start, path):
        # 如果当前路径的长度等于句子的长度，说明找到了一个完整的切分方式
        if start == len(sentence):
            result.append(path[:])
            print('result 添加内容', path[:])
            return
        for end in range(start + 1, len(sentence) + 1):
            # 检查当前切分的词是否在词典中
            word = sentence[start:end]
            if word in Dict:
                # 如果在词典中，将其添加到当前路径中，通过递归继续切分剩余部分
                path.append(word)
                backtrack(end, path)
                # 回溯，移除当前词，尝试其他切分方式
                path.pop()

    result = []
    backtrack(0, [])
    return result

#目标输出;顺序不重要
target = [
    ['经常', '有意见', '分歧'],
    ['经常', '有意见', '分', '歧'],
    ['经常', '有', '意见', '分歧'],
    ['经常', '有', '意见', '分', '歧'],
    ['经常', '有', '意', '见分歧'],
    ['经常', '有', '意', '见', '分歧'],
    ['经常', '有', '意', '见', '分', '歧'],
    ['经', '常', '有意见', '分歧'],
    ['经', '常', '有意见', '分', '歧'],
    ['经', '常', '有', '意见', '分歧'],
    ['经', '常', '有', '意见', '分', '歧'],
    ['经', '常', '有', '意', '见分歧'],
    ['经', '常', '有', '意', '见', '分歧'],
    ['经', '常', '有', '意', '见', '分', '歧']
]

# 调用函数
target = all_cut(sentence, Dict)
print(target)

