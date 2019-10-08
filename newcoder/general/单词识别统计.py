# 牛客网
# @See https://www.nowcoder.com/practice/16f59b169d904f8898d70d81d4a140a0?tpId=94&&tqId=31064&rp=1&ru=/activity/oj&qru=/ta/bit-kaoyan/question-ranking
# 输入一个英文句子，把句子中的单词(不区分大小写)按出现次数按从多到少把单词和次数在屏幕上输出来，
#   要求能识别英文句号和逗号，即是说单词由空格、句号和逗号隔开。(按字典序排、同字典序的按出现次数从多到少)
# 输入有若干行，总计不超过1000个字符。 __ 使用input()输入
# -----------------------------------------------------------
#   这题测试样例坑得一笔，没有太大做的必要。熟悉熟悉输入输出方式就行了
# -----------------------------------------------------------
# 样例输入：A blockhouse is a small castle that has four openings through which to shoot.
# 样例输出:
# a:2
# blockhouse:1
# castle:1
# four:1
# has:1
# is:1
# openings:1
# shoot:1
# small:1
# that:1
# through:1
# to:1
# which:1

if __name__ == '__main__':
    st = 'A blockhouse is a small castle that has four openings through which to shoot.'  # instead of `st = input()`
    st = st.replace(',', ' ').replace('.', ' ').lower()
    # API: str.split(str="", num=string.count(str)).
    # str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    # num -- 分割次数。默认为 -1, 即分隔所有。
    sts = st.split()
    # 要注意 spilt(' ')和spilt()不一样：print(len(' '.split(' '))) => 2 || print(len(' '.split())) => 0
    sts.sort()
    dicts = {}
    for i in sts:
        dicts[i] = dicts.get(i, 0) + 1
    dicts = sorted(dicts.items())
    for i in dicts:
        print('%s:%s' % i)
