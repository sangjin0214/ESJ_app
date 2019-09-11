from BlankGenerator import blankgenerator

def test(difficulty, title):
    test, answer = blankgenerator.process(difficulty, title)
    exp = ['!', '@', '#', '$', '.', ',', '-', '&', '(', ')', '*', '?', ';', ':', '"', "'"]
    test_form = ''
    test_form += '<p>문제</p><br>'
    test_form += '<form action="/blankgenerator/answer" method="post">'
    num = 0
    n = 1
    for text in test:
        test_form += str(n) + '번 지문<br>'
        for word in text:
            if word == '':
                test_form += ' <input type="text" name="test' + str(num) + '">'
                num += 1
            else:
                if word in exp:
                    test_form += word
                else:
                    test_form += ' ' + word
        n += 1
        test_form += '<br><br><br>'
    test_form += '<input type="hidden" name="num" value="' + str(num-1) + '"><br>'
    num = 0
    for temp in answer:
        test_form += '<input type="hidden" name="n' + str(num) + '" value="' + temp + '">'
        num += 1
    test_form += '<input type="hidden" name="n" value="' + str(num-1) + '">'
    test_form += '<input type="submit" value="제출">'
    test_form += '</form>'
    return test_form