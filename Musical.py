from machine import Pin, PWM
import time
import neopixel
do_scale = [
    ("do", "seminima"),
    ("re", "colcheia"),
    ("mi", "colcheia"),
    ("fa", "colcheia"),
    ("sol", "colcheia"),
    ("la", "colcheia"),
    ("si", "colcheia"),
    ("DO", "colcheia"),
    ("PAUSE", "semicolcheia"),
    ("DO", "colcheia"),
    ("si", "colcheia"),
    ("la", "colcheia"),
    ("sol", "colcheia"),
    ("fa", "colcheia"),
    ("mi", "colcheia"),
    ("re", "colcheia"),
    ("do", "seminima")

]

fly_me_to_the_moon = [
    ("FA", "seminima."),
    ("MI", "colcheia"),
    ("RE", "seminima"),
    ("DO", "colcheia"),
    ("la#", "colcheia"),
    ("la#", "colcheia"),
    ("PAUSE", "colcheia"),  # Pausa equivalente a `time.sleep(0.08)`
    ("DO", "seminima"),
    ("RE", "colcheia"),
    ("FA", "seminima"),
    ("MI", "colcheia"),
    ("MI", "seminima"),
    ("RE", "seminima"),
    ("DO", "colcheia"),
    ("la#", "seminima"),
    ("la", "semibreve"),
    ("PAUSE", "colcheia"),  # Pausa equivalente a `time.sleep(0.05)`
    ("RE", "seminima."),
    ("DO", "colcheia"),
    ("la#", "seminima"),
    ("la", "colcheia"),
    ("sol", "colcheia"),
    ("sol", "seminima"),
    ("la", "seminima"),
    ("la#", "seminima"),
    ("RE", "seminima"),
    ("DO#", "seminima."),
    ("la#", "colcheia"),
    ("la", "seminima"),
    ("sol", "colcheia"),
    ("fa", "colcheia"),
    ("fa", "minima."),
    ("fa#", "seminima"),
    ("sol", "seminima."),
    ("RE", "colcheia"),
    ("RE", "minima"),
    ("RE", "minima"),
    ("MI", "seminima"),
    ("FA", "seminima"),
    ("DO", "semibreve"),
    ("DO", "minima"),
    ("PAUSE", "colcheia"),  # Pausa equivalente a `time.sleep(0.08)`
    ("mi", "colcheia"),
    ("fa", "seminima."),
    ("la#", "colcheia"),
    ("la#", "minima"),
    ("la#", "seminima"),
    ("RE", "minima"),
    ("DO", "seminima"),
    ("la#", "seminima."),
    ("la", "colcheia"),
    ("la", "minima"),
    ("la", "semibreve")
]


note_durations = {
    "semibreve": 1,  
    "minima": 1/2,     
    "seminima": 1/4, 
    "colcheia": 1/8, 
    "semicolcheia": 1/16,
    "fusa" : 1/32,
    "semifusa" : 1/64
}
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

buzzer = PWM(Pin(21))  # Conecte o buzzer 
buzzer.duty_u16(0)  # Desliga o buzzer inicialmente

