
from flask import Flask, render_template, request, url_for,redirect
import requests
from bs4 import BeautifulSoup
import i2c_lcd
app = Flask(__name__,template_folder='Template')
display = i2c_lcd.lcd()

@app.route('/')
def index():
    return redirect(url_for('Inicio'))

@app.route('/Inicio')
def Inicio():
    return render_template('index.html')

@app.route('/equipos')
def equipos():
    return render_template('equipos.html')

@app.route('/equipos/equipo1')
def equipos_equipo1():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[0].find_all('td')[2].get_text()
    a = rows[0].find_all('td')[3].get_text()
    ar = rows[0].find_all('td')[4].get_text()
    ars = rows[0].find_all('td')[5].get_text()
    arse = rows[0].find_all('td')[6].get_text()
    arsen = rows[0].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 1 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo2')
def equipos_equipo2():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[1].find_all('td')[2].get_text()
    a = rows[1].find_all('td')[3].get_text()
    ar = rows[1].find_all('td')[4].get_text()
    ars = rows[1].find_all('td')[5].get_text()
    arse = rows[1].find_all('td')[6].get_text()
    arsen = rows[1].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 2 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo3')
def equipos_equipo3():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[2].find_all('td')[2].get_text()
    a = rows[2].find_all('td')[3].get_text()
    ar = rows[2].find_all('td')[4].get_text()
    ars = rows[2].find_all('td')[5].get_text()
    arse = rows[2].find_all('td')[6].get_text()
    arsen = rows[2].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 3 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo4')
def equipos_equipo4():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[3].find_all('td')[2].get_text()
    a = rows[3].find_all('td')[3].get_text()
    ar = rows[3].find_all('td')[4].get_text()
    ars = rows[3].find_all('td')[5].get_text()
    arse = rows[3].find_all('td')[6].get_text()
    arsen = rows[3].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 4 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo5')
def equipos_equipo5():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[4].find_all('td')[2].get_text()
    a = rows[4].find_all('td')[3].get_text()
    ar = rows[4].find_all('td')[4].get_text()
    ars = rows[4].find_all('td')[5].get_text()
    arse = rows[4].find_all('td')[6].get_text()
    arsen = rows[4].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 5 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo6')
def equipos_equipo6():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[5].find_all('td')[2].get_text()
    a = rows[5].find_all('td')[3].get_text()
    ar = rows[5].find_all('td')[4].get_text()
    ars = rows[5].find_all('td')[5].get_text()
    arse = rows[5].find_all('td')[6].get_text()
    arsen = rows[5].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 6 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo7')
def equipos_equipo7():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[6].find_all('td')[2].get_text()
    a = rows[6].find_all('td')[3].get_text()
    ar = rows[6].find_all('td')[4].get_text()
    ars = rows[6].find_all('td')[5].get_text()
    arse = rows[6].find_all('td')[6].get_text()
    arsen = rows[6].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 7 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo8')
def equipos_equipo8():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[7].find_all('td')[2].get_text()
    a = rows[7].find_all('td')[3].get_text()
    ar = rows[7].find_all('td')[4].get_text()
    ars = rows[7].find_all('td')[5].get_text()
    arse = rows[7].find_all('td')[6].get_text()
    arsen = rows[7].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 8 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo9')
def equipos_equipo9():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[8].find_all('td')[2].get_text()
    a = rows[8].find_all('td')[3].get_text()
    ar = rows[8].find_all('td')[4].get_text()
    ars = rows[8].find_all('td')[5].get_text()
    arse = rows[8].find_all('td')[6].get_text()
    arsen = rows[8].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 9 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo10')
