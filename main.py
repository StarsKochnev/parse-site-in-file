import requests
import lxml.html
import os

def parse(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="TopPanel"]/div[5]/div/div/div/div/div[1]/div[2]/div[6]/div[4]/div/div/text()')
    print(text_original)
    # /div/div/text() это поиск текста в div внутри div
    with open('songs/4.txt', 'w') as ouf:
        for i in text_original:
            ouf.write((i) )
            print(i)
    # теперь вытаскиваем из ссылки название исполнителя и присваиваем файлу
    a = url
    s1 = a.replace("https://www.beesona.ru/songs/", "")
    s2 = s1.replace(".php", "")
    s3 = s2.replace("/", "-")
    # удалили ненужное и теперь переименовываем наш файл с добавлением расширения
    os.rename('songs/4.txt', 'songs/' + s3 + '.txt')

    print('Создан файл в папке songs', s3 + '.txt')

def parse2(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="TopPanel"]/div[5]/div/div/div/div/div[1]/div[2]/div[6]/div[4]/div/div/p/text()')
    print(text_original)
    # /div/div/text() это поиск текста в div внутри div

    with open('songs/4.txt', 'w') as ouf:
        for i in text_original:
            ouf.write((i) + '\n')
            print(i)
    # теперь вытаскиваем из ссылки название исполнителя и присваиваем файлу
    a = url
    s1 = a.replace("https://www.beesona.ru/songs/", "")
    s2 = s1.replace(".php", "")
    s3 = s2.replace("/", "-")
    # удалили ненужное и теперь переименовываем наш файл с добавлением расширения

    os.rename('songs/4.txt', 'songs/' + s3 + '2.txt')
    print(s3)

def main():
    print('введите ссылку с песней типа: https://www.beesona.ru/songs/ddt/chto_takoe_osen.php')
    parse(input()) #https://www.beesona.ru/songs/ddt/chto_takoe_osen.php
main()
print('!!!!Если текст пустой введите еще раз ссылку!!!')
parse2(input())

