int ldrPin = A0;  // Définir la broche où la LDR est connectée

void setup() {
  Serial.begin(9600);  // Démarrer la communication série
}

void loop() {
  int ldrValue = analogRead(ldrPin);  // lire la valeur de la LDR

  // Afficher la valeur de la LDR dans le moniteur série
  Serial.print("Valeur de la LDR : ");
  Serial.println(ldrValue);

  delay(1000);  // Délai d'une seconde avant la prochaine lecture
}
