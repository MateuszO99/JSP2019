import urllib.request
import re

class Zadanie1():
    def __init__(self, link):
        self.link = link

    def check(self):
        try:
            urllib.request.urlopen(self.link).getcode()
            return 'Jest taka strona'
        except:
            return 'Nie ma takiej strony'

class Zadanie3():
    def __init__(self, text):
        self.text = text

    def find_links(self):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]|[.]|[/]))+',
                          self.text)
        print("Urls: ", urls)

class Zadanie4():
    def __init__(self, text):
        self.text = text

    def find_words(self):
        a_and_b = re.findall(' a[a-zA-Z]+| A[a-zA-Z]+| b[a-zA-Z]+| B[a-zA-Z]+', self.text)
        print(a_and_b)

class Zadanie5():
    def __init__(self, text):
        self.text = text

    def change(self):
        return re.sub(r"([a-z])([A-Z])", r"\1 \2", self.text)

class CiagArytmetyczny():
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def __len__(self):
        return self.a1 + self.r

    def __iter__(self):
        self.start = 1
        return self

    def __next__(self):
        if self.start <= self.n:
            result = self.a1
            self.a1 = self.__len__()
            self.start += 1
            return result
        else:
            raise StopIteration()

    def save_file(self, *args):
        file = open('ciag.txt', 'w')
        for a in args:
            file.write(str(a))
        file.close()

def main():
    work = False
    while not work:
        try:
            exercise = int(input('Które zadanie uruchomić: '))
            work = True
        except ValueError:
            print('Numer zadania musi być od 1 do 10!')

    if exercise == 1:
        z1 = Zadanie1('http://www.stackoverflow.com')
        print(z1.check())
    elif exercise == 3:
        z3 = Zadanie3('''Before you can use EZSheets, you need to enable the Google Sheets 
        and Google Drive APIs for your Google account. Visit the following web pages and 
        click the Enable API buttons at the top of each:

        https://console.developers.google.com/apis/library/sheets.googleapis.com/
        https://console.developers.google.com/apis/library/drive.googleapis.com/
        You’ll also need to obtain three files, which you should save in the same 
        folder as your .py Python script that uses EZSheets:

        A credentials file named credentials-sheets.json
        A token for Google Sheets named token-sheets.pickle
        A token for Google Drive named token-drive.pickle
        The credentials file will generate the token files. The easiest way to obtain a 
        credentials file is to go to the Google Sheets Python Quickstart page at 
        https://developers.google.com/sheets/api/quickstart/python/ and click the blue Enable 
        the Google Sheets API button, as shown in Figure 14-1. You’ll need to log in to your 
        Google account to view this page.''')
        z3.find_links()
    elif exercise == 4:
        z4 = Zadanie4(''' Before you can use EZSheets, you need to enable the Google Sheets 
        and Google Drive APIs for your Google account. Visit the following web pages and 
        click the Enable API buttons at the top of each:

        https://console.developers.google.com/apis/library/sheets.googleapis.com/
        https://console.developers.google.com/apis/library/drive.googleapis.com/
        You’ll also need to obtain three files, which you should save in the same 
        folder as your .py Python script that uses EZSheets:

        A credentials file named credentials-sheets.json
        A token for Google Sheets named token-sheets.pickle
        A token for Google Drive named token-drive.pickle
        The credentials file will generate the token files. The easiest way to obtain a 
        credentials file is to go to the Google Sheets Python Quickstart page at 
        https://developers.google.com/sheets/api/quickstart/python/ and click the blue Enable 
        the Google Sheets API button, as shown in Figure 14-1. You’ll need to log in to your 
        Google account to view this page.''')
        z4.find_words()
    elif exercise == 5:
        z5 = Zadanie5('TheLongAndWindingRoad')
        print(z5.change())
    elif exercise == 6:
        z6 = CiagArytmetyczny(2, 3, 4)
        z = list(z6)
        print(z)
        z6.save_file(z)
    else:
        print('Nie ma takiego zadania')

if __name__ == '__main__':
    main()