def equipos_equipo10():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[9].find_all('td')[2].get_text()
    a = rows[9].find_all('td')[3].get_text()
    ar = rows[9].find_all('td')[4].get_text()
    ars = rows[9].find_all('td')[5].get_text()
    arse = rows[9].find_all('td')[6].get_text()
    arsen = rows[9].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string('''Equipo:{}'''.format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 10 Premier League----** <br>
                Equipo: {} <br>
                Jugados: {} <br>
                Ganados: {} <br>
                Empatados: {} <br>
                Perdidos: {} <br>
                Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo11')
def equipos_equipo11():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[10].find_all('td')[2].get_text()
    a = rows[10].find_all('td')[3].get_text()
    ar = rows[10].find_all('td')[4].get_text()
    ars = rows[10].find_all('td')[5].get_text()
    arse = rows[10].find_all('td')[6].get_text()
    arsen = rows[10].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 11 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo12')
def equipos_equipo12():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[11].find_all('td')[2].get_text()
    a = rows[11].find_all('td')[3].get_text()
    ar = rows[11].find_all('td')[4].get_text()
    ars = rows[11].find_all('td')[5].get_text()
    arse = rows[11].find_all('td')[6].get_text()
    arsen = rows[11].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 12 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo13')
def equipos_equipo13():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[12].find_all('td')[2].get_text()
    a = rows[12].find_all('td')[3].get_text()
    ar = rows[12].find_all('td')[4].get_text()
    ars = rows[12].find_all('td')[5].get_text()
    arse = rows[12].find_all('td')[6].get_text()
    arsen = rows[12].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 13 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo14')
def equipos_equipo14():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[13].find_all('td')[2].get_text()
    a = rows[13].find_all('td')[3].get_text()
    ar = rows[13].find_all('td')[4].get_text()
    ars = rows[13].find_all('td')[5].get_text()
    arse = rows[13].find_all('td')[6].get_text()
    arsen = rows[13].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 14 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo15')
def equipos_equipo15():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[14].find_all('td')[2].get_text()
    a = rows[14].find_all('td')[3].get_text()
    ar = rows[14].find_all('td')[4].get_text()
    ars = rows[14].find_all('td')[5].get_text()
    arse = rows[14].find_all('td')[6].get_text()
    arsen = rows[14].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 15 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo16')
def equipos_equipo16():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[15].find_all('td')[2].get_text()
    a = rows[15].find_all('td')[3].get_text()
    ar = rows[15].find_all('td')[4].get_text()
    ars = rows[15].find_all('td')[5].get_text()
    arse = rows[15].find_all('td')[6].get_text()
    arsen = rows[15].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 16 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo17')
def equipos_equipo17():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[16].find_all('td')[2].get_text()
    a = rows[16].find_all('td')[3].get_text()
    ar = rows[16].find_all('td')[4].get_text()
    ars = rows[16].find_all('td')[5].get_text()
    arse = rows[16].find_all('td')[6].get_text()
    arsen = rows[16].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 17 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo18')
def equipos_equipo18():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[17].find_all('td')[2].get_text()
    a = rows[17].find_all('td')[3].get_text()
    ar = rows[17].find_all('td')[4].get_text()
    ars = rows[17].find_all('td')[5].get_text()
    arse = rows[17].find_all('td')[6].get_text()
    arsen = rows[17].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 18 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo19')
def equipos_equipo19():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[18].find_all('td')[2].get_text()
    a = rows[18].find_all('td')[3].get_text()
    ar = rows[18].find_all('td')[4].get_text()
    ars = rows[18].find_all('td')[5].get_text()
    arse = rows[18].find_all('td')[6].get_text()
    arsen = rows[18].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string("Equipo:{}".format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 19 Premier League----** <br>
               Equipo: {} <br>
               Jugados: {} <br>
               Ganados: {} <br>
               Empatados: {} <br>
               Perdidos: {} <br>
               Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

@app.route('/equipos/equipo20')
def equipos_equipo20():

    url = "https://www.goal.com/es/premier-league/clasificaci%C3%B3n/2kwbbcootiqqgmrzs6o5inle5"
    r  = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.find('table', attrs={"class":"widget-match-standings__table"}).find('tbody').find_all('tr')
    equ1 = rows[19].find_all('td')[2].get_text()
    a = rows[19].find_all('td')[3].get_text()
    ar = rows[19].find_all('td')[4].get_text()
    ars = rows[19].find_all('td')[5].get_text()
    arse = rows[19].find_all('td')[6].get_text()
    arsen = rows[19].find_all('td')[10].get_text()
    display.lcd_clear()
    display.lcd_display_string('''Equipo:{}'''.format(equ1), 1)
    display.lcd_display_string("Puntaje: {}".format(arsen),2)
    return  '''**----Posicion 20 Premier League----** <br>
                Equipo: {} <br>
                Jugados: {} <br>
                Ganados: {} <br>
                Empatados: {} <br>
                Perdidos: {} <br>
                Puntos: {}'''.format(equ1, a, ar, ars, arse, arsen)

if __name__ == "__main__":
    app.run(debug=True)
    