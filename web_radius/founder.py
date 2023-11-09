import os

BASE_DIR = os.path.abspath(os.path.join('..',  'web_radius'))
result_dict = {}
print('BASE DIR: ', BASE_DIR)

def find_str_in_folders(name_string, cur_path):



    for i_file in os.listdir(cur_path):
        path = os.path.join(cur_path, i_file)

        if os.path.isdir(os.path.abspath(path)):
            if 'MyBot' in os.path.basename(path):
                print(f'{i_file} Это директория. Переходим!')
                find_str_in_folders(name_string, path)
            elif path.endswith('venv') or 'bot' in os.path.basename(path):
                print('Папка с окружением. Игнорируем.')
                return
            else:
                print(f'{i_file} Это директория. Переходим!')
                find_str_in_folders(name_string, path)

        if 'founder' in path:
            print('Нашел сам себя: ', path)
            continue

        if path.endswith('.py') :

            with open(path, mode='r', encoding='utf-8') as file:
                counter_row = 1
                for i_str in file:
                    if name_string in i_str.lower():
                        result_dict[path] = {}
                        result_dict[path]['PATH'] = path
                        result_dict[path]['RESULT'] = i_str
                        result_dict[path]['NUMBER ROW'] = counter_row

                    counter_row += 1
        elif path.endswith('.html'):

            with open(path, mode='r', encoding='utf-8') as file:
                counter_row = 1
                for i_str in file:
                    if name_string in i_str.lower():
                        result_dict[path] = {}
                        result_dict[path]['PATH'] = path
                        result_dict[path]['RESULT'] = i_str
                        result_dict[path]['NUMBER ROW'] = counter_row

                    counter_row += 1
        elif path.endswith('.css') or path.endswith('.js'):
            with open(path, mode='r', encoding='utf-8') as file:
                counter_row = 1
                for i_str in file:
                    if name_string in i_str.lower():
                        result_dict[path] = {}
                        result_dict[path]['PATH'] = path
                        result_dict[path]['RESULT'] = i_str
                        result_dict[path]['NUMBER ROW'] = counter_row

                    counter_row += 1



    else:
        return result_dict





find_str_in_folders('AppSed'.lower(), BASE_DIR)
print('--------------------------------')
print('РЕЗУЛЬТАТЫ!')
for key, value in result_dict.items():
    for i_key, i_value in value.items():
        print(f'{i_key}: {i_value}')
    print('---------------------')
