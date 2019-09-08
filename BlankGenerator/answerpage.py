from flask import request

def answer():
    test_form = ''
    test_form += '<p>결과</p><br><br>'
    num = request.form['num']
    n = request.form['n']
    ans = []
    answer = []
    i = 0
    while True:
        answer.append(request.form['n' + str(i)])
        if i == int(n):
            break
        i += 1
    i = 0
    while True:
        ans.append(request.form['test' + str(i)])
        if i == int(num):
            break
        i += 1
    n = 0
    m = ''
    for m in answer:
        if m != ans[n]:
            test_form += str(n+1) + '. ' + ans[n] + ' -> ' + m + '<br>'
        else:
            test_form += str(n+1) + '. Correct<br>'
        n += 1
    return test_form