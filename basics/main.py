""" Tell the story about the duck painter """


# Guido van Rossum <guido@python.org>

def step1():
    """ Start the story with the duck painter """
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    """ Run the scenario in which the duck took the umbrella """
    print('По пути в бар утка-маляр не попала под дождь. \n'
          'Она вошла в бар, вся раздосадованная отсутствием осадков, '
          'и заказала водку с крошками. \n'
          'Через пару минут напиток был готов. Но о ужас! '
          'На нём не было пестрящего зонтика. \n'
          'Утка-маляр решила явно намекнуть бармену об отсутствии важного \n'
          'штриха и со всей дури кинула свой зонт в несчастную рюмку. \n'
          'Близстоящие существа резко повернулись в её сторону, '
          'недоумевая от происходящего. \n'
          'А утка лишь прошептала: "Всё-таки пригодился!"'
          )


def step2_no_umbrella():
    """ Run the scenario in which the duck didn't take the umbrella """
    print(
        'В итоге, как назло, утка попала под страшный ливень. \n'
        'Гневно крякая что-то про себя, она зашла в бра и уселась за стойку. \n'
        'К утке подошёл петух-столяр, её коллега, и заказал водку с крошками'
        ' и небольшим зонтиком, \n'
        'сказав: "Пусть хоть где-то у тебя будет зонтик" \n'
    )


if __name__ == '__main__':
    step1()
