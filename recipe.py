import requests
import lxml.html

dish = input('Что готовим, мау?')
dish = dish.replace(' ', '-').lower()
url = f'https://tvoirecepty.ru/recept/{dish}'
api = requests.get(url)
tree = lxml.html.document_fromstring(api.text)
text = tree.xpath(
    '//*[@class="instructions"]/div//*[@class="instruction row-xs margin-bottom-20"]/text()')
final_output = ''.join(text)
final_output = final_output.replace(
    '                                        ', '')
final_output = final_output.replace(
    'Вопросы, предложения и пожелания - пишите в комментариях, я с радостью всем отвечу.', '')
print(final_output)
print(
    f'Более детально ознакомиться с рецептом и посмотреть фото вы можете здесь: {url}, мау 😼')
