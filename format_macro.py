import os

# Example for 'content' dictionary structure
content_structure_example = {
    'Ellipse_ORIGINAL_05.setting': {
        'source_name': 'Ellipse_ORIGINAL_05.setting',
        'source_path': './Ellipse_ORIGINAL_05.setting',
        'source_content': {
            5: {
                "line": 5,
                "line_content": '\t\t\t\tInput2 = InstanceInput {\n',
                "char_count": 34,
                "tabs": 3,
                "comma": None,
                "comma_idx": None,
                "braces_open": None,
                "braces_open_idx": None,
                "braces_closed": None,
                "braces_closed_idx": None,
            },
            6: {
                "line": 6,
                "line_content": '\t\t\t\t\tSourceOp = "Ellipse1",\n',
                "char_count": 34,
                "tabs": 4,
                "comma": 1,
                "comma_idx": [32],
                "braces_open": None,
                "braces_open_idx": None,
                "braces_closed": None,
                "braces_closed_idx": None,
            },
        },
        'converted_name': 'Ellipse_ORIGINAL_05.setting',
        'converted_path': './converted/Ellipse_ORIGINAL_05.setting',
    },
    'Ellipse_ORIGINAL_05_Copy.setting': {
        'source_name': 'Ellipse_ORIGINAL_05_Copy.setting',
        'source_path': './Ellipse_ORIGINAL_05_Copy.setting',
        'source_content': {
            255: {
                "line": 255,
                "line_content": '\t\t\t\t\tViewInfo = OperatorInfo { Pos = { 2866.11, 103.75 } },\n',
                "char_count": 66,
                "tabs": 5,
                "comma": 1,
                "comma_idx": [64],
                "braces_open": 2,
                "braces_open_idx": [29, 37],
                "braces_closed": 2,
                "braces_closed_idx": [54, 56],
            },
        },
        'converted_name': 'Ellipse_ORIGINAL_05_Copy.setting',
        'converted_path': './converted/Ellipse_ORIGINAL_05_Copy.setting',
    }
}

# ----- V A R I A B L E S -----

content = {}

original_file_path = "./"
converted_file_path = "./converted/"
enable_debug_output = False
extension = ".setting"
min_char_count = 150

# 'content' dictionary key names
source_name = 'source_name'
source_path = 'source_path'
source_content = 'source_content'
converted_name = 'converted_name'
converted_path = 'converted_path'
line = "line"
line_content = 'line_content'
char_count = 'char_count'
tabs = 'tabs'
comma = 'comma'
comma_idx = 'comma_idx'
braces_open = "braces_open"
braces_open_idx = 'braces_open_idx'
braces_closed = 'braces_closed'
braces_closed_idx = 'braces_closed_idx'

# -----------------------------

#   Executes all the functions in order.
#   This gets triggered by the command
# ⤓ at the very bottom of this program ⤓
def execute_program():
    get_files_found(extension)
    copy_content()
    convert_content()
    folder_exists(converted_file_path)
    create_files()
    write_to_files()


def get_files_found(extension):
    '''
    Attempts to find *.setting files in the
    same folder as the 'format_macro.py'.
    If it found at least one,
    the content dictionary gets populated
    with the necessary file information.
    '''
    for file in os.listdir(original_file_path):
        if file.endswith(extension):
            content[file] = {
                source_name: file,
                source_path: original_file_path + file,
                source_content: {},
                converted_name: file,
                converted_path: converted_file_path + file,
            }


def folder_exists(folder):
    '''
    Checks if the folder exists.
    '''
    if not os.path.exists(folder):
        os.mkdir(folder)


def copy_content():
    files_imported = []
    for main in content:
        files_imported.append('./' + main)
        with open(content[main][source_path], 'r') as source_contents:
            text = source_contents.readlines()
            for next_line in range(len(text)):
                content[main][source_content][next_line + 1] = {
                    line: next_line + 1,
                    line_content: text[next_line],
                    char_count: int(len(text[next_line])),
                    tabs: find_in_line(text[next_line], '\t', 0),
                    comma: find_in_line(text[next_line], ', ', 0),
                    comma_idx: find_in_line(text[next_line], ', ', 1),
                    braces_open: find_in_line(text[next_line], '{ ', 0),
                    braces_open_idx: find_in_line(text[next_line], '{ ', 1),
                    braces_closed: find_in_line(text[next_line], ' }', 0),
                    braces_closed_idx: find_in_line(text[next_line], ' }', 1),
                }
            
            # Prints all the 'content' dictionaries,
            # if 'enable_debug_output' == True.
            if enable_debug_output == True:
                print("\n" + main + ":")
                print('├─ ' + source_name + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + content[main][source_name])
                print('├─ ' + source_path + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + content[main][source_path])
                print('├─ ' + source_content + ':')
                for x in content[main][source_content]:
                    print('│   ├─ ' + str(content[main][source_content][x][line]))
                    print('│   │   ├─ ' + line + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + str(content[main][source_content][x][line]))
                    print('│   │   ├─ ' + line_content + ': ⋅⋅⋅⋅⋅⋅⋅ ' + str([content[main][source_content][x][line_content]])[:-1][1:])
                    print('│   │   ├─ ' + char_count + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + str(content[main][source_content][x][char_count]))
                    print('│   │   ├─ ' + tabs + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + str(content[main][source_content][x][tabs]))
                    print('│   │   ├─ ' + comma + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + str(content[main][source_content][x][comma]))
                    print('│   │   ├─ ' + comma_idx + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + str(content[main][source_content][x][comma_idx]))
                    print('│   │   ├─ ' + braces_open + ': ⋅⋅⋅⋅⋅⋅⋅⋅ ' + str(content[main][source_content][x][braces_open]))
                    print('│   │   ├─ ' + braces_open_idx + ': ⋅⋅⋅⋅ ' + str(content[main][source_content][x][braces_open_idx]))
                    print('│   │   ├─ ' + braces_closed + ': ⋅⋅⋅⋅⋅⋅ ' + str(content[main][source_content][x][braces_closed]))
                    print('│   │   ├─ ' + braces_closed_idx + ': ⋅⋅ ' + str(content[main][source_content][x][braces_closed_idx]))
                    print(
                        '│   │'
                    )
                print('├─ ' + converted_name + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + content[main][converted_name])
                print('├─ ' + converted_path + ': ⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅ ' + content[main][converted_path] + '\n')
    print('  Files imported: ⋅⋅⋅⋅⋅ ' + str(files_imported)[1:][:-1])


