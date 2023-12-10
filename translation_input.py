from googletrans import Translator, LANGUAGES

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
import traceback
from waveshare_OLED import OLED_1in51
from PIL import Image, ImageDraw, ImageFont

def get_user_input():
    user_input = input("Enter the text you want to translate: ")
    return user_input.strip()

def get_target_language():
    print("\nChoose a target language:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

    while True:
        target_language_code = input("Enter the language code (e.g., 'es' for Spanish): ").lower()
        if target_language_code in LANGUAGES:
            return target_language_code
        else:
            print("Invalid language code. Please try again.")

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    
    disp = OLED_1in51.OLED_1in51()

    logging.info("\r1.51inch OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()
    
    spaces = r"              "
    show = spaces + "Enter text to" + "\n" + spaces + "translate" 
    
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 9)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    logging.info("***draw text")
    draw.text((0, 0), show, font=font1, fill=0)
    image1 = image1.rotate(90)
    disp.ShowImage(disp.getbuffer(image1))
    
    user_text = get_user_input()
    
    disp.clear()
    
    spaces = r"              "
    show = spaces + "Now enter" + '\n' + "target language" 

    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 9)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    logging.info("***draw text")
    draw.text((0, 0), show, font=font1, fill=0)
    image1 = image1.rotate(90)
    disp.ShowImage(disp.getbuffer(image1))
    
    target_language = get_target_language()
    
    disp.clear()

    translated_text = translate_text(user_text, target_language)
    
    show = spaces + "Your" + "\n" + spaces +  "translated text is:" 

    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 9)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    logging.info("***draw text")
    draw.text((0, 0), show, font=font1, fill=0)
    
    time.sleep(10)
    
    image1 = Image.new('1', (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image1)
    font1 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 9)
    font2 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    logging.info("***draw text")
    display_translate = spaces + translated_text
    draw.text((0, 0), display_translate, font=font1, fill=0)
    image1 = image1.rotate(90)
    disp.ShowImage(disp.getbuffer(image1))
    
    time.sleep(10)
    
    disp.clear()

    print(spaces + "\nOriginal Text:" + '\n', user_text)
    print(spaces + "Translated Text:" + '\n', translated_text)

if __name__ == "__main__":
    main()
