from flask import render_template, Flask
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ftyfguhijijokopkopkpok'
Bootstrap5(app)

class TextForm(FlaskForm):
    text_field = StringField('Enter Text', validators=[validators.DataRequired()])
    submit = SubmitField('Commit')

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
    'y': '-.--', 'z': '--..',
}

@app.route('/', methods=['GET', 'POST'])
def action():
    form = TextForm()
    morse_code_string = ""
    if form.validate_on_submit():
        user_input = form.text_field.data
        morse_code_translation = []
        for char in user_input:
            if char != ' ':
                code = morse_code_dict.get(char)
                if code:
                    morse_code_translation.append(code)
                else:
                    print(f"Character '{char}' cannot be translated to Morse code.")
            else:
                morse_code_translation.append(' ')  # Add space for word separation
        
        morse_code_string = ' '.join(morse_code_translation)
        print(f"Morse Code: {morse_code_string}")  # Debug print
    return render_template('index.html', form=form, morse_code=morse_code_string)

if __name__ == '__main__':
    app.run(debug=True)