def find_in_line(line: str = '', to_find: str = '', mode: int = 0) -> int:
    """
    Finds all occurances of a keywork (to_find) in a string (line).
    It then returns an integer. With 0: 'occurances', 1: 'line_index'.
    """
    if to_find in line:
        occurances = line.count(to_find)
        line_index = []
        if occurances == 1:
            line_index.append(line.find(to_find))
        elif occurances > 1:
            prev_index = 0
            for number in range(occurances):
                prev_index = line.find(to_find, prev_index)
                line_index.append(prev_index)
                prev_index += 1
        if mode == 0:
            return occurances
        elif mode == 1:
            return line_index


def convert_content():
    '''
    Replaces the signs
    ', ' with ',\n\t' - Adds a line break and the number of tabs (tab_count) after the comma. Removes the space.
    '{ ' with '{\n\t' - Adds a line break and the number of tabs (tab_count + 1) after the opening brace. Removes the space.
    ' }' with '\n\t}' - Adds a line break and the number of tabs (tab count - 1) before the closing brace. Removes the space.
    '''
    lines_edited = []
    for main in content:
        for source_item in content[main][source_content]:
            src_item = content[main][source_content][source_item]
            if src_item[char_count] >= min_char_count:
                tab_count = src_item[tabs]
                for index in range(src_item[char_count]):
                    if index in src_item[comma_idx]:
                        comma_with_tabs = add_tabs(',\n', tab_count)
                        src_item[line_content] = replace_nth(src_item[line_content], ', ', comma_with_tabs, 1)
                        lines_edited.append(index)
                    elif index in src_item[braces_open_idx]:
                        tab_count += 1
                        braces_open_with_tabs = add_tabs('{\n', tab_count)
                        src_item[line_content] = replace_nth(src_item[line_content], '{ ', braces_open_with_tabs, 1)
                        lines_edited.append(index)
                    elif index in src_item[braces_closed_idx]:
                        tab_count -= 1
                        braces_closed_with_tabs = add_tabs('\n', tab_count)
                        braces_closed_with_tabs += '}'
                        src_item[line_content] = replace_nth(src_item[line_content], ' }', braces_closed_with_tabs, 1)
                        lines_edited.append(index)
    
    # Places the noted changes from a list in a string
    # and adds commas and a line break for every 10th item.
    # Then prints it out.
    at_index = 10
    lines_counter = int(len(lines_edited) / at_index)
    for x in range(lines_counter):
        lines_edited.insert(at_index, '\n\t\t\t')
        at_index += 11
    new_string = ''
    for x in range(len(lines_edited)):
        if x != len(lines_edited):
            new_string += str(lines_edited[x])
            if lines_edited[x] != '\n\t\t\t':
                new_string += ', '
    print('  Lines changed: ⋅⋅⋅⋅⋅⋅ ' + str(new_string))


def create_files():
    '''
    Creates files with the same name
    as the source *.setting files
    inside the "./converted/" folder,
    preparing them for the generated
    content.
    '''
    files_created = []
    for main in content:
        with open(content[main][converted_path], 'w') as converted_file:
            converted_file.write('')
            files_created.append(converted_file_path + str(main))
    print('  Files created: ⋅⋅⋅⋅⋅⋅ ' + str(files_created)[1:][:-1])
    

def write_to_files():
    '''
    Takes the previously created
    *.setting files in "./converted/"
    and writes the formatted content.
    '''
    files_written = []
    for main in content:
        with open(content[main][converted_path], 'a') as converted_file:
            for item in content[main][source_content]:
                converted_file.write(content[main][source_content][item][line_content])
        files_written.append(converted_file_path + main)
    print('  Files written: ⋅⋅⋅⋅⋅⋅ ' + str(files_written)[1:][:-1])


def add_tabs(string: str = '', tab_count: int = 1) -> str:
    '''
    Adds a number of tab spaces (tab_count)
    to a string (string), then returns it.
    '''
    letter_with_tabs = string
    for _index in range(tab_count):
        letter_with_tabs += '\t'
    return letter_with_tabs


def replace_nth(text: str = '', old: str = '', new: str = '', nth: int = 1) -> str:
    """
    Replaces a string (old) with another string (new) in a text (text).
    You can specify which occurance of the found string should be replaced (nth).
    Example: print(replace_nth('apple apple apple', 'apple', 'banana', 2))
    Output: apple banana apple
    """
    arr = text.split(old)
    part1 = old.join(arr[:nth])
    part2 = old.join(arr[nth:])
    
    return part1 + new + part2


#################
execute_program()
#################