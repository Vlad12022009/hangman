

def return_game(life):
    while True:
        if slovo_secret_list == list(slovo):
                   win_screen()
                   break
                
        else:
            if life != 0:
                game(slovo_secret, life)
            

def win_screen():
    print('Молодцы!!! Вы выйграли!!')
    
def game(slovo_secret, life):
    bykva = input('Введите букву:')
    slovo_secret = i_in_slovo(slovo_secret, bykva, life)
    return slovo_secret



def i_in_slovo(slovo_secret, bykva, life):
    
    for i in slovo:
        if i == bykva:
            slovo_secret = secretfunc(bykva)

    life_proverka_func(slovo_secret, bykva, life)
    

def life_proverka_func(slovo_secret, bykva, life):
    
    if slovo_secret != secretfunc(bykva):
        life = lose_screen(life)
        
    print_slovo_secret(slovo_secret, life)



def print_slovo_secret(slovo_secret, life):
    if life != 0:
        print('Слово ' + ''.join(map(str,slovo_secret)))
    return_game(life)


def  lose_screen(life):
    life = life - 1
    if life == 0:
        return lose_func()
    else:
        print(f'Осталось {life} попытки')
        return life


def lose_func():
    print('Вы проиграли!!')
    return 0

    
def secretfunc(x):
    q = 0
    for i in slovo_list:
            if i == x:
                slovo_secret_list[q] = slovo_list[q]
            q += 1
    return slovo_secret_list


def start():
    print(f'''
    Добро пожаловать в игру - hangman 2000
    Ваша задача угадать загаданное слово за несколько попыток,
    иначе вас ждет расплата!
    
    Загаданное слово состоит из {len(slovo)} букв {slovo_secret}
    ''')
    return_game(3)
    
    
slovo = 'orange'
slovo_secret =  '______'
slovo_secret_list = []
slovo_list = []
slovo_secret_list += slovo_secret
slovo_list += slovo
start()




