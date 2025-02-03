# BitDogLab-MusicPlayer

🎵 Tocador de Música com LEDs e Buzzer - Raspberry Pi Pico

Este projeto implementa um sistema para tocar músicas usando um buzzer e LEDs endereçáveis (Neopixel) em um Raspberry Pi Pico. Cada nota musical acende um LED correspondente e toca a frequência correta no buzzer.

🚀 Funcionalidades

🎼 Reprodução de músicas definidas pelo usuário.

🔊 Emissão de som com um buzzer PWM.

💡 Iluminação sincronizada dos LEDs Neopixel.

🕒 Ajuste de BPM para controlar a velocidade da música.

🛠️ Requisitos

Raspberry Pi Pico

Buzzer Piezoelétrico (PWM)

LED Neopixel (pelo menos 25 LEDs)

MicroPython instalado no Raspberry Pi Pico

Biblioteca neopixel instalada

📜 Como Usar

Clone este repositório ou copie o código para seu Raspberry Pi Pico.

Conecte os LEDs ao pino GPIO 7 e o buzzer ao GPIO 21.

Defina sua música em um array no formato:

fly_me_to_the_moon = [
    ("do", "4"),
    ("re", "4"),
    ("mi", "4"),
    ("PAUSE", "4"),
    ("fa", "4"),
]

Execute o script e ouça a música enquanto os LEDs acendem!

🎨 Cores e Notas

Cada nota possui um LED específico com uma cor correspondente para visualização sincronizada.

📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

💡 Créditos

Desenvolvido para aprendizado e experimentação com som e luz em microcontroladores! 🎶
