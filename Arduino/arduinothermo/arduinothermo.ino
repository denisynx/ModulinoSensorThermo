#include <Modulino.h>

ModulinoThermo thermo;

float celsius = 0;
float humidity = 0;

void setup(){
  Serial.begin(115200);
  Modulino.begin();
  thermo.begin();
}

void loop(){
  celsius = thermo.getTemperature();
  humidity = thermo.getHumidity();

  // preveri veljavnost
  if (isnan(celsius) || isnan(humidity)) {
    return;
  }

  // izpis CSV formatu
  Serial.print(millis());
  Serial.print(",");
  Serial.print(celsius);
  Serial.print(",");
  Serial.println(humidity);

  delay(1000);
}

