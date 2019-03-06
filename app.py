from flask import Flask, render_template, request
from compute import k_means

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    check_files()
    pic_path = '/static/graphic_cache/20181025182829.png'
    if request.method == 'GET':
        return render_template("main_page.html", pic_path=pic_path)
    else:
        try:
            input_data = request.form.get('input_data')
            print(input_data)
            k_value = int(request.form.get('k_value'))
            data_li = input_data.split('\n')
            print(data_li)
            for index in range(len(data_li)):
                data_li[index] = data_li[index].split(',')
                data_li[index][0] = float(data_li[index][0])
                data_li[index][1] = float(data_li[index][1])
                data_li[index] = tuple(data_li[index])
            # print(data_li)
            cl, cores = k_means.k_means(data_li, k_value)
            pic_path = k_means.k_graphic(cl, cores, 'static/graphic_cache/')
            print(pic_path)
        except OSError:
            print('err')
            return '数据错误'

        return render_template("main_page.html", pic_path=pic_path)


def check_files():
    import os
    files = os.listdir('static/graphic_cache/')
    if len(files) > 10:
        os.remove('static/graphic_cache/' + files[1])
        print("{} has been removed.".format(files[1]))


if __name__ == '__main__':
    app.run()
