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
4. Defina sua música em um array no formato:
   `nome_da_musica = [
    ("nota1", "tempo1."),
    ("nota2", "tempo2"),
    ("nota3", "tempo3"),
    ("nota4", "tempo4")]`
   ### Exemplo
   `do_scale = [
    ("do", "seminima"),<br>
    ("re", "colcheia"),<br>   
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
]`
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
