enum DPad {RIGHT = 2, UP = 3, LEFT = 4, DOWN = 5};
enum Buttons {A = 6, B = 7, X = 8, Y = 9};

void setup() {
  // Set the DPad buttons to pullup inputs
  pinMode(RIGHT, INPUT_PULLUP);
  pinMode(UP, INPUT_PULLUP);
  pinMode(LEFT, INPUT_PULLUP);
  pinMode(DOWN, INPUT_PULLUP);
  
  // Set the action buttons to pullup inputs
  pinMode(A, INPUT_PULLUP);
  pinMode(B, INPUT_PULLUP);
  pinMode(X, INPUT_PULLUP);
  pinMode(Y, INPUT_PULLUP);

  Serial.begin(9600);

  delay(5000);

  Serial.print("AT+IMME0");
  delay(1000);
  Serial.print("AT+ROLE0");
  delay(1000);
  Serial.print("AT+TYPE0");
  delay(1000);
}

void loop() {
  // Print the Key packet
  // DPad
  Serial.print("K:");
  Serial.print(digitalRead(RIGHT));
  Serial.print(digitalRead(UP));
  Serial.print(digitalRead(LEFT));
  Serial.print(digitalRead(DOWN));
  
  // Action buttons
  Serial.print(digitalRead(A));
  Serial.print(digitalRead(B));
  Serial.print(digitalRead(X));
  Serial.println(digitalRead(Y));

  delay(1000);
}
