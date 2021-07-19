from flask import Flask, render_template, request

# create a alphabet to morse code dictionary
a_morse_dict = {'a': '.- ', 'b': '-... ', 'c': '-.-. ', 'd': '-.. ', 'e': '. ',
                'f': '..-. ', 'g': '--. ', 'h': '.... ', 'i': '.. ', 'j': '.--- ',
                'k': '-.- ', 'l': '.-.. ', 'm': '-- ', 'n': '-. ', 'o': '--- ', 'p': '.--. ',
                'q': '--.- ', 'r': '.-. ', 's': '... ', 't': '- ', 'u': '..- ', 'v': '...- ',
                'w': '.-- ', 'x': '-..- ', 'y': '-.-- ', 'z': '--.. ',
                1: '.---- ', 2: '..--- ', 3: '...-- ', 4: '....- ', 5: '..... ',
                6: '-.... ', 7: '--... ', 8: '---.. ', 9: '----. ', 0: '----- '}


# covert a string to morse code
def str_to_morse(a_str):
    result = ''
    code = None
    dict_keys = list(a_morse_dict.keys())
    a_str = a_str.lower()
    for char in a_str:
        if char not in dict_keys:
            char = ''
        elif char == ' ':
            code = ' / '
        else:
            code = a_morse_dict[char]
        result += code
    return result


# remove any chars not in the dictionary keys
def clean_str(the_str):
    cleaned_str = the_str
    the_str = the_str.lower()
    for char in the_str:
        dict_keys = list(a_morse_dict.keys())
        if char not in dict_keys:
            cleaned_str = cleaned_str.replace(char, ' ').rstrip()
    return cleaned_str


# create flask app
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    the_code = ''
    the_str = ''

    if request.method == 'POST':
        a_str = request.form['mystr']
        the_code = str_to_morse(a_str)
        the_str = clean_str(a_str)

    return render_template('index.html', code=the_code, the_str=the_str)


if __name__ == '__main__':
    app.run(debug=True)
