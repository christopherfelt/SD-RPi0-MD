#include <LowPower.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(8, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(13,LOW);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(8, HIGH);
  delay(2000);
  digitalWrite(8, LOW);
//  LowPower.powerDown(SLEEP_2S, ADC_OFF, BOD_OFF);
  LowPower.idle(SLEEP_8S, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF,
  USART0_OFF, TWI_OFF);
}
