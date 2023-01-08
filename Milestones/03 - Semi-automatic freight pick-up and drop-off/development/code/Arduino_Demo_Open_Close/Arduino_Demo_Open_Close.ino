//------------------------------------------------------------------------------
// CargoHolder - Democode - open-close
//
// This Arduino code will open / close the cargo holder when a button is
// pressed.
//
// This file is part of the AutonomousDroneDeliverySystem:
// https://github.com/Andreas-Menzel/AutonomousDroneDeliverySystem
//------------------------------------------------------------------------------
// @author: Andreas Menzel
//------------------------------------------------------------------------------

#include <Servo.h>

Servo myservo;

uint8_t PIN_SERVO = 9;
uint8_t PIN_BUTTON = 7;

uint16_t SERVO_VAL_CLOSED = 70;
uint16_t SERVO_VAL_OPEN = 180;

void setup() {
  Serial.begin(9600);
  
  myservo.attach(PIN_SERVO);
  pinMode(PIN_BUTTON, INPUT_PULLUP);
}

void loop() {
  myservo.write(SERVO_VAL_CLOSED);
  delay(100);

  while(digitalRead(PIN_BUTTON) == HIGH) ; // wait until button is pressed
  while(digitalRead(PIN_BUTTON) == LOW) ;  // wait until button is released

  myservo.write(SERVO_VAL_OPEN);
  delay(100);

  while(digitalRead(PIN_BUTTON) == HIGH) ; // wait until button is pressed
  while(digitalRead(PIN_BUTTON) == LOW) ;  // wait until button is released
}