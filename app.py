from flask import Flask, render_template, request
import pytesseract
import re
from preprocess import *
import os

# set path for tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# set path for upload and result folder
UPLOAD_FOLDER = 'static/'
RESULT_FOLDER = 'Results/'

# make upload and result folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(RESULT_FOLDER):
    os.makedirs(RESULT_FOLDER)

# set default values for global variables
fname = None
img_tag = None

app = Flask(__name__)

# function to write results to txt file
def write_to_file(name, email, phone, address):
    # get filename for txt file
    txt_fname = RESULT_FOLDER + fname.split('.')[0] + '.txt'
    # if any of the extracted information is None, then set it to 'Not Found'
    if name is None:
        name = 'Not Found'
    if email is None:
        email = 'Not Found'
    if phone is None:
        phone = 'Not Found'
    if address is None:
        address = 'Not Found'
    # write results to the file
    with open(txt_fname, 'w') as f:
        f.write(f'Name: {name}\n')
        f.write(f'Email: {email}\n')
        f.write(f'Phone: {phone}\n')
        if address:
            address = address.replace('\n', ' ')
        f.write(f'Address: {address}\n')
    f.close()

# define index route or home route
@app.route('/')
def index():
    # render index.html with default values
    return render_template('index.html', name="-", email="-", phone="-", address="-")

# define upload route that uploads image of detected card to static folder
@app.route('/upload', methods=['POST'])
def upload():
    # global variables to store image name and image tag
    global fname, img_tag
    # get image from form
    file = request.files['image']
    # get filename
    fname = file.filename
    # read image
    img = file.read()
    # read opencv image
    img = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_UNCHANGED)
    # create instance of Card class
    card = Preprocess(img)
    # detect card from image
    img = card.detect_card_from_image()
    # upload image to static folder
    cv2.imwrite(UPLOAD_FOLDER + fname, img)
    # set image path
    img_path = UPLOAD_FOLDER + fname
    # set image tag with image path
    img_tag = f'<img src="{img_path}" alt="Card Image" class="block shadow-xl rounded-md border border-slate-900 mx-auto w-[300px]">'
    # render index.html with image tag and values
    return render_template('index.html', name="-", email="-", phone="-", address="-", img_tag=img_tag)


# define extract route that extract information from image
@app.route('/extract', methods=['POST'])
def extract():
    # global variables to store image name and image tag
    global fname, img_tag
    # if fname is not None, read image from static folder
    if fname:
        # read image from static folder
        img = cv2.imread(UPLOAD_FOLDER + fname)
    else:
        # if fname is None, then re render index.html with default values
        return render_template('index.html', name="-", email="-", phone="-", address="-")
    # extract text from image using tesseract
    text = pytesseract.image_to_string(img, lang='eng')

    # extract name
    name = re.search(r"\b[A-Za-zÀ-ÖØ-öø-ſ'-]+(?: [A-Za-zÀ-ÖØ-öø-ſ'-]+)+\b", text)
    # if name is not found, then set it to None
    if name:
        name = name.group()
    else:
        name = None

    # extract email
    email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    # if email is not found, then set it to None
    if len(email) == 0:
        email = None
    else:
        email = email[0]
    
    # extract phone number
    phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
    # if phone number is not found, then set it to None
    if len(phone) == 0:
        phone = None
    else:
        phone = phone[0]

    # extract address
    address = re.search(r'\d+ .+[\r\n|\n](.+[\r\n|\n])?.+(?<![A-Za-z])[A-Z]{2} \d{5}(-\d{4})?', text)
    # if address is not found, then set it to None
    if address:
        # group() concatenates all the matches and returns it as a string
        address = address.group()
    else:
        address = None

    # write results to txt file
    write_to_file(name, email, phone, address)

    # render index.html with extracted values and image tag
    return render_template('index.html', name=name, email=email, phone=phone, address=address, img_tag=img_tag)

# run app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')