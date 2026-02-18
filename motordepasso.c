#include <xc.h>
#include <pic16f886.h>

#define _XTAL_FREQ 8000000  // Frequência do clock

// Sequência Half Step (8 estados)
const unsigned char halfStepStates[8] = {1, 3, 2, 6, 4, 12, 8, 9};

long motor_position = 0;

void stepper_init(void) {
    TRISB &= 0b11110000;      // RB0 a RB3 como saída
    ANSELH &= 0b11110000;     // Digital nos pinos RB0-RB3
    PORTB &= 0b11110000;      // Zera as saídas
}

unsigned int read_adc(unsigned char channel) {
    ADCON0 = (channel << 2);
    ADCON0 |= 0b00000001;
    __delay_us(20);
    GO_nDONE = 1;
    while (GO_nDONE);
    return ((ADRESH << 8) | ADRESL);
}

void stepper_set(int steps, unsigned int step_time) {
    static int index = 0;

    while (steps != 0) {
        PORTB = (PORTB & 0b11110000) | halfStepStates[index];

        if (steps > 0) {
            index = (index >= 7) ? 0 : index + 1;
            steps--;
            motor_position++;
        } else {
            index = (index <= 0) ? 7 : index - 1;
            steps++;
            motor_position--;
        }

        for (unsigned int j = 0; j < step_time; j++) {
            __delay_ms(1);
        }
    }
}

void main(void) {
    OSCCON = 0b01110000;  // Clock interno 8MHz
    ADCON1 = 0b10000000;  // ADC justificado à esquerda
    ADCON0 = 0b00000001;  // Liga o ADC

    stepper_init();

    while (1) {
        unsigned int adc_value = read_adc(0);   // Lê o potenciômetro (0-1023)

        long target_position = adc_value;       // Cada valor ADC representa exatamente 1 passo

        long diff = target_position - motor_position;

        if (diff > 0) {
            stepper_set(1, 2);  // Um passo para frente
        } else if (diff < 0) {
            stepper_set(-1, 2); // Um passo para trás
        }
    }
}
