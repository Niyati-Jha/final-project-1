#include <ESP8266WiFi.h>
#include <EEPROM.h>
int val;
#define USE_SERIAL Serial
#define vib A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(100);

}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(vib);
  Serial.print(val);
  Serial.println(" ");
  delay(100);

}