notes = {
    # Linha 1 (Notas mais graves)
    "do": {"frequencia": 261.63, "rgb": (0, 50, 0), "index" : 0},    # Dó 4
    "do#": {"frequencia": 277.18, "rgb": (0, 120, 0), "index" : 1},   # Dó sustenido 4
    "re": {"frequencia": 293.66, "rgb": (0, 180, 0), "index" : 2},    # Ré 4
    "re#": {"frequencia": 311.13, "rgb": (0, 240, 0), "index" : 3},    # Ré sustenido 4
    "mi": {"frequencia": 329.63, "rgb": (0, 200, 80), "index" : 4},     # Mi 4
    
    # Linha 2 (Notas intermediárias)
    "fa": {"frequencia": 349.23, "rgb": (0, 0, 60), "index" : 5},    # Fá 4
    "fa#": {"frequencia": 369.99, "rgb": (0, 0, 140), "index" : 6},   # Fá sustenido 4
    "sol": {"frequencia": 392.00, "rgb": (0, 0, 200), "index" : 7},   # Sol 4
    "sol#": {"frequencia": 415.30, "rgb": (0, 100, 255), "index" : 8},  # Sol sustenido 4
    "la": {"frequencia": 440.00, "rgb": (0, 180, 220), "index" : 9},    # Lá 4

    # Linha 3 (Notas mais agudas)
    "la#": {"frequencia": 466.16, "rgb": (40, 0, 80), "index" : 10},   # Lá sustenido 4
    "si": {"frequencia": 493.88, "rgb": (80, 0, 160), "index" : 11},    # Si 4
    "DO": {"frequencia": 523.25, "rgb": (120, 0, 220), "index" : 12},    # Dó 5
    "DO#": {"frequencia": 554.37, "rgb": (180, 100, 255), "index" : 13},     # Dó sustenido 5
    "RE": {"frequencia": 587.33, "rgb": (140, 60, 190), "index" : 14},      # Ré 5

    # Linha 4 (Notas agudas)
    "RE#": {"frequencia": 622.25, "rgb": (60, 0, 0), "index" : 15},   # Ré sustenido 5
    "MI": {"frequencia": 659.26, "rgb": (140, 0, 0), "index" : 16},    # Mi 5
    "FA": {"frequencia": 698.46, "rgb": (200, 20, 20), "index" : 17},    # Fá 5
    "FA#": {"frequencia": 739.99, "rgb": (255, 50, 50), "index" : 18},   # Fá sustenido 5
    "SOL": {"frequencia": 783.99, "rgb": (220, 80, 120), "index" : 19},     # Sol 5

    # Linha 5 (Notas mais agudas)
    "SOL#": {"frequencia": 830.61, "rgb": (90, 40, 0), "index" : 20},    # Sol sustenido 5
    "LA": {"frequencia": 880.00, "rgb": (160, 80, 0), "index" : 21},      # Lá 5
    "LA#": {"frequencia": 932.33, "rgb": (220, 140, 0), "index" : 22},    # Lá sustenido 5
    "SI": {"frequencia": 987.77, "rgb": (255, 190, 80), "index" : 23},
    "PAUSE" : {"frequencia" : 0.0, "rgb": (0, 0, 0), "index" : 24}
}
def apagar_todos():
    """ Desliga todos os LEDs """
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def calcular_tempo(tempo, bpm):
    has_dot = "." in tempo
    tempo = tempo.replace(".", "")  # Remove ponto da duração da nota
    
    if tempo in note_durations:
        tempo_segundos = (60 / bpm) * note_durations[tempo]  # Converte para segundos com base no BPM
        if has_dot:
            tempo_segundos += tempo_segundos / 2  # Aumenta 50% do tempo original
        return tempo_segundos
    else:
        print(f"Tempo '{tempo}' não reconhecido.")
        return None

def tocar_buzzer(frequencia, tempo_segundos):
    buzzer.freq(int(frequencia))  
    buzzer.duty_u16(500)  # MUDE AQUI A ALTURA DA MUSICA VALOR PADRÃO: 32768 
    time.sleep(tempo_segundos)  
    buzzer.duty_u16(0)
def ativarLed(index, rgb):
    """ Acende um LED com a cor ajustada """
    np[index] = rgb  # Configura a cor do LED
    np.write()  # Atualiza os LEDs
def acender_led(nota):
    if nota in notes:
        index = notes[nota]["index"]  # Obtém o índice diretamente do dicionário
        rgb = notes[nota]["rgb"]  # Obtém a cor RGB
        ativarLed(index, rgb)

def tocarNota(nota, tempo, bpm=40):
    apagar_todos()  # Apaga todos os LEDs

    if nota in notes:
        frequencia = notes[nota]["frequencia"]
        tempo_segundos = calcular_tempo(tempo, bpm)
        
        if tempo_segundos:
            print(f"Tocando nota: {nota}, Frequência: {frequencia}Hz, Tempo: {tempo_segundos} segundos")
            if nota == "PAUSE":
                time.sleep(tempo_segundos)
            else:
                acender_led(nota)
                tocar_buzzer(frequencia, tempo_segundos)
    else:
        print("Nota não encontrada!")
        
for nota, tempo in fly_me_to_the_moon:
    tocarNota(nota, tempo)











