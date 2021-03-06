import random


class DataClass:
    bases = 'bases/'
    fbase = 'base.json'
    fimage = 'image'
    prefixbase = 'm', 'd'
    pointer = [
        '&#10145;', '&#128077;', '&#128226;', '&#128172;', '&#128161;', '&#9999;', '&#10002;', '&#10004;',
        '&#9193;', '&#9654;', '&#128266;', '&#9997;', '&#128073;', '&#128483;', '*&#8419;'
    ]
    delete_msg_blacklist = [
        'ремонт цоколя здания администрации города малмыжа', 'закупаю коров на мясо', 'мой брат попал в беду',
        'iqos', 'айкос', 'вейп', 'ploom', 'кальян', 'джул', 'новый взгляд', 'всё по карману', 'освр',
        'частный клининг', 'снова в наличии', 'метелица', 'николай дубравин', 'узнай своих поклонниц',
        'запустили производство профнастила', 'большое поступление', 'закажу второй портрет',
        'в салоне метелица', 'метелица - тепло отношений', 'magiccanvas24', 'оплата при получении',
        'к. маркса 78', 'карла маркса,92', 'карла маркса, 92', 'к. маркса, 20', 'К-Маркса 88', 'К-Маркса, 88',
        '912-828-33-85',
        '89229258077', 'наши именинники', 'любой продукт', 'любое фото', '1 фото', 'любое средство', '1фото',
        'каждая по 180', 'всё по 500', 'каждое по 150', 'любая за 350', 'любая по 350', '150р!',
        '300р!', '950р', 'Любая 300р!', '500р!', 'ночной крем', 'в наличии 800р!', 'любое средство - 150р',
        'пробники', 'пробник', 'выезжаем в любой регион россии', 'банкротство', 'котят', 'котята', 'кошка', 'кошку',
        'котенок', 'котенка', 'кошечка', 'кошечку', 'котик', 'котёнка', 'мышеловка', 'кот',
        'собака', 'собаку', 'собачка', 'собачку', 'щенка', 'щенок', 'щенков', 'щенки', 'щенят', 'щеночка', 'пёс',
        'пёсики', 'песики', 'котики',
        'туалетная вода', 'передержку', 'красная весна', 'кургинян', 'замалчивается', 'замалчивает',
        'любая шампунь', 'бурение скважин', 'по 145р', 'любое мыло', 'красное-белое',
        'брала для мамы массажную подушку', 'второй этаж флагман',
        'любое средство-150', 'массажная подушка', 'всё по карману', 'распродажа', 'ждем вас за покупками',
        'видеоуроки на заказ', 'зимний стиль', 'кодовые замки', 'профессиональный спил'
                                                                'приглашаем за покупками', 'группу совместных покупок',
        'покупать товары', 'с нами выгодно', 'интересные закупки',
        'пункт выдачи в г.малмыж', 'цены снижены', 'вышел новый айфон', 'добреев', 'minifit'
    ]
    delete_word = [
        'Не анон', 'не анон', 'НЕ АНОН', 'неанон', 'не АНОН',
        'анонимно', 'Анонимно', 'АНОНИМНО', 'ананимно',
        'пожалуйста', 'Пожалуйста', 'ПОЖАЛУЙСТА', 'пожалуйсто',
        'пожалуста', 'Пожалуста', 'ПОЖАЛУСТА',
        'Анон)', 'АНОН', 'анон', 'Анон',
        'Админу добра'
    ]
    delete_bad_simbol = ' .!,\n'

    size_base_old_posts = 500  # количество
    difference_old_posts = 259200  # в секундах (259200 секунд это 3 дня)


class AvtorTut:
    def avtortut(txt, owner_id, id):
        if ' -> https://vk.com/wall' not in txt:
            random.shuffle(pointer)
            return pointer[0] + ' ' + txt + ' -> https://vk.com/wall' + str(owner_id) + '_' + str(id)
        return txt