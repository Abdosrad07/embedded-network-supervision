unsigned long previousMillis = 0;
const long interval = 2000; // envoi toutes les deuw secondes
const int ledPin = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  randomSeed(analogRead(A0)); // initialise le générateur pseudo-aléatoire

}

void loop() {
  // put your main code here, to run repeatedly:
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    int simulatedData = random(20, 40); // donnée simulée
    int checksum = simulatedData + 1;
    digitalWrite(ledPin, HIGH); // LED ON

    Serial.print("<START>|ID:01|DATA:");
    Serial.print(simulatedData);
    Serial.print("|TIME:");
    Serial.print(currentMillis);
    Serial.print("|CHK:");
    Serial.print(checksum);
    Serial.println("|<END>");

    delay(100);
    digitalWrite(ledPin, LOW); // LED OFF
  }
}
