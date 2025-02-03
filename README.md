# BitDogLab-MusicPlayer

# 🎵 Tocador de Música com LEDs e Buzzer - Raspberry Pi Pico

Este projeto implementa um sistema para tocar músicas usando um buzzer e LEDs endereçáveis (Neopixel) em um Raspberry Pi Pico. Cada nota musical acende um LED correspondente e toca a frequência correta no buzzer.

## 🚀 Funcionalidades
- 🎼 **Reprodução de músicas** definidas pelo usuário.
- 🔊 **Emissão de som** com um buzzer PWM.
- 💡 **Iluminação sincronizada** dos LEDs Neopixel.
- 🕒 **Ajuste de BPM** para controlar a velocidade da música.

## 🛠️ Requisitos
- Raspberry Pi Pico
- Buzzer Piezoelétrico (PWM)
- LED Neopixel (pelo menos 25 LEDs)
- MicroPython instalado no Raspberry Pi Pico
- Biblioteca `neopixel` instalada
- Biblioteca `machine` instalada
- IDE Thonny

## 📝 Como Usar
1. Clone este repositório ou copie o código para seu Raspberry Pi Pico.
2. Conecte os LEDs ao pino GPIO 7 e o buzzer ao GPIO 21.
3. Configure a IDE Thonny para receber a Placa Pi Pico
4. Tempos definidos:
   ```python
   note_durations = {
    "semibreve": 1,  
    "minima": 1/2,     
    "seminima": 1/4, 
    "colcheia": 1/8, 
    "semicolcheia": 1/16,
    "fusa" : 1/32,
    "semifusa" : 1/64
}```
5. Notas definidas: Clave de Sol
# Criando o conteúdo para o README e salvando em um arquivo .md
readme_content = """
# Notas Musicais

As notas abaixo são organizadas por linha (baixa, intermediária e aguda) e incluem suas frequências e representações.

## Linha 1 (Notas mais graves)

| Nota   | Frequência (Hz) | Representação     |
|--------|-----------------|-------------------|
| do     | 261.63          | Dó 4              |
| do#    | 277.18          | Dó sustenido 4    |
| re     | 293.66          | Ré 4              |
| re#    | 311.13          | Ré sustenido 4    |
| mi     | 329.63          | Mi 4              |

## Linha 2 (Notas intermediárias)

| Nota   | Frequência (Hz) | Representação     |
|--------|-----------------|-------------------|
| fa     | 349.23          | Fá 4              |
| fa#    | 369.99          | Fá sustenido 4    |
| sol    | 392.00          | Sol 4             |
| sol#   | 415.30          | Sol sustenido 4   |
| la     | 440.00          | Lá 4              |

## Linha 3 (Notas mais agudas)

| Nota   | Frequência (Hz) | Representação     |
|--------|-----------------|-------------------|
| la#    | 466.16          | Lá sustenido 4    |
| si     | 493.88          | Si 4              |
| DO     | 523.25          | Dó 5              |
| DO#    | 554.37          | Dó sustenido 5    |
| RE     | 587.33          | Ré 5              |

## Linha 4 (Notas agudas)

| Nota   | Frequência (Hz) | Representação     |
|--------|-----------------|-------------------|
| RE#    | 622.25          | Ré sustenido 5    |
| MI     | 659.26          | Mi 5              |
| FA     | 698.46          | Fá 5              |
| FA#    | 739.99          | Fá sustenido 5    |
| SOL    | 783.99          | Sol 5             |

## Linha 5 (Notas mais agudas)

| Nota   | Frequência (Hz) | Representação     |
|--------|-----------------|-------------------|
| SOL#   | 830.61          | Sol sustenido 5   |
| LA     | 880.00          | Lá 5              |
| LA#    | 932.33          | Lá sustenido 5    |
| SI     | 987.77          | Si 5              |

## Pausa

| Nota   | Frequência (Hz) | Representação     |
|--------|-----------------|-------------------|
| PAUSE  | 0.00            | Pausa             |
"""

6. Defina sua música em um array no formato:
   ```python
   nome_da_musica = [
    ("nota1", "tempo1."),
    ("nota2", "tempo2"),
    ("nota3", "tempo3"),
    ("nota4", "tempo4")]
   ```
### Exemplo
```python
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
```
6. A função tocarMusica é responsável por reproduzir uma sequência de notas com controle de tempo e altura. 
`def tocarMusica(nome_musica, bpm=40, altura=2000):
  for nota, tempo in nome_musica:
    tocarNota(nota, tempo, altura)`
- nome_musica: Array contendo as notas da música.
- bpm (opcional): Controla a velocidade da música. O valor padrão é 40, mas pode ser ajustado conforme necessário.
- altura (opcional): Define a frequência base das notas. O valor recomendado está entre 500 e 3000.
   
7. Execute o script e ouça a música enquanto os LEDs acendem!

## 🎨 Cores e Notas
Cada nota possui um LED específico com uma cor correspondente para visualização sincronizada.

## 💡 Créditos
Desenvolvido baseado na documentação da BitDogLab (https://github.com/BitDogLab/BitDogLab)🎶
Dúvida de como instalar o MicroPython e a IDE Thonny? acesse:
https://github.com/BitDogLab/BitDogLab/tree/main/doc#iniciando-com-micropython
